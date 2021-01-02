from moviepy.editor import AudioFileClip
import sys
from you_get import common as you_get       #导入you-get库
import time

directory = r'E:\workspace\python\demo\src'                         #设置下载目录
name = str(time.time())     #获取当前时间戳命名
url = 'https://www.bilibili.com/bangumi/play/ss35874'      #需要下载的视频地址
sys.argv = ['you-get','-o',directory,'-O',name,url]       #sys传递参数执行下载，就像在命令行一样
you_get.main()

video = AudioFileClip('E:\\workspace\\python\demo\\src\\'+name+'.flv')   #读取视频
audio = video.write_audiofile('E:\\workspace\\python\demo\\src\\'+name+'.wav')      #将视频中的音频提取出来
