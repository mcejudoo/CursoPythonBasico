# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 10:30:32 2022

@author: Anton
"""

n = 0x3A
print(bin(n))

"""
0011 1010
0000 0001
0000 0100
"""

# Bit 2 a 1
n = n | (1<<2)
print(bin(n))

# Bit 4 a 0
n = n & ~(1<<4)
print(bin(n))