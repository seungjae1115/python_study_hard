'''
if 문
if문은 조건이 참일 떼만 해당 블록의 코드를 실행합니다.
'''
# age= 20
# if age >= 19:
#     print("성인입니다.")   #if와 함께있는 조건문이 true 일때만 7번 라인이 실행됩니다.
'''
    if 문에서 주의할 점:
    1) if와 같은 라인에 작성된 코드는 true/false으로 구분할 수 있어야만함
    2)if와 같은 라인에 있는 조건문이 끝났을 때 콜론(:)으로 마무리
    3)파잇선에서는 타 언어들과 달리 들여쓰기(indented writing)이 "매우" 중요
    5-6에 해당하는 코드를 Java로 작성한다면
    if(age >=19) {
    System.out.println("성인입니다.");
    }
2. if-else 문 
   if문 다음에  else를 사용할 수 있는데 , if가 참이 때 실행한다면, else는 거짓일 때 실행됨.
'''
age = 3
if age>=19:
    print("성인입니다.")
else:
    print("미성년자입니다.")
'''
    이상의 코드에서 확인할 수 있는 것은 20번 라인의 print()는 if절에,
    22번 라인의 print()는 else절에 종송되있음을 들여쓰기를 통해 알 수 있다. 
    
    if-else는 서로 반대이기때문에 else절에는 굳이 조건식을 명시하지 않습니다.
3. if-else - elseams(타 언어에서는 else if) 
   여러 조건을 동시에 검사하기 웨해서 사용하는 구조 
'''
# age = 14
# if age >= 19:
#     print("성인입니다.")
# elif age >= 8:
#     print("학생입니다.")
# else:
#     print("미취학 아동입니다.")
'''
    이상의 코드에서 확인할 수 있는 점
    1)첫 번째 조건은 False 이지만,
    2)두 번째 조건은 True 이므로 37라인이 실행됨
    3)이후 조건은 확인하지 않고 조건문 전체가 종료됨
    
    if 조건문의 전체 형식:
  if 조건식1:
     실행문1
     (elif 조건식2:)  -> optional
        (실행문2)
     (elif 조건식3:)  ->선택적
        (실행문3)
     (else:)         -> optional
        (실행문4)
        
4.중첩 if문(nested if)
  조건문 내부에 또 다른 조건문을 사용할 수 있음. 다만 가독성이 떨어지는 편이라서
  추후에 배우는 논리연산자와 함께 사용하는 편
'''
age = 18
has_ticket = False

if age >= 19:
        #if 내부에 다시 if문 작성 ->중첩 if문
        if has_ticket:
            print("영화관 입장이 가능합니다.")
        else:
            print("티켓을 구매하세요.")
else:
    print("미성년자는 출입할 수 없습니다.")
'''
5. 조건문에서 자주 쓰이는 연산자
비교 연산자:
        1) == : 같다
        2)!= : 같지 않다
        3)>
        4)<
        5)>=
        6)<=
논리연산자
1)and : a and b  a와 b가 모두 참일 때 실행문 실행 
2)OR : a or b a 혹은 b 중에 하나가 참이면 실행문 실행
3)not : if not A A가 false일 때 실행문 실행
'''
age = 25
has_ticket = True

#논리연산자를 사용한 중첩 if문의 축약
if age >= 19 and has_ticket:
    print("영화관 입장이 가능합니다.")
else:
    print("입장할 수 없습니다.")
