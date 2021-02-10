# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 09:57:00 2020

@author: BADHON
"""

path=[
      ['q1','null','null','null','null','null','null','null'],
      ['null','null','q2','null','null','null','null','null'],
      ['null','null','null','q3','null','null','null','null'],
      ['null','null','null','null','null','q4','null','null'],
      ['null','null','null','null','null','null','null','q5'],
      ['null','null','null','null','null','null','q6','null'],
      ['null','null','null','null','q7','null','null','null'],
      ['null','q8','null','null','null','null','null','null']
      
      
      
      ]




q=[[0,0],[1,2],[2,3],[3,5],[4,7],[5,6],[6,4],[7,1]]

for t in range(8):
    
    attack=[]
    
    
    pi=q[t][0]
    pj=q[t][1]
   # print(t)
    i=q[t][0]
    j=0
    queen=path[q[t][0]][q[t][1]]
    print(queen)
   
    
        # for row attack
    while  j<=7:
        #print(i)
        #print(j)
            
        if path[i][j]!='null' and path[i][j]!=queen:
              
              attack.append(path[i][j])
                
            
        j+=1
       
    #col attack
    j=q[t][1]
    i=0
    while j<=7:
        #print(j)
        #print(i)
        if path[j][i]!='null' and path[i][j]!=queen:
              
              attack.append(path[j][i])
        j+=1
    
    
    
    #attack for left up diagonal
    i=q[t][0]-1
    j=q[t][1]-1
    while i>=0 and j>=0:
       # print(i)
        #print(j)
        if path[i][j]!='null' and path[i][j]!=queen:
              
              attack.append(path[i][j])
        j-=1
        i-=1
        
    i=q[t][0]+1
    j=q[t][1]+1
    while i<=7 and j<=7:
        #print(i)
        #print(j)
        if path[i][j]!='null' and path[i][j]!=queen:
              
              attack.append(path[i][j])
        j+=1
        i+=1
    
    
    
    
    #attack for right up diagonal
    i=q[t][0]-1
    j=q[t][1]+1
    while i>=0 and j<=7:
        #print(i)
        #print(j)
        if path[i][j]!='null' and path[i][j]!=queen:
              
              attack.append(path[i][j])
        j+=1
        i-=1
        
    i=q[t][0]+1
    j=q[t][1]-1
    while i<=7 and j>=0:
        #print(i)
        #print(j)
        if path[i][j]!='null' and path[i][j]!=queen:
              
              attack.append(path[i][j])
        j-=1
        i+=1
    
    
        
   #print(attack)
    
        
    
    
    print("attcak for {0} are {1}".format(queen,attack))

    
            
           
   