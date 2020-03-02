def mysum(*args):

    result = 0
    for _, val in enumerate(args):
        result += val
        
    return result
    
print(f"1+2+3 = {mysum(1,2,3)}")
print(f"4+5+6+3+2+1 = {mysum(4,5,6,3,2,1)}")