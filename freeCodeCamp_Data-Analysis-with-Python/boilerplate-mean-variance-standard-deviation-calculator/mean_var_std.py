import numpy as np

def calculate(list):
    i=0  
    for x in list:
      if str(x).isdigit():
        i=i+1
      
    try:
        a = np.array(list)
        b = a.reshape(3,3) 
    except ValueError:
        raise ValueError("List must contain nine numbers.")
    
    if i==9:
        calculations = {}
        
        
        calculations["mean"]=[b.mean(axis=i).tolist() for i in [0,1,None] ]
        calculations["variance"]=[b.var (axis=i).tolist() for i in [0,1,None] ]
        calculations["standard deviation"]=[b.std(axis=i).tolist() for i in [0,1,None] ]
        calculations["max"]=[b.max(axis=i).tolist() for i in [0,1,None] ]
        calculations["min"]=[b.min(axis=i).tolist() for i in [0,1,None] ]
        calculations["sum"]=[b.sum(axis=i).tolist() for i in [0,1,None] ]
    
        return calculations
    else:
        return "List must contain nine numbers."


    