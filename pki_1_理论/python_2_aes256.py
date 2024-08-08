#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# pip install pycryptodome

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


def aes_encrypt(plain_text, key):
    # 生成随机初始化向量(IV)
    iv = get_random_bytes(16)
    # 创建cipher对象
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # 填充明文，使其长度为块大小的整数倍 [先填充, 后加密]
    padded_data = pad(plain_text.encode('utf-8'),  # encode()将字符串转换为字节
                      AES.block_size)
    # 加密 [先填充, 后加密]
    encrypted_data = cipher.encrypt(padded_data)
    return iv + encrypted_data  # 返回IV和加密后的数据


def aes_decrypt(encrypted_data, key):
    # 提取IV和加密后的数据
    iv, enc_data = encrypted_data[:16], encrypted_data[16:]
    # 创建cipher对象
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # 解密 [先解密, 再去除填充]
    decrypted_data = cipher.decrypt(enc_data)
    # 去除填充 [先解密, 再去除填充]
    plain_text = unpad(decrypted_data, AES.block_size).decode('utf-8')  # decode()将字节转换为字符串
    return plain_text


# 生成256位(32个字节)随机密钥
key = get_random_bytes(32)

# 保存秘钥到文件
with open("./msg/aes.key", "wb") as f:
    f.write(key)

# 待加密的明文
plain_text = 'Hello, World!'

# 加密
encrypted_data = aes_encrypt(plain_text, key)
print(f'Encrypted: {encrypted_data.hex()}')

# 保存加密后的数据到文件
with open("./msg/aes_encrypted.data", "wb") as f:
    f.write(encrypted_data)

# 读取保存的秘钥
with open("./msg/aes.key", "rb") as f:
    read_aes_key = f.read()

# 读取保存的加密后的数据
with open("./msg/aes_encrypted.data", "rb") as f:
    read_encrypted_data = f.read()

# 解密
decrypted_text = aes_decrypt(read_encrypted_data, read_aes_key)
print(f'Decrypted: {decrypted_text}')
