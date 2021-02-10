# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 09:21:44 2020

@author: BADHON
"""

path={
      
      'Oradea':[['Zerind',71],['Sibiu',151]],
      'Zerind':[['Arad',75],['Oradea',71]],
      'Sibiu':[['Arad',140],['Oradea',151],['Fagaras',99],['Rimnicu',80]],
      'Arad':[['Sibiu',140],['Zerind',75],['Timisoara',118]],
      'Timisoara':[['Arad',118],['Lugoj',111]],
      'Lugoj':[['Timisoara',111],['Mehadia',70]],
      'Mehadia':[['Lugoj',70],['Drobeta',75]],
      'Drobeta':[['Mehadia',75],['Craiova',120]],
      'Craiova':[['Drobeta',120],['Rimnicu',146],['Pitesti',138]],
      'Rimnicu':[['Sibiu',80],['Pitesti',97],['Craiova',146]],
      'Pitesti':[['Rimnicu',97],['Craiova',138],['Bucharest',101]],
      'Fagaras':[['Sibiu',99],['Bucharest',211]],
      'Bucharest':[['Fagaras',221],['Pitesti',101],['Giurgiu',90],['Urziceni',85]],
      'Giurgiu':[['Bucharest',90]],
      'Urziceni':[['Bucharest',90],['Vaslui',142],['Hirsova',86]],
      
      'Hirsova':[['Eforie',86]],
      'Eforie':[["Hirsova",86]],
      'Vaslui':[['Urziceni',142],['Lasi',92]],
      "Lasi":[['Vaslui',92],['Neamt',87]],
      'Neamt':[['Lasi',87]]
      
      
      
        
      }
h={
      'Oradea':380,
      'Zerind':374,
      'Sibiu':253,
      'Arad':366,
      'Timisoara':329,
      'Lugoj':244,
      'Mehadia':241,
      'Drobeta':242,
      'Craiova':160,
      'Rimnicu':193,
      'Pitesti':100,
      'Fagaras':176,
      'Bucharest':0,
      'Giurgiu':77,
      'Urziceni':80,
      
      'Hirsova':151,
      'Eforie':161,
      'Vaslui':199,
      "Lasi":226,
      'Neamt':234
      }

node={
      'Oradea':['Null',0],
      'Zerind':[' ',0],
      'Sibiu':[' ',0],
      'Arad':[' ',0],
      'Timisoara':[' ',0],
      'Lugoj':[' ',0],
      'Mehadia':[' ',0],
     
      'Drobeta':[' ',0],
      'Craiova':[' ',0],
      'Rimnicu':[' ',0],
      'Pitesti':[' ',0],
      'Fagaras':[' ',0],
      'Bucharest':[' ' ,0],
      'Giurgiu':[' ',0],
      'Urziceni':['',0],
      
      'Hirsova':[' ',0],
      'Eforie':[' ',0],
      'Vaslui':[' ',0],
      "Lasi":[' ',0],
      'Neamt':[' ',0]
      
      }

found=False


search='Bucharest';
start='Zerind'

 
frontier={start:0}
explorer=[]

print("Frontier   {0}".format(frontier))
print("explorer {0}".format(explorer)) 
while  len(frontier):
    print("Frontier   {0}".format(frontier))
    f=""
    i=0
    cost=11111111111
    for key,val in frontier.items():
        if val<cost:
            cost=val
            f=key
    
    #print(cost)
    #print(f)
    #print(frontier)
    #print(explorer)
   
    
        
    frontier.pop(f)
    expand=list()
   
    
    
    
    if f not in explorer:
        explorer.append(f);
        
    
       # print(f)
        if f==search:
            found=True;
            break   #updated line
  
       
        
        
    
        if f in path:
            for value in path[f]:
                
                if value[0] in frontier and not value[0] in explorer:
                    
                    if node[f][1]+value[1]<frontier[value[0]]:
                        
                        
                        frontier[value[0]]=node[f][1]+value[1]

                        
                        node[value[0]]=[f,(node[f][1]+value[1])]
                     
                    
                        
                  
                        
                elif value[0] in explorer:
                    continue;
                    
                else:
                     frontier[value[0]]=node[f][1]+value[1]

                        
                     node[value[0]]=[f,node[f][1]+value[1]]
                     
                    
                   
                  
                     
                    
                    
    print("explorer {0}".format(explorer))
    print("expand {0}".format(f)) 
    
    
    
    
print("Frontier   {0}".format(frontier))
print("explorer {0}".format(explorer)) 
                
print("node      {0}".format(node)    )
    
    
fullpath=[search]


if found:
    print("Goal is founded")
    p=[search]
    key=search
    cost=0
    while key!= start:
       # print(node[key])
       
        p.append(node[key][0])
        cost+=node[key][1]
        key=node[key][0]
    p.reverse()
    
    tpath=""
    
    for i in p:
        tpath+="-->"+i
        
    print("the path is {0}".format(tpath))
    
    print("the cost is {0}".format(cost))
else:
    print("Goal is not founded")

       
       
     

