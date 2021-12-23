def mysum(*items):
    output = ()
    if not items:
        return ()
    else:
        output = items[0]
        for item in items[1:]:
            output += item

    return output
