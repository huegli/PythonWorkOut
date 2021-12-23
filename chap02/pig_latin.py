def pig_latin(word):
    if word[0] in 'aeiou':
        return ''.join([word, 'way'])
    else:
        return ''.join([word[1:], word[0], 'ay'])


if __name__ == "__main__":
    print(f"air = {pig_latin('air')}")
    print(f"eat = {pig_latin('eat')}")
    print(f"python = {pig_latin('python')}")
    print(f"computer = {pig_latin('computer')}")
    print(f"hello = {pig_latin('hello')}")
