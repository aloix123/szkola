sums = []
current_sum = 0

while True:
    try:
        inpt = int(input())
        current_sum += inpt
        sums.append(current_sum)
    except ValueError:
        for s in sums:
            print(s)
        exit()