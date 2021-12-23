def run_timing():
    total_time = 0.0
    times = 0

    while run := input("Enter 10 km run time: "):
        try:
            total_time += float(run)
        except ValueError():
            break
        times += 1

    print(f"Average of {total_time/times:.2f} over {times}")


if __name__ == "__main__":
    run_timing()
