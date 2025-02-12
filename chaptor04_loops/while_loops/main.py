'''
while: 반복문
    while 다음에 나오는 조건문이 참이려면 이하의 실행문이 반복 실행됨(조건문이 False가 될 때 까지.

형식:
while 조건문:
    실행문
'''
#무한 루프의 개념
# num = 1
# while num1 > 0:
#     print(numi)

'''
그래서 while 반복문을 작성할 때 고려할 점:
    특정한 상황에서 조건식이 False가 될 수 있도록 사전에 미리 지정해줘야함.
    ->아닐 경우 무한루프에 빠짐
'''
#특정 조건에서 반복문이 종료될 수 있도록 하는 예시
'''
if문과의비교: 
    if문의 경우 조건식이 점일 때 실행문이 한번 실행되지만, 
    while문의 경우 조건식이 참일 때 실행문이 "반복"실행되기깨문에
    특정 조건이 맞을 경우와 아닐 경우에 대한 고민이 필요한 편
기본예제

'''
#num3 = 10
#while num3 > 0:
#print(num3)
#num3 -=1

#num3 = 11
#while num3>1:
 #   num3-=1
  #  prit(num3)
'''
중첩 while문: while문 내부에 while문이 나타나는 것

ex)
총 5일 동안 매일 3시간씩 수업을 진행합니다. '매일 1일차 1교시입니다.'
'''
#day = 1
#while day<6:
 #   hour=1
  #  while hour<4:
   #     print(f"{day}일차, {hour}교시입니다.")
    #    hour +=1
    #day +=1
'''
구구단 2단부터 9단까지 출력하는 프로그램
변수명은 dan number로 
'''
# dan = 2
# while dan<10:
#     number =1
#     while number<10:
#         print(f"{dan} X {number} = {dan*number}")
#         number+=1
#     dan +=1

# a=1
# while a<100:
#     print(f" {a} {a+1} {a+2} {a+3} {a+4} {a+5} {a+6} {a+7} {a+8} {a+9}")
#     a+=10

a=1
#모든 편견을 가지고 억지로 코드 작성->반복 100번
while a<101:
    print(a,end=",")
    if a % 10 ==0:
        print()
    a+=1 #마지막에 100 다음에 "," 생김






