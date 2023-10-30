import copy
import random
# Consider using the modules imported above.

class Hat:
  
  def __init__(self,**kwargs):
    self.contents = []
        
    for k,v in kwargs.items():
      for i in range(v):
        self.contents.append(k) 
  
  def draw(self, rep):
    
    if rep > len(self.contents):
      return self.contents
    
    those_balls = []
    for i in range(rep):
      eleman = random.randrange(len(self.contents))
      those_balls.append(self.contents.pop(eleman))
    
    return those_balls


def experiment(hat,expected_balls,num_balls_drawn,num_experiments):

  olasilik = 0
  beklenen = []
  

  for i in range(num_experiments):
    yedek = copy.deepcopy(hat)
    cekilen = yedek.draw(num_balls_drawn)
    
    for k in expected_balls:
      beklenen.append(k)
    
    cek_dict = {}
    for j in cekilen:
      cek_dict[j] = cek_dict.get(j,0) + 1  
    
    sayim = 0
    
    for k in beklenen:
      if k in cek_dict and expected_balls[k] <= cek_dict[k]:
          sayim += 1 
    
    if sayim == len(beklenen):
      olasilik += 1
  
  olasilik /= num_experiments   
  return olasilik