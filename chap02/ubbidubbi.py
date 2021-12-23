def ubbidubbi(word):
    output = []

    for chr in word:
        if chr in 'aeiou':
            output.append('ub')
        output.append(chr)

    return ''.join(output)


if __name__ == "__main__":
    print(f"elephant -> {ubbidubbi('elephant')}")
    print(f"octopus -> {ubbidubbi('octopus')}")
    print(f"python -> {ubbidubbi('python')}")
