# 安装epel-release
```shell
# centos
yum install -y epel-release

# aws
amazon-linux-extras install -y epel

```

### 安装nginx与certbot
```shell
yum install -y nginx certbot

```

### 修改一下首页
```shell
cat >/usr/share/nginx/html/index.html <<EOF
<h1>certbot.mingjiao.org</h1>
EOF

```

### 打开NGINX服务
```shell
systemctl start nginx
systemctl enable nginx

```

### DNS解析(一定要确认解析成功)
### 域名certbot.mingjiao.org 到IP地址的A记录

### 申请证书
```shell
certbot certonly --webroot -w /usr/share/nginx/html -d certbot.mingjiao.org

```

### 互动内容记录
```shell
Saving debug log to /var/log/letsencrypt/letsencrypt.log
Plugins selected: Authenticator webroot, Installer None
Enter email address (used for urgent renewal and security notices)
 (Enter 'c' to cancel): collinsctk@dcloud.cisco.com

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Please read the Terms of Service at
https://letsencrypt.org/documents/LE-SA-v1.3-September-21-2022.pdf. You must
agree in order to register with the ACME server. Do you agree?
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
(Y)es/(N)o: Y

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Would you be willing, once your first certificate is successfully issued, to
share your email address with the Electronic Frontier Foundation, a founding
partner of the Let's Encrypt project and the non-profit organization that
develops Certbot? We'd like to send you email about our work encrypting the web,
EFF news, campaigns, and ways to support digital freedom.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
(Y)es/(N)o: Y
Account registered.
Requesting a certificate for certbot.mingjiao.org
Performing the following challenges:
http-01 challenge for certbot.mingjiao.org
Using the webroot path /usr/share/nginx/html for all unmatched domains.
Waiting for verification...
Cleaning up challenges
Subscribe to the EFF mailing list (email: collinsctk@dcloud.cisco.com).
We were unable to subscribe you the EFF mailing list because your e-mail address appears to be invalid. You can try again later by visiting https://act.eff.org.

IMPORTANT NOTES:
 - Congratulations! Your certificate and chain have been saved at:
   /etc/letsencrypt/live/certbot.mingjiao.org/fullchain.pem
   Your key file has been saved at:
   /etc/letsencrypt/live/certbot.mingjiao.org/privkey.pem
   Your certificate will expire on 2024-01-15. To obtain a new or
   tweaked version of this certificate in the future, simply run
   certbot again. To non-interactively renew *all* of your
   certificates, run "certbot renew"
 - If you like Certbot, please consider supporting our work by:

   Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
   Donating to EFF:                    https://eff.org/donate-le

```

### 修改nginx配置(nignx.conf)
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

### 创建目录并且把证书和私钥文件拷贝到nginx证书目录下
```shell
mkdir -p /etc/pki/nginx/private
chown -R nginx:nginx /etc/pki/nginx
cp /etc/letsencrypt/live/certbot.mingjiao.org/fullchain.pem /etc/pki/nginx/server.crt
cp /etc/letsencrypt/live/certbot.mingjiao.org/privkey.pem /etc/pki/nginx/private/server.key

```

### 产生dhparam.pem
```shell
openssl dhparam -out /etc/pki/nginx/dhparam.pem 2048

```

### dhparam.pem GPT4介绍
```text
dhparam.pem 文件是Diffie-Hellman（DH）参数文件。在SSL/TLS握手过程中，Diffie-Hellman算法用于实现完全前向保密（PFS）。
完全前向保密确保即使一个会话的密钥被捕获，之前的会话仍然是安全的，因为没有一个固定的私钥用于所有的会话。

详细地说，Diffie-Hellman密钥交换是一种允许两个通信实体生成一个共享的、随机的密钥，尽管他们之间的通信可能被监听。这种方法的优势是，
即使攻击者捕获了他们之间的所有通信，他们也不能确定共享的密钥是什么。

在使用Diffie-Hellman密钥交换的SSL/TLS中，服务器和客户端都需要一个DH参数。这些参数通常可以预先生成并存储在一个文件中，
如您提供的dhparam.pem。使用这些预先生成的参数可以加速握手过程。

为了增加安全性，推荐使用更长的DH参数，例如2048位或更长。这将增加计算的复杂性，但也会增加安全性。不过，生成长的DH参数可能需要很长时间。

总之，dhparam.pem文件存储了Diffie-Hellman参数，这些参数在SSL/TLS握手过程中用于实现完全前向保密。
```

### 再次修改nginx.conf
```shell
    server {
        listen       443 ssl http2;
        listen       [::]:443 ssl http2;
        server_name  _;
        root         /usr/share/nginx/html;

        ssl_certificate "/etc/pki/nginx/fullchain.pem";
        ssl_certificate_key "/etc/pki/nginx/privkey.pem";
        ssl_dhparam /etc/pki/nginx/dhparam.pem;  # 添加了dhparam
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

### 再次重启nginx
```shell
nginx -t
systemctl restart nginx

```