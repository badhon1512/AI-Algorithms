# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 09:40:17 2020

@author: BADHON
"""

path={
      
      'Oradea':['Zerind','Sibiu'],
      'Zerind':['Arad','Oradea'],
      'Sibiu':['Arad','Oradea','Fagaras','Rimnicu Vilcea'],
      'Arad':['Sibiu','Zerind','Timisoara'],
      'Timisoara':['Arad','Lugoj'],
      'Lugoj':['Timisoara','Mehadia'],
      'Mehadia':['Lugoj','Drobeta'],
      'Drobeta':['Mehadia','Craiova'],
      'Craiova':['Drobeta','Rimnicu Vilcea','Pitesti'],
      'Rimnicu Vilcea':['Sibiu','Pitesti','Craiova'],
      'Pitesti':['Rimnicu Vilcea','Craiova','Bucharest'],
      'Fagaras':['Sibiu','Bucharest'],
      'Bucharest':['Fagaras','Pitesti','Giurgiu','Urziceni'],
      'Giurgiu':['Bucharest'],
      'Urziceni':['Bucharest','Vaslui','Hirsova'],
      
      'Hirsova':['Eforie'],
      'Eforie':["Hirsova"],
      'Vaslui':['Urziseni','Lasi'],
      "Lasi":['Vaslui','Neamt'],
      'Neamt':['Lasi']
      
      
      
        
      }

found=False


search='Bucharest';
start='Zerind'

 
frontier=[start]
explorer=[]


def get_parent(value):
    for key,val in path.items():
        for i in val:
            if i==value:
                return key



i=0;
while  len(frontier):
    f=frontier.pop(0);
    expand=list()
   
   
      
    
    if f not in explorer:
    
      
        if f==search:
            found=True;
            break;
    
        if f in path:
            for value in path[f]:
                if value not in frontier and value not in explorer:
                
        
                     frontier.append(value)
                     expand.append(value)
    explorer.append(f);
    print('frontier : ',format(frontier))
   
    print('Explorer : ',format(explorer))
    print('expand : ',format(expand))
    
                
   
print(explorer)
    
    
    
    
    
    
    
    
fullpath=[search]

if found:
    print("value is founded")
    
    while not fullpath[len(fullpath)-1]==start:
        fullpath.append(get_parent(fullpath[len(fullpath)-1]))
        
    fullpath.reverse()
    print("the path is :")
    for val in fullpath:
        print('{0}--'.format(val),end=" ")

        
    
else:
     print("value is not founded")
    
 

    
    
    

    
