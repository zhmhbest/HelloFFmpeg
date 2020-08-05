from .ff import ffplay, ffprobe, ffmpeg


def ff_play(src, title='', shape=None, loop=0):
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


def ff_msg_video(src):
    """
    查看视频的视频信息
    :param src:
    :return:
    """
    ffprobe(['-v', 'quiet', '-show_streams', '-select_streams', 'v', '-i', src])


def ff_msg_audio(src):
    """
    查看视频的音频信息
    :param src:
    :return:
    """
    ffprobe(['-v', 'quiet', '-show_streams', '-select_streams', 'a', '-i', src])


def ff_detach(src, path_to_video=None, path_to_audio=None):
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


def ff_pack(src_video, src_audio, path_to_save):
    """
    合并视频和音频
    :param src_video:
    :param src_audio:
    :param path_to_save:
    :return:
    """
    ffmpeg(['-i', src_video, '-i', src_audio, '-vcodec', 'copy', '-acodec', 'copy', path_to_save])
