#! /usr/bin/env python3
# ########################
# rdice - v1, b71521
# my famous rdice application,
# written in python3.
# not as good as the c or
# cpp versions, but hopefully
# that will change in the
# near future.
# for now, Quick&Dirty;
# like MS.
# brianc2788@gmail.com
# ########################
import random

strInput = ''
nValue = 0
bRun = 1

print('[instructions:]')
print('- Enter # of dice to roll\n-OR-\n- Type "/quit" to exit.')

while bRun:
    strInput = input('enter: ')
    if strInput == '/quit':
        bRun = 0
    else:
        nValue = int(strInput)
        nCount = 0

        while nValue > 0:
            nCount = nCount + 1
            print('Roll #',nCount, ': ', random.randint(1,6))
            nValue = nValue - 1
