FROM rockylinux:9.1.20230215
#定义启动jenkins的用户
USER root

# 安装必要工具
RUN yum install -y net-tools python3.11 python3.11-devel python3.11-pip

# 安装Python模块
RUN pip3.11 install -i https://pypi.douban.com/simple/ requests

# 切换到工作目录
WORKDIR /qytang

# 拷贝Python测试文件
COPY ./pressure_test_async.py /qytang/pressure_test_async.py
COPY ./ms-root.cer /qytang/ms-root.cer

# [root@654867127bbb qytang]# python3.11
# >>> import certifi
# >>> certifi.where()
# '/usr/local/lib/python3.11/site-packages/certifi/cacert.pem'

# 把企业根证书写入到"certifi.where()"
RUN cat /qytang/ms-root.cer >> /usr/local/lib/python3.11/site-packages/certifi/cacert.pem

CMD python3.11 /qytang/pressure_test_async.py

### Build的镜像名称为"collinsctk/pki2023_test" (已经push!!!)