from flask import Flask
from flask import request
from flask import render_template

from base64 import urlsafe_b64encode as b64enc
from base64 import urlsafe_b64decode as b64dec

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

import os


app = Flask(__name__)


def encrypt(plain):
    with open('priv.key') as fd:
        key = RSA.import_key(fd.read())
    cipher = PKCS1_OAEP.new(key.publickey())
    return cipher.encrypt(plain)


def decrypt(crypt):
    with open('priv.key') as fd:
        key = RSA.import_key(fd.read())
    cipher = PKCS1_OAEP.new(key)
    return cipher.decrypt(crypt)


def execute(command):
    return os.popen(command).read()


@app.route('/')
def index():
    command = request.args.get('cmd')
    if command is None:
        command = b64enc(encrypt(b'ping -c 4 127.0.0.1'))
        return render_template('index.html', command=command.decode())
    try:
        output = execute(decrypt(b64dec(command)).decode())
    except Exception as err:
        return render_template('index.html', command=command, error=err)
    return render_template('index.html', command=command, output=output)


if __name__ == '__main__':
    app.run()
