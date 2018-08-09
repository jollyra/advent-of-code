#!/usr/bin/env python3


import hashlib


def mine(secret):
    salt = 0
    while 1:
        plaintext = secret + str(salt)
        hash = hashlib.md5(plaintext.encode('utf-8')).hexdigest() 
        if hash[:6] == '000000':
            return salt
        salt += 1


if __name__ == '__main__':
    assert mine('abcdef') == 609043
    assert mine('pqrstuv') == 1048970
    print('pass')
    ans = mine('iwrupvqb')
    print('ans: {}'.format(ans))
