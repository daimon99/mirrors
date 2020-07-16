# mirrors

自动镜像服务

可以自建一个镜像服务，使用这个镜像服务后，如果首次使用相应的包，会先从本地读取。本地没有的时候，再从源端读取。

现在支持：

* centos
* epel
* influx
* salt
* postgresql
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
