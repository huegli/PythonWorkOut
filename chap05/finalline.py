def get_final_line(fname):
    with open(fname) as f:
        for line in f:
            pass
    return line


if __name__ == "__main__":
    print(get_final_line("/etc/passwd"))
