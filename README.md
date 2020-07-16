# mirrors

自动镜像服务

可以自建一个镜像服务，使用这个镜像服务后，使用相应的包，会先从本地读取。本地没有的时候，再从源端读取。

现在支持：

* centos
* epel
* influx yum 源
* salt yum 源
* postgresql yum 源
* pypi

# 依赖

* nginx
* python3.6 及以上

# 使用

1. nginx 配置

参考 deploy/nginx 中的配置，加入 mirrors 站点

2. 启动服务

```
cd <mirrors path>
mkdir www
python src/run.py
```

镜像文件，按源类型，自动存放在 www/<repo>/<url> 目录下。

# 镜像配置

## yum 源

yum.repos.d 源文件中的domain 部分，替换为：

* centos && epel : https://mirrors.daimon.cc/centos
* influx: https://mirrors.daimon.cc/influx
* salt: https://mirrors.daimon.cc/salt
* pg: https://mirrors.daimon.cc/pg

## pypi 源

~/.pip/pip.conf 或 /etc/pip.conf 域名部分替换为：https://mirrors.daimon.cc/pypi

参考配置

```
[global]
index-url=https://mirrors.daimon.cc/pypi/pypi/simple
trusted-host=
    mirrors.daimon.cc
```
