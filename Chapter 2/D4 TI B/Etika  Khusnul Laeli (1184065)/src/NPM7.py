# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 21:58:38 2019

@author: ANIF
"""

#Perkalian
i=0
npm=input("Masukan NPM : ")
while i<i:
    if len(npm) < 7:
        print("NPM Kurang dari 7 digit")
        npm=input("Masukan NPM : ")
    elif len(npm) > 7:
        print("NPM lebih dari 7 digit")
        npm=input("Masukan NPM : ")
    else:
        i=1
a=npm[0]
b=npm[1]
c=npm[2]
d=npm[3]
e=npm[4]
f=npm[5]
g=npm[6]
y=0

for x in a,b,c,d,e,f,g:
    y*=int(x)
print(y)