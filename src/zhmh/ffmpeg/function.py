from .ff import ffplay, ffprobe, ffmpeg


def ff_play(src: str, title='', shape=None, loop=0):
    """
    播放视频
    :param src:
    :param title:
    :param shape:
    :param loop:
    :return:
    """
    if shape is None:
        ffplay([src, '-window_title', title, '-loop', str(loop)])
    else:
        ffplay([src, '-x', str(shape[0]), '-y', str(shape[1]), '-window_title', title, '-loop', str(loop)])


def ff_msg_video(src: str):
    """
    查看视频的视频信息
    :param src:
    :return:
    """
    ffprobe(['-v', 'quiet', '-show_streams', '-select_streams', 'v', '-i', src])


def ff_msg_audio(src: str):
    """
    查看视频的音频信息
    :param src:
    :return:
    """
    ffprobe(['-v', 'quiet', '-show_streams', '-select_streams', 'a', '-i', src])


def ff_detach(src: str, path_to_video=None, path_to_audio=None):
    """
    分离视频和音频
    :param src: 视频文件
    :param path_to_video: 导出视频位置
    :param path_to_audio: 导出音频位置
    :return:
    """
    if path_to_video is not None:
        # 分离出视频
        ffmpeg(['-i', src, '-vcodec', 'copy', '-an', f'{path_to_video}.264'])
    if path_to_audio is not None:
        # 分离出音频
        ffmpeg(['-i', src, '-vcodec', 'copy', '-vn', f'{path_to_audio}.aac'])


def ff_repack(srcs: str or [str, ...], path_to_save: str):
    """
    重新封装视频 或 合并视频和音频
    :param srcs:
    :param path_to_save:
    :return:
    """
    cmd = []
    if isinstance(srcs, list):
        for src in srcs:
            cmd.append('-i')
            cmd.append(src)
    else:
        cmd.append('-i')
        cmd.append(srcs)
    cmd.extend(['-vcodec', 'copy', '-acodec', 'copy', path_to_save])
    ffmpeg(cmd)


def ff_key_cut(src: str, start_time, duration_or_end_time, output: str):
    """
    关键帧裁剪视频
    但会造成几秒的误差，只能落在关键帧上
    :param src:
    :param start_time:
    :param duration_or_end_time:
    :param output:
    :return:
    """
    ffmpeg([
        '-i', src,
        '-ss', start_time,
        '-to' if isinstance(duration_or_end_time, str) else '-t', str(duration_or_end_time),
        # '-vcodec', 'copy', '-acodec', 'copy',
        '-codec', 'copy',
        output, '-y'
    ])


def ff_cut(src: str, start_time, duration_or_end_time, output: str):
    """
    精准裁剪
    :param src:
    :param start_time:
    :param duration_or_end_time:
    :param output:
    :return:
    """
    ffmpeg([
        '-ss', start_time,
        '-to' if isinstance(duration_or_end_time, str) else '-t', str(duration_or_end_time),
        '-accurate_seek',
        '-i', src,
        # '-vcodec', 'copy', '-acodec', 'copy',
        '-codec', 'copy',
        '-avoid_negative_ts', '1',
        output, '-y'
    ])


def ff_combine(src_list: list, output: str):
    """
    合并多个视频
    :param src_list:
    :param output:
    :return:
    """
    import random
    import os
    dump_list_file = os.path.abspath(f"{output}.{random.random()}.dump_list.txt")
    with open(dump_list_file, 'w') as fp:
        for item in src_list:
            item = os.path.abspath(item).replace('\\', '/')
            fp.write(f"file {item}\n")
    ffmpeg([
        '-f', 'concat',
        '-safe', '0',
        '-i', dump_list_file,
        '-codec', 'copy',
        '-y', output
    ])
    os.remove(dump_list_file)


def ff_encode_audio(
        src_audio: str, output: str, to_format: str,
        acodec: str = None,
        brc: (int, int, int) = None
):
    """
    编码Audio为MP3
    :param src_audio: 音频文件
    :param output:
    :param to_format: 编码为, eg: mp3、ogg、wave、flac
    :param acodec: 编码, eg: copy、pcm_s24le、libmp3lame
    :param brc: (ab, ar, ac)
        ab: 码率, eg: 128
        ar: 采样率, eg: 16
        ac: 声道, eg: 2
    :return:
    """
    cmd = ['-i', src_audio]
    # 设置编码器
    if acodec is not None:
        cmd.extend(['-acodec', acodec])
    # 设置码率
    if brc is not None and 3 == len(brc):
        cmd.extend([
            '-ab', f'{str(brc[0])}k',
            '-ar', f'{str(brc[1])}k',
            '-ac', str(brc[2]),
        ])
    # 设置格式
    cmd.extend(['-f', to_format, '-y', output])
    ffmpeg(cmd)


def ff_encode_video_crf(
        src_video: str, output: str, crf: int
):
    """
    编码视频ByCRF
    :param src_video:
    :param output:
    :param crf: Constant Rate Factor{0 ~ 51}, advance{18 ~ 28}, 越大越差
    :return:
    """
    cmd = ['-i', src_video, '-vcodec', 'libx264', '-acodec', 'copy']
    cmd.extend(['-crf', str(crf)])
    cmd.extend(['-f', 'mp4', '-y', output])
    ffmpeg(cmd)


def ff_encode_video_2pass(
        src_video: str, output: str,
        vb: int
):
    cmd = ['-i', src_video, '-vcodec', 'libx264', '-vb', f'{vb}k']
    cmd1 = cmd.copy()
    cmd1.extend(['-an', '-pass', '1', '-f', 'mp4', '-y', 'NUL'])
    ffmpeg(cmd1)
    cmd2 = cmd.copy()
    cmd2.extend(['-acodec', 'copy', '-pass', '2', '-f', 'mp4', '-y', output])
    ffmpeg(cmd2)
