from functools import reduce
from random import randint

password = "1jd90-*&-lmpasd[]!!@#asdasdnoio0nkjn"
hashed_password = None
key_num = 7


def decrypt1(p):
    t2 = [n >> key_num for n in [ord(c) for c in p[key_num:-key_num]]]
    return reduce((lambda acc, x: acc + chr(x)), t2, "")


def decrypt2(p: str):
    i, s = 0, ""
    while i < len(p):
        while i % key_num != 0:
            i += 1
        i, s = i+1, s+p[i]
    return s


def decrypt3(p: [int]):
    p = [c // key_num for c in p]
    return reduce((lambda acc, x: acc + chr(x)), p, "")


def gen_rand_str():
    s = [chr(randint(32, 126)) for _ in range(key_num)]
    return reduce((lambda acc, x: acc + x), s, "")


def encrypt1(p: str):
    t2 = [n << key_num for n in [ord(c) for c in gen_rand_str()+p+gen_rand_str()]]
    return reduce((lambda acc, x: acc + chr(x)), t2, "")


def encrypt2(p: str):
    i, k = 0, key_num << key_num
    s = ""
    for c in p:
        while i % key_num != 0:
            s += chr(k)
            k = k >> 1 if k > 0 else key_num << key_num
            i += 1
        s += c
        i += 1
    return s


def encrypt3(p):
    return [ord(c) * key_num for c in p]


en = encrypt3(encrypt1(encrypt2(password)))
de = decrypt2(decrypt1(decrypt3(en)))
print(password)
print(en)
print(de)


def access_something_secure(password: str):
    pass
