'''
chapter14_exception
main

1. 예외 처리의 필요성
    1) 예외 vs. 오류
        예외(exception) : 개발자가 직접 처리할 수 있는 문제
        오류(error) : 개발자가 처리할 수 없는 문제

    2) 예외 처리의 목적 :
        어떤 문제가 발생했을 때 그 문제를 해결해 주는 것이 아니라,
        발생된 문제로 인해 프로그램이 비정상적으로 종료되는 것을 막고,
        사용자에게 발생한 문제에 대해 정보를 전달하기 위함.
'''
# 2 / 0
'''
    2 / 0
    ~~^~~
ZeroDivisionError: division by zero

와 같은 방식으로 프로그램이 정상적으로 종료되지 않으며, 보기에 좋지도 않기 때문에,
예외를 처리하면 좋다.
2. 예외 처리
    1) 고전적인 예외처리
'''
# a = int(input("나누는 수를 입력하세요>>>"))
# b = int(input("나누어 지는 수를 입력하세요 >>>"))
# if a == 0:
#     print("0으로 나눌 수 있습니다.")
# else:
#     print(f"b/a = {b/a}")
'''
어떤 값이든 0으로 나눌 수 없기 때문에 if a ==0을 통해 0으로 나누는 것을 아예 시도할 수 없
도록 예외를 처리함

여기서 생각할 수 있는 잠재적인 문제는 :
1)어떤 문제가 발생할 지 예상할 줄 있어야 미리 대비할 수 있다.
2)어떤 문제가 발생할 지 예상할 수 있더라도 대비할 수 없는 경우가 있다.

4.예외 처리 방식
    1)모든 예외를 처리하는 방식 -> try / except 문
    
    형식:
try:
    코드 작성 영역
except:
    예외 발생시 처리 영역
'''
# try:
#     a = int(input("나누는 수를 입력하세요>>>"))
#     b = int(input("나누어 지는 수를 입력하세요 >>>"))
#     print(f"b/a = {b/a}")
# except:
#     print("예외가 발생했습니다.")
#
# from prettytable import PrettyTable
# table = PrettyTable()
# table.field_names =["순번","예외 클래스","의미"]
# table.add_row(1, "BaseException", "최상위 예외 클래스")
# table.add_row(2, "Exception", "대부분 예외 클래스의 슈퍼 클래스")
# table.add_row(3, "Arithmeticerror", "산술 연산에 문제가 있을 때")
# table.add_row(4,"AttributeError", "잘못된 속성을 참조할 때")
# table.add_row(5, "E0FError", "파일에서 더 이상 읽어 들일 데이터가 없을 때")
# table.add_row(6,"ModuleNotFoundError", "import할 모듈이 없을 때")
# table.add_row(7,"FileNotFoundError", "존재하지 않는 파일일때")
# table.add_row(8,"IndexError", "잘못된 인덱스를 사용할 때")
# table.add_row(9, "NameError", "잘못된 이름(변수)을 사용할 때")
# table.add_row(10, "SyntaxError", "문법이 틀렸을 때")
# table.add_row(11,"TypeError", "계산하려는 데이터의 유형이 잘못되었을 때")
# table.add_row(12, "ValueError", "계산하려는 데이터의 값이 잘못되었을 때")
# print(table)
'''
기본 예제 

다음은 사용자가 입력한 키를 정수로 반올림해서 다시 저장하는 프로그램
try / except 문을 사용하여 "예외가 발생하였습니다"를 출력할 수 있도록 작성
'''
# try:
#     height = input("키를 입력하세요 >>>")   #결과값이 str -> float 사용
#     height=round(height)                      #str을 round처리할 수 없기 때문에 예외 발생
#     print(f"입력하신 키는 {height}cm로 처리됩니다.")
# except:
#     print("예외가 발생합니다.")
'''
        2)특정 예외만 처리하는 방식
            try/except문을 사용하면 기본적으로 예외의 종류에 상관없이 모든 예외가 처리됨.
            하지만 이상에서 본 것처럼 0으로 나누는 경우와, 정수가 아닌 값ㅇㄹ 입력한 경우에
            서로 다른 메시지를 출력한다면, 개발자에세 예외를 처리할 수 있을만한 정보를 
            제공할 수 있음(아까 전까지의 예시는 예외 발생 후에 개발자가 어떤 코드에 문제가 있었는지
            
            2-1) 0으로 나누려고 하는 경우 -> 0으로 나눌 수 없습니다.
            2-2) 정수가 아닌 값을 입력하는 경우 -> 정수만 입력할 수 있습니다.
            로 특정 예외에 따른 서로 다른 안내문을 재시한다고 할 때, 
            except 문 뒤에 처리하고자 하는 예외를 모두 명시하면 됨
'''
# try:
#     a = int(input("나누는 수를 입력하세요>>>"))
#     b= int(input("나누어지는 수를 입력하세요>>>"))
#     print(f"b/a = {b/a}")
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")
# except ValueError:
#     print("정수만 입력할 수 있습니다.")
'''
ZeroDivisionError
ValueError
'''
# try:
#     a = int(float(input("나누는 수(정수만)을 입력하세요>>>")))
#     b = int(float(input("나누어지는 수(정수만)을 입력하세요 >>>)))
#     print(f"b/a = {b / a}")
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")
'''
        거의 모든 예외는 Except
'''
'''
4. 예외메시지 처리하기
    지금까지는 직접 예외 메시지를 만들어서 사용했지만 기본저으로 예외 메시지를 이미 가지고 있는 경우도 있다

try :
    코드 작성 영역
except 예외클래스 as 예외메시지:
    예외 발생 시 처리 영역
'''
# z = [10,20,30,40,50]
#
# try:
#     print(z[10])
# except IndexError as e:
#     print(e)
'''
5. else / finally 문
    tru / except 문에 추가로 else finally 문을 사용할 수 있음
    else: 예외가 발생하지 않으면 처리되는 구문
    finally : 예외발생 여부와 관계없이 맨 마지막에 항상 처리되는 구문
    
형식:
try:
    코드 작성 영역
except:
    예외 발생 시 처리영역
else:
    예외 없음 시 처리 영역
finally:
    언제나 실행되는 영역
    
'''
# try:
#     a = int(input("나누는 수를 입력하세요>>>"))
#     b= int(input("나누어지는 수를 입력하세요>>>"))
#     result = b / a
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# else :
#     print(f"b/a = {result}")
# finally:
#     print("프로그램이 종료되었습니다.")
'''
6.강제로 예외발생시키기
    어떤 ㅏ람이 나이를 정수로 입력 받는 프로그램이 있다고 가정했을 때,
    컴퓨터 상으로는(그리고 파이썬 상으로는) -1000이 정수이기 때문에 예외가 발생하지 않는다.
    하지만 -1000살이 될 수는 없기 때문에 직접 예외를 만들어 
'''
# age = int(input("나이를 입력하세요 >>>"))   #-1000살 입력했을 때 예외 발생 X
# print(f"당신의 나이는 {age}살입니다.")       #파이썬 상에선ㄴ ㄴ문제가 없지만 현실 세계에선 생기는 예외
#
# try:
#     age = int(input("나이를 입력하세요 >>>"))
#     raise Exception("강제로 발생시킨 예외입니다.")   #이 경우 멀쩡한 숫자를 입력해도 예외가 발생
# except Exception as e:
#     print("발생한 예외 메시지ㅡㄴ 다음과 같습니다.")
#     print(e)

'''
7.상용자 정의 예외 클래스

    음수를 입력받을 때 강제로 예외를 발생시키는 예외 클래스를 정의
'''
# class NegavieAgeError(Exception):     #클래스명(부모클래스)-> 상속개념
#     """사용자 정의 예외 클래스 : 나이가 음수일때 발생"""
#     pass   #예외를 발생시키기만 하면 되기 때문에 따로 코드 작성할 필요가 없음
#            #-> Exception 클래스를 상속 받았기 때문에 메서드 사용
# class TooManyAgeError(Exception):
#     pass
# try:
#     age = int(input("나이를 입력하세요 >>>"))
#     if age < 0:
#         raise NegavieAgeError("나이는 음수일 수 없습니다.")
#     elif age > 200:
#         raise TooManyAgeError("불가능한 나이 입력입니다.")
# except NegavieAgeError as e:
#     print("발생한 예외 메시지는 다음과 같습니다.")
#     print(e)
# except TooManyAgeError as e:
#     print("발생한 예외 메시지는 다음과 같습니다.")
#     print(e)
# except ValueError as e:
#     print(e)
# except Exception as e:
#     print(e)
# else:
#     print(f"당신의 나이는 {age}입니다.")
# finally:
#     print("프로그램이 종료되었습니다.")
'''
나이를 200 초과했을 때 '강제로 TooManyAgeError를 발생시키고' '불가능한 나이 입략입니다'를 
출력하는 예외 클래스를 정의하고 이상의 코드에 추가하시오
나이를 실수로 입력했을 때 나타나는 예외를 처리하고 default 에러 메시지를 출력하시오
예상할 수 없는 예외가 발생했을 때 처리하는 예외구문을 작성
else문을 통해 정상적으로 처리되었을때 당신의 나이는 __살 입니다. 가 출력되도록 작성
finally 구문을 통해 프로그램이 종료되었습니다. 가 출력되도록 작성
'''
'''
과제

사용자의 점수를 0 이상 100이하로 입력 받아서 점수가 80점 이상이면 합격 아니면 불합격 출력하는 프로그램 작성
0 이상 100 이하의 유효한 값이 아니면 예외 발생시키고
'점수는 0 이상 100이하입니다'라는 예외 메시지 출력하기 -> 사용자 정의 예외 클래스 정의
ScoreOutOfRangeError 클래스를 정의해서 사용

'''
# class ScoreOutOfRangeError(Exception):
#     """0 미만 100 초과의 점수값이 입려되었을 때 발생하는 Error클래스"""
#     pass
# try:
#     score = int(input("점수를 정수로 입력하세요 >>>"))
#     if score < 0 or score > 100:
#         raise ScoreOutOfRangeError("점수는 0이상 100이하입니다")
#     if score >=80 :
#         print("합격입니다.")
#     else:
#         print("불합격입니다.")
# except ScoreOutOfRangeError as e:
#     print(e)
# except TypeError as e:
#     print("점수는 숫자로 입력해야합니다.")
# except Exception as e:
#     print(e)
# else:
#     if score >=80 :
#         print("합격입니다.")
#     else:
#         print("불합격입니다.")
# finally:
#     print("프로그램이 종료되었습니다.")
'''
사용자로부터 숫자를 입력받아 해당 숫자로 100을 나누는 값을 출력하는 프로그램을 작성하시오
만약 사용자가 0을 입력하거나 숫자가 아닌 값을 입력하면 적절한 예외 메시지를 출력하시오

지시사항
1.사용자로부터 숫자를 입력받음
2.입력 받은 숫자로 100을 나누어 결과를 출력함
3.입력 값이 0일 경우 적절한 예외를 처리하여 '숫자만 입력할 수 있습니다'라는 메시지를 출력
4.입력 값이 숫자가 아닌 경우 적절한 예외를 처리하여 '숫자만 입력할 수 있습니다.' 출력
5.예외가 발생하지 않는 경우 '정상적으로 처리되었습니다.' 출력, 결과 출력
6.프로그램 종료 메시지 출력
'''
# try:
#     num = int(input("숫자를 입력하세요 >>>"))
#     result = 100/ num
# except ZeroDivisionError as e:
#     print("0으로 나눌 수 없습니다.")
# except ValueError as e:
#     print("숫자만 입력할 수 있습니다.")
# else:
#     print("정상적으로 처리되었습니다.")
#     # print(f"100 / {num} = {100/num}") #else로 넘어와서 0으로 연산을 하려고 하면 예외 발생함
#     print(f"100/{num} = {result}")      #이상을 이유로 result 라는 중간단계를 거쳐 작성함
# finally:
#     print("프로그램이 종료되었습니다.")

'''
사용자로부터 리스트의 인덱스를 입력 받아 해당 인덱스의 값을 출력하는 프로그램을 작성
만약 잘못된 인덱스를 립력하면 적절한 예외 메시지를 출력하시오

지시사항 
1.미리 정의된 리스트가 있다
2.사용자로부터 리스트의 인덱스를 입력 받음
3.입력 받은 인덱스를 사용하여 리스트의 값을 출력
4.인덱스가 리스트의 범위를 벗어나면 적절한 메시지를 출력함
5.사람을 의심하고 예상되는 예외를 작성
6.예외가 발생하지 않는 경우  "정상적으로 처리되었습니다"라는 메시지와 함께 해당 인덱스의 값을 출력한다
7.프로그램 종료 메시지 출력
8.마이너스 인덱스는 적용시키지 않는다.-> 사용자 정의 예외 클래스를 통해서 적용함
        ->NegativeNumIndexError라고 이름 짓고 처리
'''
# class NegativeNumIndexError(Exception):
#     """마이너스 인덱스를 입력했을 때 오류"""
#     pass
# my_list = [10, 20, 30, 40, 50]
# try:
#     index_num = int(input("인덱스 넘버를 입력하세요.>>>"))
#     if index_num < 0:
#         raise NegativeNumIndexError("마이너스 인덱스는 적용하지 않습니다.")
#     chosen_element = my_list[index_num]
# except NegativeNumIndexError as e:
#     print(e)
# except ValueError as e:
#     print("정수만 입력할 수 있습니다.")
#     print(e)
# except IndexError as e:
#     print("list의 범위를 벗어났습니다.")
# except TypeError as e:
#     print("자료형이 잘못되었습니다.")
# except Exception as e:
#     print("예측할 수 없는 예외가 발생하였습니다.")
#     print(e)
# else:
#     print(f"{index_num} 위치에 있는 값은 {chosen_element}입니다.")
# finally:
#     print("프로그램이 종료되었습니다.")

'''
사용자로부터 솟성명을 입려 받아 객체의 해당 속성을 출력하는 프로그램을 작성하시오
만약 사용자가 잘못된 속성을 입략하면 적절한 예외 처리 메시지를 출력하시오

지시사항

1.미리 정의된 클래스와 객체가 있다.
2.사용자로부터 속성명을 입력받는다.
3.입력받은 '속성명'을 사용하여 객체의 '속성값'을 출력한다.
4.잘못된 속성명을 입력하면 '존재하지 않는 속성입니다.'라는 메시지를 출력한다.
5.예외가 발생하지 않은 경우 '정상적으로 처리되었습니다'ㅎ는 메시지와 속성값을 출력함
6.프로그램 종료 메시지
'''
#클래스정의
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
#객체 생성
person1 = Person(name ="Jhon", age=30)     #keyword argument로 객체 생성
#풀이법1
# try:
#     attribute = input("출력할 속성명을 입력하세요.>>>")
# except AttributeError as e:
#     print("존재하지 않는 속성명입니다.")
#     print(e)
# except Exception as e:
#     print("예측할 수 없는 예외가 발생하였습니다.")
#     print(e)
# else:
#     print("정상적으로 처리되었습니다.")
#     print(getattr(person1, attribute))
# finally:
#     print("프로그램이 종료되었습니다.")
'''
getattr(객체명, 속성명->대입된 애가 들어가야함) 함수:
이상의 코드를 예시로 생각했을 때 
Person 클래스 내부에 있는 인스턴스 변수명을 그대로 집어넣는 것은 불가능하고 
input을 통해서 받은 str 데이터를 대입했을 때 가능

vars(객체명): 객체의 속성명 - 값을 dictionary의 키 - 값 쌍으로 만들어주는 함수
'''
#객체를 dictionary로 변환
profile = vars(person1)
try:
    attribute2 = input("출력할 속성명을 입력하세요.>>>")
    # for key in profile:      #딕셔너리에서 반복문 돌리면 key만 튀어나옴
    #     print(key)           #value를 조회하기 위해서느 추가적으로 작성해야함
    #     print(profile[key])
    if attribute2 in profile:   #profile의 key 중에 attribute2와 일치하는 것이 있는짐 둗는 조건문
        print("정상 출력이 가능합니다.")
    else:
        raise KeyError
except KeyError as e:
    print(e)
    print("존재하지 않는 속성입니다.")
except Exception as e:
    print(e)
    print("예측할 수 없는 예외가 발생하였습니다.")
else:
    print(f"{attribute2}의 속성값은 : {profile[attribute2]}입니다.")
finally:
    print("프로그램이 종료되었습니다.")










