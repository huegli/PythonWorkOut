from operator import itemgetter


def alphabetize_names(phonebook):
    return sorted(phonebook, key=itemgetter("last", "first"))
