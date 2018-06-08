#!/usr/bin/env python3


import re


def is_four_char_abba(s):
    h = s[:2]
    t = s[-2:]
    if h == t[::-1] and s[0] != s[1]:
        return True
    else:
        return False


def is_abba(s):
    if len(s) < 4:
        return False
    else:
        if is_four_char_abba(s[:4]):
            return True
        else:
            return is_abba(s[1:])


def supports_TLS(s):
    out_a = re.compile('^([a-z]+)\[')
    out_b = re.compile('\]([a-z]+)\[')
    out_c = re.compile('\]([a-z]+)$')
    outs = out_a.findall(s)
    outs.extend(out_b.findall(s))
    outs.extend(out_c.findall(s))

    in_a = re.compile('\[([a-z]+)\]')
    ins = in_a.findall(s)

    return any([is_abba(x) for x in outs]) and all([not is_abba(x) for x in ins])


def get_abas(xs):
    if len(xs) < 3:
        return []
    else:
        h = xs[:3]
        if h[0] == h[2]:
            return [h] + get_abas(xs[1:])
        else:
            return [] + get_abas(xs[1:])


def supports_SSL(s):
    out_a = re.compile('^([a-z]+)\[')
    out_b = re.compile('\]([a-z]+)\[')
    out_c = re.compile('\]([a-z]+)$')
    outs = out_a.findall(s)
    outs.extend(out_b.findall(s))
    outs.extend(out_c.findall(s))

    in_a = re.compile('\[([a-z]+)\]')
    ins = in_a.findall(s)

    out_abas = []
    for x in outs:
        if len(x) > 0:
            out_abas += get_abas(x)

    in_abas = []
    for x in ins:
        if len(x) > 0:
            in_abas += get_abas(x)

    for a in out_abas:
        for b in in_abas:
            if a[0] == b[1] and a[1] == b[0]:
                return True
    return False


def input_lines():
    with open('seven_input.txt', 'r') as f:
        return [line.strip() for line in f]


if __name__ == '__main__':
    assert is_four_char_abba('abba') is True
    assert is_four_char_abba('baba') is False
    assert is_four_char_abba('aaaa') is False
    assert is_abba('abba') is True
    assert is_abba('nabba') is True
    assert is_abba('aba') is False
    assert supports_TLS('abba[mnop]qrst') is True
    assert supports_TLS('abba[mnop]qrst[bddb]') is False
    assert supports_TLS('abcd[bddb]xyyx') is False
    assert supports_TLS('aaaa[qwer]tyui') is False
    assert supports_TLS('ioxxoj[asdfgh]zxcvbn') is True
    assert get_abas('zaz')[0] is 'zaz'
    assert len(get_abas('zazbz')) is 2
    assert supports_SSL('aba[bab]xyz') is True
    assert supports_SSL('xyx[xyx]xyx') is False
    assert supports_SSL('aaa[kek]eke') is True
    assert supports_SSL('zazbz[bzb]cdb') is True
    print('pass')

    tls_count = 0
    ssl_count = 0
    for ip in input_lines():
        if supports_TLS(ip):
            tls_count += 1
        if supports_SSL(ip):
            ssl_count += 1

    print('{} IPs support TLS'.format(tls_count))
    print('{} IPs support SSL'.format(ssl_count))

