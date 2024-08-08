#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# pip install pycryptodome

from Crypto.Hash import SHA256


# 需要HASH的消息(需要二进制数据)
plain_text = b'Welcome to qytang.com!'

# 生成消息的哈希值
plain_text_hash = SHA256.new(plain_text)

print("明文消息的哈希值:", plain_text_hash.digest())            # 二进制
print("明文消息的哈希值(16进制):", plain_text_hash.hexdigest())  # 字符串

with open("./msg/plain.hash", "wb") as f:
    f.write(plain_text_hash.digest())  # 写入的是二进制数据

