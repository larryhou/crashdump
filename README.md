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


>raw crash log
>1 #00 pc 0001a2cc /system/lib/libc.so (strlen+71) [armeabi-v8::5384836a47b4d9f81b4da285fb380e5c]
2 #01 pc 0048a8c8 /data/app/com.tencent.godgame-jD8v7SMfqpR-BEgtNVDyqg==/lib/arm/libunity.so [armeabi-v7a::ea6a07752df91d3fd3dd621fcefca534]
3 #02 pc 0093e5f8 /data/app/com.tencent.godgame-jD8v7SMfqpR-BEgtNVDyqg==/lib/arm/libunity.so [armeabi-v7a::ea6a07752df91d3fd3dd621fcefca534]
4 #03 pc 0047b988 /data/app/com.tencent.godgame-jD8v7SMfqpR-BEgtNVDyqg==/lib/arm/libunity.so [armeabi-v7a::ea6a07752df91d3fd3dd621fcefca534]
5 #04 pc 0047b1ec /data/app/com.tencent.godgame-jD8v7SMfqpR-BEgtNVDyqg==/lib/arm/libunity.so [armeabi-v7a::ea6a07752df91d3fd3dd621fcefca534]
6 #05 pc 00459794 /data/app/com.tencent.godgame-jD8v7SMfqpR-BEgtNVDyqg==/lib/arm/libunity.so [armeabi-v7a::ea6a07752df91d3fd3dd621fcefca534]
7 #06 pc 003c94d0 /data/app/com.tencent.godgame-jD8v7SMfqpR-BEgtNVDyqg==/lib/arm/libunity.so [armeabi-v7a::ea6a07752df91d3fd3dd621fcefca534]
8 #07 pc 003c97fc /data/app/com.tencent.godgame-jD8v7SMfqpR-BEgtNVDyqg==/lib/arm/libunity.so [armeabi-v7a::ea6a07752df91d3fd3dd621fcefca534]
9 #08 pc 004d8eb4 /data/app/com.tencent.godgame-jD8v7SMfqpR-BEgtNVDyqg==/lib/arm/libunity.so [armeabi-v7a::ea6a07752df91d3fd3dd621fcefca534]
10 #09 pc 004df388 /data/app/com.tencent.godgame-jD8v7SMfqpR-BEgtNVDyqg==/lib/arm/libunity.so [armeabi-v7a::ea6a07752df91d3fd3dd621fcefca534]
11 #10 pc 004dff1c /data/app/com.tencent.godgame-jD8v7SMfqpR-BEgtNVDyqg==/lib/arm/libunity.so [armeabi-v7a::ea6a07752df91d3fd3dd621fcefca534]
12 #11 pc 004e34c8 /data/app/com.tencent.godgame-jD8v7SMfqpR-BEgtNVDyqg==/lib/arm/libunity.so [armeabi-v7a::ea6a07752df91d3fd3dd621fcefca534]
13 #12 pc 0001b213 /data/app/com.tencent.godgame-jD8v7SMfqpR-BEgtNVDyqg==/oat/arm/base.odex (oatexec+531) [armeabi::89cbf21cdc3d12c922b85ad8b8854f9e]
14 java:
15 com.unity3d.player.UnityPlayer.nativeRender(Native Method)
16 com.unity3d.player.UnityPlayer.c(Unknown Source:0)
17 com.unity3d.player.UnityPlayer$e$2.queueIdle(Unknown Source:72)
18 android.os.MessageQueue.next(MessageQueue.java:394)
19 android.os.Looper.loop(Looper.java:148)
20 com.unity3d.player.UnityPlayer$e.run(Unknown Source:32)


>symblicated crash log
>1 #00 pc 0001a2cc /system/lib/libc.so (strlen+71) [armeabi-v8::5384836a47b4d9f81b4da285fb380e5c]
libunity.so 0x0048a8c8: std::_Rb_tree<int, std::pair<int const, int>, std::_Select1st<std::pair<int const, int> >, std::less<int>, std::allocator<std::pair<int const, int> > >::_M_erase(std::_Rb_tree_node<std::pair<int const, int> >*) at ??:? /* 2 #01 pc 0048a8c8 /data/app/com.tencent.godgame-jD8v7SMfqpR-BEgtNVDyqg==/lib/arm/libunity.so [armeabi-v7a::ea6a07752df91d3fd3dd621fcefca534] */
libunity.so 0x0093e5f8: std::vector<unsigned char, std::allocator<unsigned char> >::operator=(std::vector<unsigned char, std::allocator<unsigned char> > const&) at ??:? /* 3 #02 pc 0093e5f8 /data/app/com.tencent.godgame-jD8v7SMfqpR-BEgtNVDyqg==/lib/arm/libunity.so [armeabi-v7a::ea6a07752df91d3fd3dd621fcefca534] */
libunity.so 0x0047b988: std::_Rb_tree<int, std::pair<int const, int>, std::_Select1st<std::pair<int const, int> >, std::less<int>, std::allocator<std::pair<int const, int> > >::_M_erase(std::_Rb_tree_node<std::pair<int const, int> >*) at ??:? /* 4 #03 pc 0047b988 /data/app/com.tencent.godgame-jD8v7SMfqpR-BEgtNVDyqg==/lib/arm/libunity.so [armeabi-v7a::ea6a07752df91d3fd3dd621fcefca534] */
libunity.so 0x0047b1ec: std::_Rb_tree<int, std::pair<int const, int>, std::_Select1st<std::pair<int const, int> >, std::less<int>, std::allocator<std::pair<int const, int> > >::_M_erase(std::_Rb_tree_node<std::pair<int const, int> >*) at ??:? /* 5 #04 pc 0047b1ec /data/app/com.tencent.godgame-jD8v7SMfqpR-BEgtNVDyqg==/lib/arm/libunity.so [armeabi-v7a::ea6a07752df91d3fd3dd621fcefca534] */
libunity.so 0x00459794: std::_Rb_tree<int, std::pair<int const, int>, std::_Select1st<std::pair<int const, int> >, std::less<int>, std::allocator<std::pair<int const, int> > >::_M_erase(std::_Rb_tree_node<std::pair<int const, int> >*) at ??:? /* 6 #05 pc 00459794 /data/app/com.tencent.godgame-jD8v7SMfqpR-BEgtNVDyqg==/lib/arm/libunity.so [armeabi-v7a::ea6a07752df91d3fd3dd621fcefca534] */
libunity.so 0x003c94d0: void std::vector<unsigned int, std::allocator<unsigned int> >::_M_assign_aux<__gnu_cxx::__normal_iterator<unsigned int*, std::vector<unsigned int, std::allocator<unsigned int> > > >(__gnu_cxx::__normal_iterator<unsigned int*, std::vector<unsigned int, std::allocator<unsigned int> > >, __gnu_cxx::__normal_iterator<unsigned int*, std::vector<unsigned int, std::allocator<unsigned int> > >, std::forward_iterator_tag) at ??:? /* 7 #06 pc 003c94d0 /data/app/com.tencent.godgame-jD8v7SMfqpR-BEgtNVDyqg==/lib/arm/libunity.so [armeabi-v7a::ea6a07752df91d3fd3dd621fcefca534] */
libunity.so 0x003c97fc: void std::vector<unsigned int, std::allocator<unsigned int> >::_M_assign_aux<__gnu_cxx::__normal_iterator<unsigned int*, std::vector<unsigned int, std::allocator<unsigned int> > > >(__gnu_cxx::__normal_iterator<unsigned int*, std::vector<unsigned int, std::allocator<unsigned int> > >, __gnu_cxx::__normal_iterator<unsigned int*, std::vector<unsigned int, std::allocator<unsigned int> > >, std::forward_iterator_tag) at ??:? /* 8 #07 pc 003c97fc /data/app/com.tencent.godgame-jD8v7SMfqpR-BEgtNVDyqg==/lib/arm/libunity.so [armeabi-v7a::ea6a07752df91d3fd3dd621fcefca534] */
libunity.so 0x004d8eb4: UnitySendMessage at ??:? /* 9 #08 pc 004d8eb4 /data/app/com.tencent.godgame-jD8v7SMfqpR-BEgtNVDyqg==/lib/arm/libunity.so [armeabi-v7a::ea6a07752df91d3fd3dd621fcefca534] */
libunity.so 0x004df388: UnitySendMessage at ??:? /* 10 #09 pc 004df388 /data/app/com.tencent.godgame-jD8v7SMfqpR-BEgtNVDyqg==/lib/arm/libunity.so [armeabi-v7a::ea6a07752df91d3fd3dd621fcefca534] */
libunity.so 0x004dff1c: UnitySendMessage at ??:? /* 11 #10 pc 004dff1c /data/app/com.tencent.godgame-jD8v7SMfqpR-BEgtNVDyqg==/lib/arm/libunity.so [armeabi-v7a::ea6a07752df91d3fd3dd621fcefca534] */
libunity.so 0x004e34c8: UnitySendMessage at ??:? /* 12 #11 pc 004e34c8 /data/app/com.tencent.godgame-jD8v7SMfqpR-BEgtNVDyqg==/lib/arm/libunity.so [armeabi-v7a::ea6a07752df91d3fd3dd621fcefca534] */
13 #12 pc 0001b213 /data/app/com.tencent.godgame-jD8v7SMfqpR-BEgtNVDyqg==/oat/arm/base.odex (oatexec+531) [armeabi::89cbf21cdc3d12c922b85ad8b8854f9e]
14 java:
15 com.unity3d.player.UnityPlayer.nativeRender(Native Method)
16 com.unity3d.player.UnityPlayer.c(Unknown Source:0)
17 com.unity3d.player.UnityPlayer$e$2.queueIdle(Unknown Source:72)
18 android.os.MessageQueue.next(MessageQueue.java:394)
19 android.os.Looper.loop(Looper.java:148)
20 com.unity3d.player.UnityPlayer$e.run(Unknown Source:32)
