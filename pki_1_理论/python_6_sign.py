#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# pip install pycryptodome

from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

# 加载私钥
private_key = RSA.import_key(open("./rsa_key/private.pem").read())

# 签名的明文消息 (需要二进制数据)
plain_text = b'Welcome to qytang.com!'

# 签名的密文消息 (需要二进制数据)
with open("./msg/aes_encrypted.data", "rb") as f:
    cipher_text = f.read()

# -------------------------数字签名使用私钥对HASH值进行加密-------------------------
# 先产生消息的哈希值 [数字签名就是对哈希值进行私钥加密]
plain_text_hash = SHA256.new(plain_text)
cipher_text_hash = SHA256.new(cipher_text)

# 然后数字签名 [数字签名就是对哈希值进行私钥加密]
plain_text_digital_signature = pkcs1_15.new(private_key).sign(plain_text_hash)
cipher_text_digital_signature = pkcs1_15.new(private_key).sign(cipher_text_hash)

# 打印签名
print("明文消息的数字签名:", plain_text_digital_signature)
print("秘闻消息的数字签名:", cipher_text_digital_signature)

# 保存签名
with open("./msg/plain_text.sig", "wb") as f:
    f.write(plain_text_digital_signature)

with open("./msg/cipher_text.sig", "wb") as f:
    f.write(cipher_text_digital_signature)


