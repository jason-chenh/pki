#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# pip install pycryptodome

from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

# 加载公钥
public_key = RSA.import_key(open("./rsa_key/public.pem").read())

# -------------------------------------校验明文消息的签名-------------------------------------

plain_text = b'Welcome to qytang.com!'

# 生成明文消息的散列值, 后续用于"对比散列值" [公钥解密数字签名, 再比对散列值, 完成对数字签名的校验]
plain_text_hash = SHA256.new(plain_text)

# 验证签名
try:
    # 读取明文的数字签名
    with open("./msg/plain_text.sig", "rb") as f:
        plain_text_digital_signature = f.read()
    # 使用公钥解密数字签名, 并与散列值进行比对
    pkcs1_15.new(public_key).verify(plain_text_hash, plain_text_digital_signature)
    print("明文的数字签名是合法的.")
except (ValueError, TypeError):
    print("明文的数字签名是非法的.")


# -------------------------------------校验密文消息的签名-------------------------------------
with open("./msg/aes_encrypted.data", "rb") as f:
    cipher_text = f.read()

# 生成密文消息的散列值, 后续用于"对比散列值" [公钥解密数字签名, 再比对散列值, 完成对数字签名的校验]
cipher_text_hash = SHA256.new(cipher_text)

# 验证签名
try:
    # 读取密文的数字签名
    with open("./msg/cipher_text.sig", "rb") as f:
        cipher_text_digital_signature = f.read()
    # 使用公钥解密数字签名, 并与散列值进行比对
    pkcs1_15.new(public_key).verify(cipher_text_hash, cipher_text_digital_signature)
    print("密文的数字签名是合法的.")
except (ValueError, TypeError):
    print("密文的数字签名是非法的.")

