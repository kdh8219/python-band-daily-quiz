def intInput(prompt: str = "", errorMessage: str = "") -> int:
    """
    :param prompt: 사용자에게 물어보는 문구
    :param errorMessage: 사용자가 입력한 값이 올바르지 않을 때 보여주는 문구, 공백일시 출력 안함.
    :return: 사용자가 입력한 값
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            if errorMessage != "":
                print(errorMessage)
            else:
                continue
            return(intInput(prompt, errorMessage))


def day1():
    while True:
        a = intInput("정수 입력:")
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
        a = intInput()
        if a == 0:
            break
        for b in range(1, 1+a):
            print(b*"*")


def day5():
    a = intInput()
    b = intInput()
    print(str(a)+","+str(b))
    b = a+b
    a = b-a
    b = b-a
    print(str(a)+","+str(b))


def day6():
    while True:
        a = intInput()
        if a == 0:
            break
        for b in range(a, 0, -1):
            print(b*"*")


def day7():
    while True:
        a = intInput("정수 입력, 0입력시 종료:")
        if a == 0:
            break
        if a < 0:
            a = 0-a
        print(a)


def day8():
    while True:
        a = intInput("별의 개수:")
        if a == 0:
            break
        for i in range(a, 0, -1):
            print(" "*i, "*"*(a-i+1))


def day9():
    while True:
        a = intInput("정수 입력, 0입력시 종료:")
        if a == 0:
            break
        a = a**2
        a = a**(1/2)
        print(a)


def day10():
    while True:
        a = intInput("줄 수:")
        if a == 0:
            break
        for i in range(a, 0, -1):
            print(" "*i, "*"*((a-i+1)*2-1), " "*i)


def day11():
    start = intInput("시작수:")
    end = intInput("끝수:")
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


def day14():
    while True:
        _input = intInput("정수 n:")
        if _input == 0:
            break
        sum = 0
        for i in range(1, _input+1):
            if i % 2 == 1:
                sum += i
        print(sum)


def day15():
    while True:
        _input = intInput("층수 n:")
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
        _input = intInput("정수 n:")
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
        _input = intInput("층수 n:")
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
        _input = intInput("정수:")
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


def day22():
    win = 0
    lost = 0
    while True:
        _input1 = intInput("정수:")
        _input2 = intInput("정수:")
        if _input1 == 0 and _input2 == 0:
            print(f"암산성적:{int(win/(win+lost)*100)}")
            break
        answer = int(input(f"{_input1}+{_input2}="))
        if answer == _input1+_input2:
            print("정답")
            win += 1
        else:
            print(f"오답! 정답은{_input1+_input2}!")
            lost += 1


def day23():
    wordList = []
    while True:
        _input = input("단어입력:")
        if _input == "\n":
            break
        if _input in wordList:
            print(f"{_input}은 {wordList.index(_input)+1}번째에 있다.")
        else:
            addinput = input(f"{_input}은 없음. 추가할까요?(y/n)")
            if addinput == "y":
                wordList.append(_input)
                print(f"{_input} 추가됨.")


def day24():
    import time as t
    startTime = t.time()
    n = 100000000  # 1억
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:  # n이 i로 나누어 떨어지면
            print(i, end=',')
            cnt += 1
    endTime = t.time()
    print(f"\n {cnt}개, 경과시간:{endTime-startTime}초")


def day25():
    import time as t
    _input = intInput("정수 입력:")
    startTime = t.time()
    divisors = []
    divisors_back = []
    divisors_end = []

    for i in range(1, int(_input**(1/2)) + 1):
        if (_input % i == 0):
            divisors.append(i)
            if (i != (_input // i)):
                divisors_back.append(_input//i)

    divisors_end = divisors + divisors_back[::-1]
    endTime = t.time()
    print(str(divisors_end).replace('[', '').replace(']', ''))
    print(f"\n {len(divisors_end)}개, 경과시간:{endTime-startTime}초")


def day26():
    myDic = {'sky': '하늘', 'apple': '사과', 'can': '깡통', 'boat': '배',
             'sea': '바다', 'smile': '미소', 'animal': '동물', 'park': '공원'}
    while True:
        _input = input("단어입력:")
        if _input == "":
            break
        if _input in myDic:
            print(f"{_input} {myDic[_input]}")
        else:
            print(_input+" 없음.")


def day27():
    import antigravity
    import os
    os.system("start https://youtu.be/HEMC_InYhyM")


def day28():
    while True:
        _input = intInput("정수 입력:")
        if _input == 0:
            break
        if _input == 1:
            print("소수 아님")
        else:
            for i in range(2, _input):
                if _input % i == 0:
                    print("소수 아님")
                    break
            else:
                print("소수")


def day29():
    import math
    import time as t
    while True:
        _input = intInput("정수 입력:")
        startTime = t.time()
        if _input == 0:
            break
        if _input == 1:
            print("소수 아님")
        else:
            for i in range(2, int(math.sqrt(_input)) + 1):
                if _input % i == 0:
                    print("소수 아님")
                    break
            else:
                print("소수")
        endTime = t.time()
        print(f"경과시간:{endTime-startTime}초")


def day30():
    import math
    import time as t

    def prime(count):
        if count == 0:
            return(False)
        if count == 1:
            return(False)
        else:
            for i in range(2, int(math.sqrt(count)) + 1):
                if count % i == 0:
                    return(False)
            else:
                return(True)

    start = input("시작수:")
    end = input("끝수:")
    startTime = t.time()
    alist = list(map(prime, range(int(start), int(end)+1)))
    endTime = t.time()
    print(f"{alist.count(True)}")
    print(f"경과시간:{endTime-startTime}초")


def day31():
    while True:
        _input = intInput("층수 입력:")
        if _input == 0:
            break
        for i in range(0, _input+1):
            print(f"{i}층 interval:{1-(1/_input)*i}초")
        print("도착")


def day32():
    while True:

        _input = intInput('정수:', "")
        if _input == 0:
            break
        if _input == 1:
            continue

        def primeFactorization(_input: int) -> list:
            _list = []
            for i in range(2, _input+1):
                while _input % i == 0:
                    _list.append(i)
                    _input = _input//i
            return(_list)

        _output = str(primeFactorization(_input)).replace(
            "[", "").replace("]", "").replace(", ", "x")
        print(_output)


def day33():
    from time import time

    text = 'Explicit is better than implicit.'
    print(f">{text}")
    startTime = time()
    _input = input(">")
    while _input != text:
        print("오타가 있습니다.")
        _input = input(">")
    endTime = time()
    print(f"{(len(text)/(endTime-startTime))*60}타/분")


def day34():
    while True:
        _input = intInput('정수:', "")
        if _input == 0:
            break
        if _input == 1:
            continue

        def primeFactorization(_input: int) -> dict:
            _list = {}
            for i in range(2, _input+1):
                while _input % i == 0:
                    if i in _list.keys():
                        _list[i] += 1
                    else:
                        _list[i] = 1
                    _input = _input//i
            return(_list)

        _output = primeFactorization(_input)
        for count, (number, up) in enumerate(_output.items()):
            if count+1 != len(_output):
                o = (f"{number}^{up}x" if up != 1 else f"{number}x")
            else:
                o = (f"{number}^{up}" if up != 1 else f"{number}")
            print(o, end="")
        print()


def day35():
    from time import time

    texts = ['Now is better than never.',
             'Life is too short, you need python.',
             'Happy python']
    text_len = 0
    allOfStartTime = time()
    for text in texts:
        text_len += len(text)
        print(f">{text}")
        startTime = time()
        _input = input(">")
        while _input != text:
            print("오타가 있습니다.")
            _input = input(">")
        endTime = time()
        print(f"{(len(text)/(endTime-startTime))*60}타/분")
    allOfEndTime = time()
    print(f"전체 {(text_len/(allOfEndTime-allOfStartTime))*60}타/분")


def day36():
    nameList = ['김', '이', '박', '최', '정', '강', '조', '윤', '장', '임']
    List = [95, 73, 82, 83, 64, 89, 77, 48, 74, 99]
    _list = {}
    for i in range(len(nameList)):
        _list[nameList[i]] = List[i]
    _list = sorted(_list.items())
    for name, score in _list:
        print(f"{name} {score}")


def day37():
    pList = [95, 73, 82, 83, 64, 89, 77, 48, 74, 99]
    sList = []
    print(f'0차 {pList}')
    print("정렬과정")
    for i in range(len(pList)):
        sList.append(min(pList))
        del pList[pList.index(min(pList))]
        print(
            f"{i+1}차 : {sList+pList}")


def day38():
    while True:
        _input = intInput("연도:")
        if _input % 4 == 0:
            if _input % 100 == 0:
                if _input % 400 == 0:
                    print("윤년")
                else:
                    print("평년")
            else:
                print("윤년")
        else:
            print("평년")


if __name__ == "__main__":
    try:
        date = intInput("일차 입력:", "정수만 입력하세요")
        print(f"\n{date}일차\n\n")
        eval(f"day{int(date)}()")
    except KeyboardInterrupt:
        exit()
