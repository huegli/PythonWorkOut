from io import StringIO

import glob
import json


def read_scores(fname):

    with open(fname) as fh:
        scores = json.load(fh)

    result = {}
    for row in scores:
        for subject in ['science', 'literature', 'math']:
            result.setdefault(subject, [])
            result[subject].append(row[subject])

    return result


def print_scores(dname):
    result = StringIO()
    result.write("\n")

    json_files = glob.glob('./scores/*.json')
    for fname in json_files:
        result.write(f"{fname}\n")
        scores = read_scores(fname)
        for key, value in scores.items():
            result.write("    ")
            result.write(f"{key}: min {min(value)}")
            result.write(f", max {max(value)}")
            result.write(f", average {sum(value)/len(value)}\n")

    return result
