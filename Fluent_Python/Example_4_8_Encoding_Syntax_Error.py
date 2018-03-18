# 'ola.py' : “Hello, World!” in Portuguese

# coding: cp1252

print('Olá, Mundo!')


u16 = 'El Niño'.encode('utf_16')
print(u16)
print(list(u16))

u16le = 'El Niño'.encode('utf_16le') # little endian
print(u16le)
print(list(u16le))

u16be = 'El Niño'.encode('utf_16be') # big endian
print(u16be)
print(list(u16be))
