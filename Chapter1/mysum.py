def mysum(*numbers):

    result = 0
    for val in numbers:
        result += val
        
    return result
    
print(f"1+2+3 = {mysum(1,2,3)}")
print(f"4+5+6+3+2+1 = {mysum(4,5,6,3,2,1)}")
print(f"9+99+999+9999 = {mysum(9,99,999,9999)}")
print(f"mysum(*[5,25,55] = {mysum(*[5, 25, 55])}")