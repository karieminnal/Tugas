# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 20:30:22 2019

@author: NISA
"""

def npm9(npm):
    a=npm[0]
    b=npm[1]
    c=npm[2]
    d=npm[3]
    e=npm[4]
    f=npm[5]
    g=npm[6]
    for x in a,b,c,d,e,f,g:
    
        if int(x)%2==1:
            print(x,end ="")

i=0
npm=input("Masukan NPM : ")
while i<1:
    if len(npm) < 7:
        print("NPM Kurang dari 7 digit")
        npm=input("Masukan NPM : ")
    elif len(npm) > 7:
        print("NPM lebih dari 7 digit")
        npm=input("Masukan NPM : ")
    else:
        i=1
npm9(npm)
