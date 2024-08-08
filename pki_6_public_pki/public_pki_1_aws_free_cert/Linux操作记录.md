# 安装epel-release
```shell
# centos
yum install -y epel-release

# aws
amazon-linux-extras install -y epel
```

### 安装nginx
```shell
yum install -y nginx

```

### 修改一下首页
```shell
cat >/usr/share/nginx/html/index.html <<EOF
<h1>certbot.dcloud.cisco.com</h1>
EOF

```

### 打开NGINX服务
```shell
systemctl start nginx
systemctl enable nginx

```

### DNS解析(一定要确认解析成功)
### 域名chatbot.dcloud.cisco.com 到IP地址的A记录


### 把申请到的证书和秘钥放入文件
```shell
mkdir -p /etc/pki/nginx/private
chown -R nginx:nginx /etc/pki/nginx
vim /etc/pki/nginx/server.crt
vim /etc/pki/nginx/private/server.key
```

### 取消/etc/nginx/nginx.conf下面部分的注释
```shell
    server {
        listen       443 ssl http2;
        listen       [::]:443 ssl http2;
        server_name  _;
        root         /usr/share/nginx/html;

        ssl_certificate "/etc/pki/nginx/server.crt";
        ssl_certificate_key "/etc/pki/nginx/private/server.key";
        ssl_session_cache shared:SSL:1m;
        ssl_session_timeout  10m;
        ssl_ciphers HIGH:!aNULL:!MD5;
        ssl_prefer_server_ciphers on;

        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;

        error_page 404 /404.html;
            location = /40x.html {
        }

        error_page 500 502 503 504 /50x.html;
            location = /50x.html {
        }
    }

```

### 重启NGINX
```shell
[root@ip-10-1-1-217 certs]# nginx -t
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful

[root@ip-10-1-1-217 certs]# systemctl restart nginx

```