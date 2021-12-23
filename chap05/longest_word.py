import os


def find_longest_word(fname):
    max_wlen = 0

    with open(fname, "r") as fh:
        for line in fh:
            for word in line.split():
                if len(word) > max_wlen:
                    max_word = word
                    max_wlen = len(word)

    return max_word


def find_all_longest_word(dname):
    result = {}
    files = os.listdir(dname)

    for fn in files:
        filename = os.path.join(dname, fn)
        result[fn] = find_longest_word(filename)

    return result
