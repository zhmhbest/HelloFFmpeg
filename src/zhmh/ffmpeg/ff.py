"""
    ffmpeg: http://www.ffmpeg.org/download.html
    ffmpeg windows build: https://ffmpeg.zeranoe.com/builds/
"""

import os
import subprocess


def __get_version_location(version):
    import platform
    # from zhmh.download import download_one_file, unpack_one_file
    # pip install python-zhmh -i https://pypi.org/simple
    from pyzhmh import download_one_file, unpack_one_file
    __architecture = platform.architecture()
    if 'WindowsPE' != __architecture[1]:  # 仅支持Windows系统
        raise Exception("Windows platform only!")
    current_directory = os.path.abspath(os.path.dirname(__file__))
    ffmpeg_directory = os.path.join(current_directory, 'execute')
    bit = 'win64' if '64bit' == __architecture[0] else 'win32'
    final_directory = os.path.join(ffmpeg_directory, f"ffmpeg-{version}-{bit}-shared", 'bin')
    if not os.path.exists(final_directory):
        ffmpeg_builds_zip = \
            os.path.join(current_directory, f"ffmpeg-{version}-{bit}-shared.zip")
        ffmpeg_builds_url = \
            f"https://ffmpeg.zeranoe.com/builds/{bit}/shared/ffmpeg-{version}-{bit}-shared.zip"
        if download_one_file(ffmpeg_builds_zip, {'url': ffmpeg_builds_url}):
            unpack_one_file(ffmpeg_builds_zip, ffmpeg_directory)
        else:
            raise Exception(f"Can not find ffmpeg@{version}.")
    return final_directory


def __get_check_bin(final_directory):
    bin_ffmpeg = os.path.join(final_directory, 'ffmpeg.exe')
    bin_ffplay = os.path.join(final_directory, 'ffplay.exe')
    bin_ffprobe = os.path.join(final_directory, 'ffprobe.exe')
    if not os.path.exists(bin_ffmpeg):
        raise Exception("Can not find ffmpeg.exe.")
    if not os.path.exists(bin_ffplay):
        raise Exception("Can not find ffplay.exe.")
    if not os.path.exists(bin_ffprobe):
        raise Exception("Can not find ffprobe.exe.")
    return bin_ffmpeg, bin_ffplay, bin_ffprobe


FFMPEG_VERSION = '4.3.1'
FFMPEG_PATH = __get_version_location(FFMPEG_VERSION)
FFMPEG_bin_ffmpeg, FFMPEG_bin_ffplay, FFMPEG_bin_ffprobe = __get_check_bin(FFMPEG_PATH)


def ffmpeg(cmd: list):
    cmd.insert(0, FFMPEG_bin_ffmpeg)
    subprocess.run(cmd)


def ffplay(cmd: list):
    cmd.insert(0, FFMPEG_bin_ffplay)
    subprocess.run(cmd)


def ffprobe(cmd: list):
    cmd.insert(0, FFMPEG_bin_ffprobe)
    subprocess.run(cmd)
