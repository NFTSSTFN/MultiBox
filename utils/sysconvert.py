
import numpy as np
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