def mysum(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum


if __name__ == "__main__":
    print(f"1+2+3 = {mysum(1,2,3)}")
    print(f"10+20+30+40+50 = {mysum(10, 20, 30, 40, 50)}")
