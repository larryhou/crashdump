#!/usr/bin/env python3
import os.path as p
import os, re, io

class OpenProxy(object):
    def write(self, v):
        print(v)

    def seek(self, v):
        pass

    def read(self):
        pass

    def close(self):
        pass

def symbolicate(libname, stack, fp):
    if not libname in libmap:
        for _, line in stack:
            fp.write(line)
        return
    command = '/usr/local/bin/arm-linux-androideabi-addr2line -f -p -a -C -i -e {} {}'.format(
        libmap.get(libname), ' '.join([x[0] for x in stack])
    )
    content = os.popen(command).read()
    buffer = io.StringIO(content)
    index = 0
    for line in buffer.readlines():
        fp.write(libname + ' ' + line[:-1] + ' /* ' + stack[index][1][:-1] + ' */\n')
        index += 1

def main():
    import argparse, sys
    arguments = argparse.ArgumentParser()
    arguments.add_argument('--symbol-path', '-p', default=p.expanduser('~/Documents/Symbols/Android/godgame'))
    arguments.add_argument('--crash-file', '-f', nargs='+', required=True)
    options = arguments.parse_args(sys.argv[1:])
    for file_name in os.listdir(options.symbol_path):
        if not file_name.endswith('.so'): continue
        libmap[file_name] = p.abspath(p.join(options.symbol_path, file_name))
    for crash_file in options.crash_file:
        cursor, stack = '', []
        with open(crash_file, 'r+') as fp:
            output = open(p.dirname(fp.name) + '/dump_' + p.basename(fp.name), 'w+')
            pattern = re.compile(r'\s+pc\s+([a-f0-9]{8})\s+', re.IGNORECASE)
            while True:
                line = fp.readline()
                if not line:
                    if stack: symbolicate(cursor, stack, output)
                    break
                match = pattern.search(line)
                libpos = line.find('/lib/arm/')
                if not match or libpos == -1:
                    if stack:
                        symbolicate(cursor, stack, output)
                        cursor, stack = '', []
                    output.write(line)
                else:
                    address = pattern.search(line).group(1)
                    libname = p.basename(line[libpos:].split(' ', 1)[0])
                    if not cursor:
                        cursor, stack = libname, []
                    elif cursor != libname:
                        symbolicate(cursor, stack, output)
                        cursor, stack = libname, []
                    stack.append((address, line))
            output.seek(0)
            print(output.read())
            output.close()


if __name__ == '__main__':
    libmap = {}
    main()
