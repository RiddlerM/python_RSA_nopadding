import os, sys
import rsa
import base64
from Crypto.PublicKey import RSA
import os

filepath = os.path.dirname(os.path.dirname(__file__))

message = 'iamatesttext'


class Encrypt:

    def encrypt(self, message):
        e = '10001'
        e = int(e, 16)
        n = ''  #需要自己填写
        n = int(n, 16)
        print(n)
        rsa_pubkey = rsa.PublicKey(e=e, n=n)

        #如果通过导入本地证书的模式 请注释上面部分，取消注释以下部分
        # with open(filepath + '/Util/test.pem') as publickfile:
        #     p = publickfile.read()
        # # print("p=="+str(p))
        # rsa_pubkey = RSA.importKey(p)

        crypto = self._encrypt(message.encode(), rsa_pubkey)
        return crypto.hex()

    def _pad_for_encryption(self, message, target_length):
        msglength = len(message)
        print("msglength==" + str(msglength))
        padding = message
        padding_length = target_length - msglength
        for i in range(padding_length):
            padding += b'\x00'
        padding = padding[::-1]
        print('padding:', padding)
        return b''.join([padding])

    def _encrypt(self, message, pub_key):
        keylength = rsa.common.byte_size(pub_key.n)
        padded = self._pad_for_encryption(message, keylength)
        payload = rsa.transform.bytes2int(padded)
        encrypted = rsa.core.encrypt_int(payload, pub_key.e, pub_key.n)
        block = rsa.transform.int2bytes(encrypted, keylength)

        return block

    def str_to_hex(self, s):
        return ' '.join([hex(ord(c)).replace('0x', '') for c in s])


en = Encrypt()
print(en.encrypt(message))