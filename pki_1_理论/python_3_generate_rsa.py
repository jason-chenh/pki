#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# pip install pycryptodome
from Crypto.PublicKey import RSA

# ----------------- 生成 RSA 密钥 -----------------
key = RSA.generate(2048)
# 私钥
private_key = key.export_key()
# 公钥
public_key = key.publickey().export_key()

# 保存密钥到文件
with open("./rsa_key/private.pem", "wb") as f:
    f.write(private_key)
with open("./rsa_key/public.pem", "wb") as f:
    f.write(public_key)
