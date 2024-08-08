### 明文秘钥与证书, 封装到p12格式
```shell
[root@elasticsearch cfssl_certs_and_keys]# pwd
/pki2023/pki_4_linux_ca/linux_ca/cfssl_certs_and_keys

[root@elasticsearch cfssl_certs_and_keys]# ls -an
~~~忽略其他~~~
-rw-------. 1 0 0     1679 Oct 24 22:12 nginx-server-key.pem  # 秘钥
-rw-r--r--. 1 0 0     1773 Oct 24 22:12 nginx-server.pem      # 证书

[root@elasticsearch cfssl_certs_and_keys]# openssl pkcs12 -export -out nginx-server.p12 -inkey nginx-server-key.pem -in nginx-server.pem
Enter Export Password: Cisc0123
Verifying - Enter Export Password: Cisc0123

# -export: 此选项指示openssl创建PKCS#12文件。
# -out nginx-server.p12: 此选项指定输出文件的名称和位置。
# -inkey nginx-server-key.pem: 此选项指定包含私钥的文件。
# -in nginx-server.pem: 此选项指定包含证书的文件。

[root@elasticsearch cfssl_certs_and_keys]# ls -an

-rw-------. 1 0 0     1679 Oct 24 22:12 nginx-server-key.pem
-rw-------. 1 0 0     3011 Oct 24 22:16 nginx-server.p12      # 产生的P12文件
-rw-r--r--. 1 0 0     1773 Oct 24 22:12 nginx-server.pem

```