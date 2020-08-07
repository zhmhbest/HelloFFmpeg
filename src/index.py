# -*- coding: utf-8 -*-
from zhmh.ffmpeg import *


DRIVE = 'E'
video_yn1 = DRIVE + ":\\Downloads\\G15\\YN010044.MP4"
video_yn2 = DRIVE + ":\\Downloads\\G15\\YN020044.MP4"
output = DRIVE + ":\\Downloads\\"


if __name__ == '__main__':
    input_list = [video_yn1, video_yn2]  # 此处可以传递多个视频地址
    ff_combine(input_list, output + 'YN.mp4')

    # vb表示比特率，比特率与视频质量和视频大小呈正相关
    ff_encode_video_2pass(output + 'YN.mp4', output + 'YN_2pass.mp4', vb=1200)
    print('Finished')
