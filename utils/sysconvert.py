
import numpy as np
import pandas as pd
import time

data = 1500

# 整形转btyes类型
byte = data.to_bytes(4,'little')
print(byte)     # b'\xdc\x05\x00\x00'

# bytes转整形
data = int.from_bytes(byte,'little')
print(data)     # 1500

# bytes转16进制
st = byte.hex()
print(st)

# 整形转16进制
st = hex(data)
print(st)   # 0x10

# 16进制转整形
data = int(st,16)
print(data)     # 1500

# bytes转二进制
bi = bin(int.from_bytes(byte,'little'))
print(bi)
print(bi[2:4])


import time

import socket

ip_address = '192.168.1.240'

# 将IP地址转换为32位整数
packed_ip = socket.inet_aton(ip_address)
print(packed_ip)
int_ip = int.from_bytes(packed_ip, byteorder='big')
print(int_ip)

# 将整数转换为小端序排列的16进制数
hex_ip = format(int_ip, '08x')  # 先将整数转换为8位16进制数
print(hex_ip)
little_endian_hex_ip = ''.join(reversed([hex_ip[i:i+2] for i in range(0, len(hex_ip), 2)]))

print(little_endian_hex_ip)  # 输出结果为：f001a8c0


import struct
data = '0xEB90149F'
byte_data = bytes.fromhex(data[2:])    # 去掉0x前缀，并转为bytes类型

byte_array = bytearray(18)
byte_array[:len(byte_data)] = byte_data[::-1]
output_bytes = struct.pack('<' + 'B'*18, *byte_array)
print(output_bytes)


ip_address = '192.168.1.240'
packed_ip = socket.inet_aton(ip_address)
print(packed_ip)
byte_array = bytearray(18)
byte_array[:len(packed_ip)] = packed_ip[::-1]
output_bytes = struct.pack('<' + 'B'*18, *byte_array)
print(output_bytes)