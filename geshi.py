import os
import shutil
import subprocess
import sys
import re

if not shutil.which("ffmpeg"):
    print('当前系统未安装ffmpeg，请下载变将 ffmpeg.exe 放在当前目录下\n下载地址\nhttps://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.7z')
    input("按回车退出")
    sys.exit()

root = os.getcwd()
filepath=root
cfg = os.path.join(root, 'cfg.txt')
sext = ['mp3', 'flac', 'mp4', 'mpeg', 'aac', 'mkv', 'avi']
ext = 'wav'

if os.path.exists(cfg):
    with open(cfg, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            it = line.strip()
            if it:
                it = it.replace('，', ',').split('=')
                length=len(it)
                if length==2:
                    if it[0].lower() == 'source_ext':
                        sext = [x.lower().strip() for x in it[1].split(",")]
                    elif it[0].lower() == 'target_ext':
                        ext = it[1].lower().strip().split(',')[0].strip()
                    elif it[0]=='dir' and os.path.exists(it[1]) and os.path.isdir(it[1]):
                        filepath=it[1]
                        



print(f"""
将把当前目录下 {",".join(sext)} 格式的文件转为 {ext}格式

你也可以修改 cfg.txt 里  source_ext  后的扩展名列表，改变需要被转换的格式
修改  target_ext  改变要转换到的格式

""")

yes=input("如果确认开始转换，请输入y\n或者输入 待转换格式->转换到的格式\n例如输入 avi->mp4  将把 avi 视频转换 mp4 视频: ")
yes=yes.strip()
if not yes:
    sys.exit()
    
if len(yes)==1 and yes.lower() !='y':
    sys.exit()

if len(yes)>1:
    m=re.match(r'([a-zA-Z0-9]+)->([a-zA-Z0-9]+)',yes,re.I)
    if not m or len(m.groups())!=2:
        print('输入错误，如果想输入 旧格式转为新格式，请按照  avi->mp4 格式输入')
        sys.exit()
    m=m.groups()
    sext=m[0].lower()
    ext=m[1].lower()

files = []
for it in os.listdir(filepath):
    if it.split('.')[-1].lower() in sext:
        files.append(it)



if len(files) < 1:
    print(f'\n没有需要转换的文件')
else:
    ok = 0
    err = []

    for i,it in enumerate(files):
        try:
            cmd=['ffmpeg', "-hide_banner", "-ignore_unknown", '-y', '-i', os.path.normpath(os.path.join(filepath, it))             ]
            if ext.lower()=='mp4':
                cmd.extend(['-c:v','libx264','-c:a','aac'])
            cmd.append(os.path.normpath(os.path.join(filepath,f'{it}.{ext}')))
            print(f'\n[{i+1}]. 开始转换 {it}\n可能需要一些时间，结束后将有提示，请耐心等待\n')
            p=subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            if p.returncode!=0:
                input(str(p.stderr))                
                sys.exit()
            print(f'[OK] {it} 转换成功')            
            ok += 1
        except Exception as e:
            err.append(it)
            print(f'[Error] {it} 转换失败 {str(e)}')

    print(f"\n转换完毕，{ok} 个成功，{len(err)} 个失败,{err if len(err) > 0 else ''}\n")
input("\n按回车退出")
