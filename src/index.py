# -*- coding: utf-8 -*-
from zhmh.ffmpeg import *
DRIVE = 'D'

video1 = DRIVE + r":\Downloads\【Nancy】MOMOLAND -' BBoom BBoom' - 1.【Nancy】MOMOLAND -' BBoom BBoom'(Av27950104,P1).mp4"
video2 = DRIVE + r":\Downloads\琴弦上.mp4"
output = DRIVE + r":\Downloads\\"

# ff_msg_audio(video1)
ff_play(video1, shape=(640, 480))

# # 【分离合并视音频】
# ff_detach(video1, output + '1', output + '2')
# ff_pack(output + '1.264', output + '2.aac', output + '3.mp4')

# 【裁剪视频】
# ff_key_cut(video1, '00:00:00', '00:00:15', output + 'cut1.mp4')
# ff_key_cut(video1, '00:00:10', 10, output + 'cut2.mp4')
# ff_cut(video1, '00:00:10', '00:00:15', output + 'cut3.mp4')
# ff_cut(video1, '00:00:00', 10, output + 'cut4.mp4')

# 【合并视频】
# ff_combine([output + 'cut3.mp4', output + 'cut4.mp4'], output + 'combine.mp4')
