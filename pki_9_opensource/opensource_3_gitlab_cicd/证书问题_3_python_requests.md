### 问题: Python requests模块无法请求WEB服务器(企业内部证书)

### 找到requests证书信任文件
```shell
[root@654867127bbb qytang]# python3.11
>>> import certifi
>>> certifi.where()
'/usr/local/lib/python3.11/site-packages/certifi/cacert.pem'

```

### 把企业根证书写入到"certifi.where()"
### Dockerfile已经自动解决了
```shell
cat /qytang/ms-root.cer >> /usr/local/lib/python3.11/site-packages/certifi/cacert.pem

```
