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


def day8():
    while True:
        a = int(input("별의 개수:"))
        if a == 0:
            break
        for i in range(a, 0, -1):
            print(" "*i, "*"*(a-i+1))


def day9():
    while True:
        a = int(input("정수 입력, 0입력시 종료:"))
        if a == 0:
            break
        a = a**2
        a = a**(1/2)
        print(a)


def day10():
    while True:
        a = int(input("줄 수:"))
        if a == 0:
            break
        for i in range(a, 0, -1):
            print(" "*i, "*"*((a-i+1)*2-1), " "*i)


def day11():
    start = int(input("시작수:"))
    end = int(input("끝수:"))
    sum = 0
    for i in range(start, end+1):
        sum += i
    print("합계:", sum)


def day12():
    import time as t
    startTime = t.time()  # 시작시간
    for i in range(10000000):  # 천만
        pass
    endTime = t.time()
    eTime = endTime-startTime  # 경과시간(걸린 시간)
    print('경과시간:%.3f초' % eTime)


def day13():
    import time as t
    startTime = t.time()  # 시작시간
    start = 10000000
    end = 20000000
    if start > end:
        start, end = end, start
    print((end+start)*(((end+1)-start)/2))
    endTime = t.time()
    eTime = endTime-startTime  # 경과시간(걸린 시간)
    print('경과시간:%.3f초' % eTime)


def day13_function(start, end):
    if start > end:
        start, end = end, start
    return((end+start)*(((end+1)-start)/2))


def day14():
    while True:
        _input = int(input("정수 n:"))
        if _input == 0:
            break
        sum = 0
        for i in range(1, _input+1):
            if i % 2 == 1:
                sum += i
        print(sum)


def day15():
    while True:
        _input = int(input("층수 n:"))
        nm = 1
        if _input == 0:
            break
        for i in range(0, _input):
            for ind2, vel2 in enumerate(range(0, _input)):
                if ind2+1 == _input:
                    print(str(nm)[-1])
                else:
                    print(str(nm)[-1], end="")
                nm += 1


def day16():
    while True:
        _input = int(input("정수 n:"))
        if _input == 0:
            break
        odd = 0
        even = 0
        all = 0
        for i in range(1, _input+1):
            if i % 2 == 1:
                odd += i
            if i % 2 == 0:
                even += i
            all += i
        print(f"홀수 합계:{odd}\n짝수합계:{even}\n총 합계:{all}")


def day17():
    while True:
        _input = int(input("층수 n:"))
        nm = 1
        if _input == 0:
            break
        for ind1, vel1 in enumerate(range(0, _input)):
            for ind2, vel2 in enumerate(range(0, _input)):
                if ind2 == ind1:
                    print(str(nm)[-1])
                    nm += 1
                    break
                else:
                    print(str(nm)[-1], end="")
                    nm += 1


def day18():
    while True:
        _input = int(input("정수:"))
        if _input == 0:
            break
        list = []
        for i in range(1, _input+1):
            if _input % i == 0:
                list.append(i)
        print(str(list).replace('[', '').replace(']', ''))


def day19():
    while True:
        try:
            a, b, c = map(int, input("정수3개 띄어쓰기로 입력: ").split())
        except:
            break
        if (a < b and a > c) or (a > b and a < c):
            print(a)
        elif (b < a and b > c) or (b > a and b < c):
            print(b)
        elif (c < a and c > b) or (c > a and c < b):
            print(c)


def day20():
    wordList = ['cat', 'dog', 'pig', 'hen', 'cow', 'duck', 'cat']
    while True:
        _input = input("단어입력:")
        if _input == "\n":
            break
        if _input in wordList:
            print(f"{_input}은 {wordList.index(_input)+1}번째에 있다.")


def day21():
    wordList = ['cat', 'dog', 'pig', 'hen', 'cow', 'duck', 'cat']
    while True:
        _input = input("단어입력:")
        if _input == "\n":
            break
        if _input in wordList:
            print(f"{_input}은 {wordList.index(_input)+1}번째에 있다.")
        else:
            print(f"{_input}은 없음.")
