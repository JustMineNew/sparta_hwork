import random

random_hand = random.choice(['가위','바위','보'])
print(random_hand)

win_count = 0
lose_count = 0
draw_count = 0
# 무한루프로 들어가는 재귀함수?
# def regame():
#     choise = input(f'다시 도전하실래요? Y/N 중 입력해주세요 = ')
#     while True:
#         if choise == 'y':
#
#             while True:
#
#                 user = input('가위,바위,보 중 선택 하세요 = ')
#                 if user > random_hand:
#                     print('승리')
#                 elif user < random_hand:
#                     print('패배')
#                 else:
#                     print('무승부')
#                 regame()
#                 #break
#         elif choise == 'n':
#             print('게임을 종료합니다.')
#             break
#         else:
#             print('y/n 둘중 입력해 주세요')
#             regame()

while True :
    user = input('가위,바위,보 중 선택 하세요 = ')
    if (user == '가위' and random_hand == '보') or (user == '보'and random_hand == '바위') or (user == '바위'and random_hand == '가위'):
        print('승리')
        win_count += 1
        print(f'승 : {win_count} 무 : {draw_count} 패 : {lose_count}')
        choise = input(f'다시 도전하실래요? Y/N 중 입력해주세요 = ')
        if choise == 'n':
            print('게임을 종료합니다.')
            break
    elif (user == '가위' and random_hand == '바위') or (user == '바위' and random_hand == '보') or (user == '보'and random_hand == '가위'):
        print('패배')
        lose_count += 1
        print(f'승 : {win_count} 무 : {draw_count} 패 : {lose_count}')
        choise = input(f'다시 도전하실래요? Y/N 중 입력해주세요 = ')
        if choise == 'n':
            print('게임을 종료합니다.')
            break
    elif user == random_hand:
        print('무승부')
        draw_count += 1
        print(f'승 : {win_count} 무 : {draw_count} 패 : {lose_count}')
        choise = input(f'다시 도전하실래요? Y/N 중 입력해주세요 = ')
        if choise == 'n':
            print('게임을 종료합니다.')
            break
    else:
        print("정확하게 입력해주세요")
    #break 여기 있으면 30 한번 돌고 끝남



# import random
#
# random_hand = random.choice(['가위','바위','보'])
# print(random_hand)
#
# def regame():
#     choise = input(f'다시 도전하실래요? y/n 중 입력해주세요 = ')    # print(f'다시 도전하실래요? y/n 중 입력해주세요 = {input('')} ') 입력시 print 보다 input 이 먼저 출력
#     while True:
#         if choise == 'y':
#             import random
#             random_hand = random.choice(['가위','바위','보'])
#             while True:
#                 rule = ('가위' < '바위'), ('바위' < '보'), ('보' < '가위')  # 얘는 def 로 while true 를 정의 하는 순간 부터 동작 안되는 듯?
#                 user = input('가위,바위,보 중 선택 하세요 = ')
#                 if user > random_hand:
#                     print('승리')
#                     regame()
#                 elif user < random_hand:
#                     print('패배')
#                     regame()
#                 else:
#                     print('무승부')
#                     regame()
#                 #break
#         elif choise == 'n':
#             print('게임을 종료합니다.')
#             break
#         else:
#             print('y/n 둘중 입력해 주세요')
#             regame()
#
#
#
# while True:
#     rule = ('가위' < '바위'),('바위' < '보'),('보' < '가위')    # 얘는 def 로 while true 를 정의 하는 순간 부터 동작 안되는 듯?
#     user = input('가위,바위,보 중 선택 하세요 = ')
#     if user > random_hand:
#         print ('승리')
#         regame()
#     elif user < random_hand:
#         print ('패배')
#         regame()
#     else:
#         print ('무승부')
#         regame()
#     break
#
#
#
# # 문제점
# # 1. 34 line def로 정의시 rule을 어느 위치에 놔도 동작이 안댐
# # 2. 위와 동일하게 정의시 input도 동작 안댐
# # 3. 게임 시작 - 승부결정 나옴 - 다시도전 출력 - y/n 출력 - n 입력시 게임을 종료합니다 까지 출력은 ok 근데 게임이 다시시작함
# # //// 3 -- 24 line 에 break 를 지우니 멈춤 = while 문에 break는 하나면 된다???#












