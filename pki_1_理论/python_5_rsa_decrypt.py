#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# pip install pycryptodome

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# 加载私钥
private_key = RSA.import_key(open("./rsa_key/private.pem").read())

# 创建 cipher 对象
cipher = PKCS1_OAEP.new(private_key)

# 读取加密消息
with open("./msg/private.msg", "rb") as f:
    encrypted_message = f.read()
    decrypted_message = cipher.decrypt(encrypted_message)
    print("解密的消息:", decrypted_message.decode())

