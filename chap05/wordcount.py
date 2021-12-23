def wordcount(wcfile):
    unique_words = set()
    lcount = 0
    wcount = 0
    ccount = 0
    for line in wcfile:
        lcount += 1
        ccount += len(line)
        words = line.split()
        wcount += len(words)
        unique_words.update(words)

    return (ccount, wcount, lcount, len(unique_words))
