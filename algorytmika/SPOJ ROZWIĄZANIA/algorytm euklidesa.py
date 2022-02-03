


def nwd():
    for i in range(int(input())):
        nums = input().split()
        a = int(nums[0])
        b = int(nums[1])

        while a != b:
            if a > b:a -= b
            else:b -= a
        print(a)

nwd()





