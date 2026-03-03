import itertools
def permutations(s):
    return list(set(''.join(w) for w in itertools.permutations(s)))
​
    
    
    
        
        
        