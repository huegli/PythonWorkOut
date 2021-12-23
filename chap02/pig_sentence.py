def pl_sentence(sentence):
    result = []
    words = sentence.split(' ')

    for word in words:
        if word[0] in 'aeiou':
            result.append(''.join([word, 'way']))
        else:
            result.append(''.join([word[1:], word[0], 'ay']))

    return ' '.join(result)


if __name__ == "__main__":
    print("'this is a test translation' -> " +
          pl_sentence('this is a test translation'))
    print(f"'the spice must flow' -> {pl_sentence('the spice must flow')}")
