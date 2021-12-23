def hex_output(hexnum):
    decnum = 0

    for power, num in enumerate(reversed(hexnum)):
        try:
            decnum += 16**power*int(num, 16)
        except ValueError:
            return -1

    return decnum


if __name__ == "__main__":
    print(f"0x50 is {hex_output('50')}")
    print(f"0x20 is {hex_output('20')}")
    print(f"0xAA is {hex_output('AA')}")
    print(f"0xxx is {hex_output('xx')}")
