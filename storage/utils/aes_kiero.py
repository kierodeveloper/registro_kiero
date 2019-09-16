import base64, sys
import Crypto.Cipher.AES
import re
aeskey = Random.new().read(32)
key = [] # See rgbKey
salt = 'ehjtnMiGhNhoxRuUzfBOXw==' # See rgbIV
aes = Crypto.Cipher.AES.new(key, Crypto.Cipher.AES.MODE_CBC, salt)
text = 'OBgFPGx+2woENzlnsq/i9kWGKXTHJBNVgww4rjqdPR0='
regex = '[a-zA-Z0-9 +-,\/ : > ]+'
qwe = aes.decrypt(text).decode('utf-16')

print(re.findall(regex, qwe)[0])

