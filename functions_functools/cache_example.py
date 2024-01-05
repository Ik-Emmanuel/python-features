from functools import cache, cached_property
import time

@cache
def add(x,y):
    """
    This caches the results of the function 
    for expensive computations that take too much time to finish and you dont want to
    recompute each time
    
    NOTE: this reduces the time complexity, but willl  increase the memory complexity
    """
    
    print("running")
    time.sleep(5)
    print("done computing")
    return x + y


a = add(2, 5)
print(a)

# this one will use the cached version if
# you calling the function with the same parameters and also the order matters
print(a)



# for classes 
# @cached_property can be use to avoid recomputing properties