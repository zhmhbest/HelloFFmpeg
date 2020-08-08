# -*- coding: utf-8 -*-
from zhmh.ffmpeg import *


DRIVE = 'E'
video1 = DRIVE + ":\\Downloads\\BBoom.mp4"
output = DRIVE + ":\\Downloads\\"


if __name__ == '__main__':
    ff_msg_audio(video1)
    ff_play(video1, shape=(640, 480))

    # 【重新封装视频】
    ff_repack(video1, output + 'BBoom2.flv')

    # 【分离合并视音频】
    ff_detach(video1, output + '1', output + '2')
    ff_repack([output + '1.264', output + '2.aac'], output + '3.mp4')

    # 【裁剪视频】
    ff_cut(video1, '00:00:10', '00:00:15', output + 'cut3.mp4')
    ff_cut(video1, '00:00:00', 10, output + 'cut4.mp4')

    # 【合并视频】
    ff_combine([output + 'cut3.mp4', output + 'cut4.mp4'], output + 'combine.mp4')

    # 【编码音频】
    ff_encode_audio(output + '2.aac', output + '2.ogg', to_format='ogg')
    ff_encode_audio(output + '2.aac', output + '2.wav', to_format='wav')
    ff_encode_audio(output + '2.aac', output + '2.flac', to_format='flac')

    # 【编码视频】
    ff_encode_video_crf(video1, output + 'en1.mp4', 28)
    ff_encode_video_2pass(video1, output + 'en2.mp4', 1200)
