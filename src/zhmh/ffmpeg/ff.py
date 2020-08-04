"""
    ffmpeg: http://www.ffmpeg.org/download.html
    ffmpeg windows build: https://ffmpeg.zeranoe.com/builds/
    - 4.3.1
      - x86: https://ffmpeg.zeranoe.com/builds/win32/shared/ffmpeg-4.3.1-win32-shared.zip
      - x64: https://ffmpeg.zeranoe.com/builds/win64/shared/ffmpeg-4.3.1-win64-shared.zip
"""
import platform
import os
import subprocess


__architecture = platform.architecture()
if 'WindowsPE' != __architecture[1]:
    raise Exception('Windows platform only!')
FFMPEG_VERSION = '4.1'
if '64bit' == __architecture[0]:
    FFMPEG_PATH = os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), FFMPEG_VERSION), 'x64'))
else:
    FFMPEG_PATH = os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), FFMPEG_VERSION), 'x86'))
FFMPEG_bin_ffmpeg = os.path.join(FFMPEG_PATH, 'ffmpeg.exe')
FFMPEG_bin_ffplay = os.path.join(FFMPEG_PATH, 'ffplay.exe')
FFMPEG_bin_ffprobe = os.path.join(FFMPEG_PATH, 'ffprobe.exe')
if not os.path.exists(FFMPEG_bin_ffmpeg):
    raise Exception('Can not find ffmpeg!')
if not os.path.exists(FFMPEG_bin_ffplay):
    raise Exception('Can not find ffplay!')
if not os.path.exists(FFMPEG_bin_ffprobe):
    raise Exception('Can not find ffprobe!')


def ffmpeg(cmd: list):
    cmd.insert(0, FFMPEG_bin_ffmpeg)
    subprocess.run(cmd)


def ffplay(cmd: list):
    cmd.insert(0, FFMPEG_bin_ffplay)
    subprocess.run(cmd)


def ffprobe(cmd: list):
    cmd.insert(0, FFMPEG_bin_ffprobe)
    subprocess.run(cmd)
