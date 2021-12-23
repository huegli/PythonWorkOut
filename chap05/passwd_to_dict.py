def passwd_to_dict(pwdfile):
    result = {}
    for line in pwdfile:
        if not line.startswith(('\n', '#')):
            elems = line.strip().split(':')
            result[elems[0]] = int(elems[2])
    return result
