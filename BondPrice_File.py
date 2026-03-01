import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    
    n = int(m * ppy)                
    r = y / ppy                      
    c = face * couponRate / ppy      
    
    t = np.arange(1, n + 1)          
    
    discount = (1 + r) ** (-t)     
    
    price = c * np.sum(discount) + face * discount[-1]
    
    return price
