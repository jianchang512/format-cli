# 一个极简的音视频格式转换工具

![image](https://github.com/jianchang512/format-cli/assets/3378335/77d3c00e-b397-4290-a274-278277841de2)


使用 python 和 ffmpeg.exe ,实现音频视频格式之间的转换。

执行 `python geshi.py`或双击 `geshi.exe`,然后根据提示输入 `旧格式->新格式`，回车，即可将当前目录下所有旧格式文件转为新格式

也可在 `cfg.txt` 中

通过 `source_ext=` 指定旧格式列表,默认将转换 mp3, flac, aac, mp4, mov, mkv, mpeg, avi, m4a

通过 `target_ext=` 指定要转换到的格式，默认将上面指定的格式转换到 wav

通过 `dir=` 指定要进行转换处理的目录，默认是当前目录




```

source_ext=mp3, flac, aac, mp4, mov, mkv, mpeg, avi, m4a
target_ext=wav
dir=./

```


## 源码使用方法

0. 确保已有python环境

1. 下载源码解压，执行 `python geshi.py`

2. 如有需要可修改 `cfg.txt`

3. 根据提示输入执行,比如想将 avi 转为 mp4 格式，直接输入 `avi->mp4` 回车


## 预打包版

0. 下载压缩包并解压

1. 如有需要可修改 cfg.txt ，指定要转换的格式和目录，或将 geshi.exe  ffmpeg.exe 复制到要处理的目录下

2. 双击 geshi.exe，根据提示输入执行


## 输入提示

```
将把当前目录下 mp3,flac,aac,mp4,mov,mkv,mpeg,avi,m4a 格式的文件转为 wav格式

你也可以修改 cfg.txt 里  source_ext  后的扩展名列表，改变需要被转换的格式
修改  target_ext  改变要转换到的格式


如果确认开始转换，请输入y
或者输入 待转换格式->转换到的格式
例如输入 avi->mp4  将把 avi 视频转换 mp4 视频:

```

