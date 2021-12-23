from collections import Counter


def most_repeating_letter_count(word):
    return Counter(word).most_common(1)[0][1]


def most_repeating_word(sentence):
    return max(sentence, key=most_repeating_letter_count)
