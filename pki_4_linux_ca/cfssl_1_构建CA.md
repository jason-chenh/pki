### CFSSL介绍
https://blog.51cto.com/liuzhengwei521/2120535

项目地址：https://github.com/cloudflare/cfssl

下载地址：https://pkg.cfssl.org/

参考链接：https://blog.cloudflare.com/how-to-build-your-own-public-key-infrastructure/

### 配置CFSSL
```shell
[root@elasticsearch cfssl_tools]# pwd
/pki2023/pki_4_linux_ca/linux_ca/cfssl_tools

[root@elasticsearch cfssl_tools]# ls
cfssl  cfssl-certinfo  cfssl-json

cp linux_ca/cfssl_tools/cfssl /usr/bin/cfssl
cp linux_ca/cfssl_tools/cfssl-json /usr/bin/cfssl-json
cp linux_ca/cfssl_tools/cfssl-certinfo /usr/bin/cfssl-certinfo
chmod +x /usr/bin/cfssl*

```
### 根证书初始化文件(20年有效期) (ca-csr.json)
```json
{
    "CN": "dcloudca",
    "hosts": [
    ],
    "key": {
        "algo": "rsa",
        "size": 4096
    },
    "names": [
        {
            "C": "CN",
            "ST": "guangzhou",
            "L": "guangzhou",
            "O": "dcloud"
        }
    ],
    "ca": {
        "expiry": "175200h"
    }
}

```
### 构建根证书
```shell
[root@elasticsearch cfssl_json]# pwd
/pki2023/pki_4_linux_ca/linux_ca/cfssl_json

[root@elasticsearch cfssl_json]# ls -an
~~~忽略其他~~~
-rw-r--r-- 1 0 0  321 Oct 30 09:31 ca-csr.json

[root@elasticsearch cfssl_json]# cfssl gencert -initca ca-csr.json | cfssl-json -bare ../cfssl_certs_and_keys/ca
2023/10/30 07:48:36 [INFO] generating a new CA key and certificate from CSR
2023/10/30 07:48:36 [INFO] generate received request
2023/10/30 07:48:36 [INFO] received CSR
2023/10/30 07:48:36 [INFO] generating key: rsa-4096
2023/10/30 07:48:43 [INFO] encoded CSR
2023/10/30 07:48:43 [INFO] signed certificate with serial number 523308930390981176133097293035172718197177455916

[root@elasticsearch cfssl_certs_and_keys]# pwd
/pki2023/pki_4_linux_ca/linux_ca/cfssl_certs_and_keys

[root@elasticsearch cfssl_certs_and_keys]# ls -an

~~~~忽略其他~~~~
-rw-r--r--. 1 0 0     1667 Oct 24 21:38 ca.csr      # 证书请求
-rw-------. 1 0 0     3243 Oct 24 21:38 ca-key.pem  # 根秘钥
-rw-r--r--. 1 0 0     2000 Oct 24 21:38 ca.pem      # 根证书

```

### 查看证书信息(dnsca)
```shell
cfssl-certinfo -cert ca.pem

```

## 配置证书模板 (ca-config.json)
### 相当于微软的证书模板 server auth
### server 服务器证书 client auth
### client 客户证书 server auth and client auth
### peer   既扮演服务器, 也扮演客户, 例如:ETCD的节点

```json
{
    "signing": {
        "default": {
            "expiry": "87600h"
        },
        "profiles": {
            "server": {
                "expiry": "175200h",
                "usages": [
                    "signing",
                    "key encipherment",
                    "server auth"
                ],
                "crl_url": "http://ad-2016.dcloud.cisco.com//CertEnroll/PKI2024-2016-CA.crl"
            },
            "client": {
                "expiry": "87600h",
                "usages": [
                    "signing",
                    "key encipherment",
                    "client auth"
                ],
                "crl_url": "http://ad-2016.dcloud.cisco.com//CertEnroll/PKI2024-2016-CA.crl"
            },
            "peer": {
                "expiry": "87600h",
                "usages": [
                    "signing",
                    "key encipherment",
                    "server auth",
                    "client auth"
                ],
                "crl_url": "http://ad-2016.dcloud.cisco.com//CertEnroll/PKI2024-2016-CA.crl"
            }
        }
    }
}

```
