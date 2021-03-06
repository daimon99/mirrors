# coding: utf-8

import os
import requests
from bottle import route, static_file, run, redirect, abort
from pathlib import Path

base_dir = Path(__file__).resolve().parents[1] / 'www'


def download_resource(repo, url, mapping_url):
    """

    :param repo: 哪个镜像
    :param url: 要访问的镜像中的路径
    :param mapping_url: 完整的镜像路径
    :return:
    """
    from pathlib import Path
    p1 = base_dir / repo / Path(url)
    print('download resource', p1)
    p1.parent.mkdir(parents=True, exist_ok=True)
    ret = requests.get(mapping_url)
    if p1.suffix:
        p1.write_bytes(ret.content)
    else:
        # 没有后缀，说明是目录索引
        p1.mkdir(exist_ok=True)
        (p1 / 'index.html').write_bytes(ret.content)


def start_download(repo, url, mapping_url):
    import threading
    threading.Thread(target=download_resource, args=(repo, url, mapping_url)).start()


def mapping(repo, url):
    if repo == 'centos':
        return f'https://mirrors.aliyun.com/{url}'
    elif repo == 'influx':
        return f'https://repos.influxdata.com/{url}'
    elif repo == 'pg':
        return f'https://download.postgresql.org/{url}'
    elif repo == 'salt':
        return f'https://repo.saltstack.com/{url}'
    elif repo == 'pypi':
        return f'http://mirrors.cloud.tencent.com/{url}'
    elif repo == 'rpmfusion':
    	return f'http://download1.rpmfusion.org/{url}'
    else:
        abort(400, f'不支持的镜像类型，请检查您的配置文件: {repo}, {url}')
        raise NotImplementedError(f'不支持的镜像：{repo}, {url}')


@route('/<repo>/<url:path>', method='get')
def mirrors(repo, url):
    print('url: ', repo, url)
    if os.path.exists(os.path.join(base_dir, url)):
        print('exist, go cache.')
        return static_file(url, base_dir / repo)
    else:
        mapping_url = mapping(repo, url)
        if 'repodata' not in url:
            start_download(repo, url, mapping_url)
        return redirect(mapping_url)


if __name__ == '__main__':
    run(host='0.0.0.0', port='9093')
