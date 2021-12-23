import csv


def passwd_to_csv(pwdfile, csvfile):

    infile = csv.reader(pwdfile, delimiter=":")
    outfile = csv.writer(csvfile, lineterminator="\n")

    for record in infile:
        if len(record) > 1:
            csvrecord = (record[0], record[2])
            outfile.writerow(csvrecord)

    return
