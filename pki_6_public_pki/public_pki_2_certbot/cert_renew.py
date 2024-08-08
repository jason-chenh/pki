#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# pip3 install pyOpenSSL
from datetime import datetime, timedelta
import os
from OpenSSL import crypto as c

cert = c.load_certificate(c.FILETYPE_PEM, open('/etc/letsencrypt/live/chatbot.mingjiao.org/fullchain.pem').read())
cert_datetime = datetime.strptime(cert.get_notAfter().decode("utf-8"), "%Y%m%d%H%M%SZ")
if timedelta(days=30) > (cert_datetime - datetime.now()):
    # if os.system('/usr/bin/certbot renew') == 0:
    if os.system('/usr/bin/certbot renew --dry-run') == 0:
        print("命令执行成功")
    else:
        print("命令执行失败")
