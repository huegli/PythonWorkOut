total = 0


def restaurant(order):
    MENU = {"sandwich": 10, "tea": 7, "icecream": 5}
    global total

    if order in MENU:
        total += MENU[order]
        output = "Running total is {total}".format(total=total)
    elif order.strip() == "":
        output = "Grand total is {total}".format(total=total)
    else:
        output = "Not available"

    return output
