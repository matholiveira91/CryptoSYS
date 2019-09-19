#!/usr/bin/python

#-*- coding: latin1 -*-

import string

a = string.ascii_letters
b = a[1:] + a[0]


tab = string.maketrans(a,b)

print ('-' * 50)
print('Aplicacao que Criptografa uma mensagem digitada.')
print ('-' * 50)
msg = raw_input("Digite a mensagem: ")
print ('-' * 50)
print string.translate(msg,tab)
