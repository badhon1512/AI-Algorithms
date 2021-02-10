# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 22:03:57 2020

@author: BADHON
"""
import random
i=1
isAdart=int()
isBdart=int()
currentPos='l'
total=0
non=0
while i<=5:
    isAdart=random.randint(0,1)
    isBdart=random.randint(0,1)
    
    if currentPos=='l':
    
        if isAdart==1:
            print('A is dart')
            if random.randint(0,1)==1:
                print("A is cleaned:suck")
                total+=1
            
            else:
                total-=1
                print("A is  not cleaned : Nop")
        else:
            print('A is not dart: non')
            non+=1;
             
            
        if isBdart==1:
            print('B is dart')
          
            if random.randint(0,1)==1:
                print('r')
                print("B is cleaned:suck")
                total+=1
                currentPos='r'
            
            else:
                total-=1
                print("B is  not cleaned : Nop")
        else:
            print("B is not dart:non")
            non+=1;
        #print("inside if")
        
        
        
                
    elif currentPos=='r':
        if isBdart==1:
            print('B is dart')
            if random.randint(0,1)==1:
                print("B is cleaned:suck")
                total+=1
            
            else:
                total-=1
                print("B is  not cleaned : Nop")
        else:
            print("B is not dart")
            non+=1;
            
        if isAdart==1:
            print('A is dart')
          
            if random.randint(0,1)==1:
                print('l')
                print("A is cleaned:suck")
                total+=1
                currentPos='l'
            
            else:
                total-=1
                print("A is  not cleaned : Nop")
        else:
            print("A is not dart")
            non+=1;
        #print("inside elif")
    i+=1

accuracy=((total+non)/10)*100
print("accuracy of vaccum cleaner is {} %".format(accuracy))
            
            
            

        
            
    

