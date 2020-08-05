import os
from urllib import request, response
from hashlib import sha256

USER_AGENT = ' '.join([
    "Mozilla/5.0", "(Windows NT 10.0; Win64; x64)",
    "AppleWebKit/537.36", "(KHTML, like Gecko)",
    "Chrome/84.0.4147.105", "Safari/537.36"
])


def __progress_bar(rate, length=32, single_char1='=', single_char2='.'):
    num_part_l = int((rate + 0.0001) * length)
    num_part_r = length - num_part_l
    str_l = single_char1 * num_part_l
    str_r = single_char2 * num_part_r
    print(f"\r[{str_l}>{str_r}] %.2f%%" % (rate * 100), end='', flush=True)


def download_one_file(url, local):
    # 文件存在且校验通过
    if os.path.exists(local) and os.path.exists(f'{local}.ok'):
        with open(local, 'rb') as f:
            hexdigest = sha256(f.read()).hexdigest()
        with open(f'{local}.ok', 'r') as f_ok:
            hexdigest_test = f_ok.read()
        if hexdigest == hexdigest_test:
            return True

    with request.urlopen(request.Request(
            url=url,
            headers={
                'User-Agent': USER_AGENT
            }
    )) as one_response:
        if 200 == one_response.status:
            print('Downloading...')
            print(f"\turl : {url}")
            print(f"\tto  : {local}")
            print("Please do not disturb the process!")
            headers = dict(one_response.getheaders())
            chunk_size = 1024
            content_size = int(headers['Content-Length'])
            loop_count = (content_size // chunk_size) + 1
            with open(local, 'wb') as f:
                for i in range(loop_count):
                    f.write(one_response.read(chunk_size))
                    __progress_bar(i/loop_count)
            with open(f'{local}.ok', 'w') as f_ok:
                with open(local, 'rb') as f:
                    hexdigest = sha256(f.read()).hexdigest()
                f_ok.write(hexdigest)
            return True
        else:
            print(one_response.reason)
    return False
