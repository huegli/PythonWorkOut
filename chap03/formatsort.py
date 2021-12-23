from operator import itemgetter


def format_sort_records(people):
    outstr = ""

    sorted_people = sorted(people, key=itemgetter(1, 0))

    for person in sorted_people:
        outstr += "{1:<11}{0:<11}{2:5.2f}\n".format(
            person[0],
            person[1],
            person[2])

    return outstr
