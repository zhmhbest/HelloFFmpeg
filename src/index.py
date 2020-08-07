# -*- coding: utf-8 -*-
from zhmh.ffmpeg import *


DRIVE = 'E'
video_yn1 = DRIVE + ":\\Downloads\\G15\\YN010044.MP4"
video_yn2 = DRIVE + ":\\Downloads\\G15\\YN020044.MP4"
output = DRIVE + ":\\Downloads\\"


if __name__ == '__main__':
    ff_combine([video_yn1, video_yn2], output + 'YN.mp4')
    ff_encode_video_2pass(output + 'YN.mp4', output + 'YN_2pass.mp4', 1200)
    print('Finished')
