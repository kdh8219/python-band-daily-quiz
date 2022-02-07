def day1():
    while True:
        a = int(input("정수 입력:"))
        if a % 2 == 0:
            print("짝수")
        else:
            print("홀수")


def day2():
    a = input()
    b = input()
    print(a+","+b)
    a, b = b, a
    print(a+","+b)


def day3():
    a = input()
    b = input()
    print(a+","+b)
    temp = a
    a = b
    b = temp
    del temp
    print(a+","+b)


def day4():
    while True:
        a = int(input())
        if a == 0:
            break
        for b in range(1, 1+a):
            print(b*"*")


def day5():
    a = int(input())
    b = int(input())
    print(str(a)+","+str(b))
    b = a+b
    a = b-a
    b = b-a
    print(str(a)+","+str(b))


def day6():
    while True:
        a = int(input())
        if a == 0:
            break
        for b in range(a, 0, -1):
            print(b*"*")


def day7():
    while True:
        a = int(input("정수 입력, 0입력시 종료:"))
        if a == 0:
            break
        if a < 0:
            a = 0-a
        print(a)
