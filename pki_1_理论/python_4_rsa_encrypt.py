#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# pip install pycryptodome

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# 加载公钥
public_key = RSA.import_key(open("./rsa_key/public.pem").read())

# 创建 cipher 对象
cipher = PKCS1_OAEP.new(public_key)

# 加密消息
message = b'Welcome to qytang.com!'
encrypted_message = cipher.encrypt(message)
print("加密的消息:", encrypted_message)

# 保存加密消息
with open("./msg/private.msg", "wb") as f:
    f.write(encrypted_message)

