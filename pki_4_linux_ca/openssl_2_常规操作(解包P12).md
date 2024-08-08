### 从P12文件中提取明文证书
```shell
openssl pkcs12 -in nginx-server.p12 -nokeys -out nginx-srv-certificate.pem

```

### 从P12文件中提取明文私钥
```shell
openssl pkcs12 -in nginx-server.p12 -nocerts -nodes -out nginx-srv-key.pem

```

### 为后续实验的微软通配符证书拆包P12文件, 提取明文证书
```shell
openssl pkcs12 -in ms-star.dcloud.cisco.pfx -nokeys -out ms-star.dcloud.cisco.com-cert.pem

```

### 为后续实验的微软通配符证书拆包P12文件, 提取明文私钥
```shell
openssl pkcs12 -in ms-star.dcloud.cisco.pfx -nocerts -nodes -out ms-star.dcloud.cisco.com-key.pem

```
