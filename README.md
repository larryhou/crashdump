# crashdump
Symblicate tool for Android crash log

## extract *.so symbols

Suppose you store Android apktool at `~/Library/Android/apktool/apktool_2.2.4.jar`, then you can add `apkdump` command into `/usr/local/bin/apkdump

> /usr/local/bin/apkdump
```
#!/usr/bin/env bash
set -x
java -jar ~/Library/Android/apktool/apktool_2.2.4.jar -f d ${*}
```

```
apkdump -o dump some.apk
```


## symblicate crash log

```
crashdump -p dump/lib/armeabi-v7a -f crash.txt
```

If you want more crash details, maybe you should supply debug so files to `crashdump`.

