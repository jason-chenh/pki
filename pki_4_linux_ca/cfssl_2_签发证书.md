### NGINX证书请求文件(/pki2023/pki_4_linux_ca/linux_ca/cfssl_json/nginx-server-csr.json)
```json
{
    "CN": "nginix.dcloud.cisco.com",
    "hosts": [
        "198.18.133.100",
        "nginix.dcloud.cisco.com"
    ],
    "key": {
        "algo": "rsa",
        "size": 2048
    },
    "names": [
        {
            "C": "CN",
            "ST": "guangzhou",
            "L": "guangzhou",
            "O": "dcloud",
            "OU": "dcloudgz"
        }
    ]
}
```

# 进入目录签发NGINX证书
```shell script
[root@elasticsearch cfssl_json]# pwd
/pki2023/pki_4_linux_ca/linux_ca/cfssl_json

[root@elasticsearch cfssl_json]# ls -an
~~~~忽略其他~~~~
-rw-r--r--. 1 0 0      387 Oct 24 22:09 nginx-server-csr.json


cfssl gencert -ca=../cfssl_certs_and_keys/ca.pem -ca-key=../cfssl_certs_and_keys/ca-key.pem \
  -config=ca-config.json -profile=server \
  nginx-server-csr.json |cfssl-json -bare ../cfssl_certs_and_keys/nginx-server
  
根证书,根证书的密钥,profile,模板用哪个,请求的json在哪里,产生的目录以nginx-server开头

[root@elasticsearch cfssl_certs_and_keys]# pwd
/pki2023/pki_4_linux_ca/linux_ca/cfssl_certs_and_keys

[root@elasticsearch cfssl_certs_and_keys]# ls -an

~~~忽略其他~~~
-rw-------. 1 0 0     1679 Oct 24 22:12 nginx-server-key.pem  # 秘钥
-rw-r--r--. 1 0 0     1773 Oct 24 22:12 nginx-server.pem      # 证书

```