import random

random_number = random.randint(1, 100)  # 랜덤한 숫자 1~ 100 을 생성해 주는 코드
try_count = 0                                 # 문자열이 아니라 숫자열로 생성 해 주는 듯? = str() 문자열, int() 숫자열 헷갈림 /// 해결
try_list = []                                   # 시도 횟수를 세기 위해서 0번쨰 시도부터 시작한다.
# print(random_number)                        # 코드 수정시 사용
print("[up,down 게임입니다.]")
while True :
    try_num = int(input("범위는 1~ 100 까지 입니다 = "))
    try_count += 1
    final_try_count = try_count                     # 트라이 리스트에 입력시 마다 시도 횟수가 추가되고 ??? == while 문 안에서는 새롭게 시작하면서 반복한다.
    try_list.append(final_try_count)                # +1 이된 try_count 의 값을 받아줘서 리스트에 넣는다?
    # print(try_list)                               # 혹시 리스트에 추가가 되는지 확인하려고

    if try_num == random_number:
        print("==== 정답 입니다. ====")
        print(f'시도 횟수 = {try_count}')                  # 젤 우선 문제점 : 리스트에 요소가 추가되지 않는다.
        regame = input('다시 하실래요? [Y,N] = ')
        if regame == "y":
            random_number = random.randint(1, 100)
            try_count = 0
            print(f'게임 최고 도전 횟수는 {max(try_list)} 입니다.')
        elif regame == 'n':
            print("=====게임을 종료합니다.=====")
            break
        elif regame != str:
            print('****[Y,N] 중 소문자로만 입력 가능합니다.****')
            regame = input('다시 하실래요? [Y,N] = ')
            if regame == 'n':
                print(f'지금까지 가장오래걸린 횟수는 {max(try_list)} 입니다.')
                print("=====게임을 종료합니다.=====")
                break
    elif 0 < try_num > 100:
        print("==== 입력 범위를 확인해 주세요. ====")
    elif try_num > random_number:
        print("==== down 입니다. ====") # random_number 보다 아래 입니다.

    else:
        print("==== up 입니다. ====") # random_num 보다 위 입니다.






