'''
클래스 도입의 필요성
'''
from xmlrpc.client import Boolean


# 매개 변수가 6개면 함수를 하나 정의합니다.
def student_info(name, department, professor, phone, address, grade):
    print(name)
    print(department)
    print(professor)
    print(phone)
    print(address)
    print(grade)

name1 = "윤승민"
department1 = "대학생"
professor1 = "David"
phone1 = "010-2345-6789"
address1 = "부산광역시 해운대구"
grade1 = "A"

#함수호출
student_info(name1, department1, professor1, phone1, address1, grade1)
'''
지금까지 배운 함수와 매개변수, 그리고 argument를 통해 6개의 변수를 처리함. 하지만
만들어야 할 변수의 개수가 많고, 학생 한 명당 매개변수가 6개라면 학생이 100명일 경우 600개의 
변수를 처리할 필요가 있음
'''
student_info(grade="B",
             address="서울특별시 성동구",
             phone="010-1234-5678",
             professor="Jhon",
             department="computer science",
             name="김일"
             )                       #keyword argument

#name2, ... grade2 라는 변수들을 선언하고 거기에 여러분들의 정보를 입력하 뒤
#keyword argument를 통해서 student_info()를 설정하고 호출

name2 = "윤승재"
department2 = "대학생"
professor2 = "Jake"
phone2 = "010-4395-1454"
address2 = "부산광역시 해운대구"
grade2 = "A+"

student_info(name = name2, department=department2, professor=professor2, phone=phone2, address=address2, grade=grade2)

'''
ㅅ이상의 상황들(볌수에 각각 데이터를 대입한 후에 함수의 argument로 사용하거나 혹은 데이터를 직접 argument에 등록)을
벗어나기 위해 클래스와 객체 개념을 도이

class란?: 객체를 만드는 도구 - 솔계도/툴/청사진
    
    자동차 설계도 -> 클래스
    설계도를 통해 생성된 자동차들 -> 객체
    
    같은 설계도로 만든 자동차라 하더라도 서로 다른 옵션을 가질 수 있음
    마찬가지로 같은 클래스로 만든 객체라 해도 서로 다른 값을 가질 수 있음
    
    인스턴스(instance) 역시 클래스를 이용해서 생성한 갯체를 가리키는 용ㅇ어
    객체와 인스턴스는 그 둘을 바라보는 관점의 차이로 볼 수 있음
    
    1.'자동차 설계도'를 만든 자동차는 객체(object)
    2. 자동차는 자동차 설계도의 인스턴스(instance)입니다. 
    
1. class 정의
 클래스를 작성하는 것을 클래스 정의라고 한다. -> 함수 정의를 생각하면 됨
 
 형식: 
 
 class 클래스면(대문자로 시작):
    본문
--------------------------------
객체지향형식:                  ->함수호출과 유사

객체 이름 = 클래스명()
'''
#클래스 정의 형식 예시
class WaffleMachine:    #클래스명은 대문자로 시작하고 Pascal case로 표기함 python에서 변수는 snke_case
      pass                  #나중에 코드를 작성하겠다는 의미로 이 경우 실행시켜ㅗ 오류가 나지 않음

#객체 생성 예시
waffle = WaffleMachine()
print(waffle)
'''
print(waffle)을 실행시켰을 때 <__main__.WaffleMachine object at 0x0000016B62367E00> 에서 object라고 
표기된 점을 미루어 waffle은 WaffleMachine의 객체임을 확인

클래스의 구성

1.클래스의 기본 구성 
    객체를 만들어내는 클래스는 객체가 가져야할 구성 요소를 지님
    객체를 갱성하기 위해서는 클래스는 객체가 가져야할 '값'과 '기능'을 가져야함
    \클래스를 구성하는 변수는 두 가지로 구분됨
    1)클래스 변수: 클래스를 기반으로 생성된 모든 인스턴스들이 공유하는 변수
    2)인스턴수 변쉬 인스턴스 들이 개별적으로 가지는 변수
    
    메서드는 특징에 따라서
     1)클래스 메서드
     2)정적 메서드
     3)인스턴스메서드
     
     인스턴스 변수: 클래스를 기반으로 만들어지는 모든 인스턴스들이 각각 따로 조=저장하는 변수를 의미
                모든 인스턴스 변수는 self라는 키워드를 앞에 붙여줌
     인슽턴스 메서드 : 인스턴스 변수를 사용하는 메서드
                 인스턴스 변수값에 따라서 각 인스턴스마다 다르게 동작함
                 인스턴스 메서드는 첫 번째 매개변수로 self를 추가해야함
'''
#클래스 정의
class Person:
    # chaptor06 fuctions 부분 침조하는데->call2()
    def set_info(self, name, age, tel, address):           #클래스 내부에 def를 사용하면 method로 정의됨.
        self.name = name
        self.age = age
        self.tel = tel
        self.address = address     #self는 인스턴스 메서드에 항상 있어야 하는 것으로
                                   # 아직 인ㅅ턴스를 생성하지 않았기 때문에 인스턴스 이름이 없음
                                   # 추후에 인스턴스를 생성하게 되면 인스턴스명.name 등으로 치환됨
    #call1() / 매개변수 없음 return없음
    def display_info(self):
        print(f"이름 : {self.name}")
        print(f"나이 : {self.age}")
        print(f"연락처 : {self.tel}")
        print(f"주소 : {self.address}")

    #call3() / 매개변수 없음 return 있음
    def display_info2(self):
        return f"제 이름은 {self.name}이고, {self.age}살입니다.\n 연락처는 {self.tel}인데, {self.address}에 살고 있습니다."

#객체 생성
# person01 = Person()
# print(person01)           #객체명을 그대로 출력할 수 없음 -> 주소값만 출력
# person01.set_info("안근수", 38, "010-7445-7113", "부산광역시 연제구")
# person01.display_info()   # 클래스에서 정의한 method사용 ->메서드 호출 방식: 객체명.메서드명()

#person02 객채를 생성하시고, person02.set.info()를 활용하여 여러분 이름 나이 연락처 주소를 입력하고
#display.info02()(call3()유형으로 작성)를 정의하여 다음 실행 예와 같이 출력되도록 작성하시오
#실행예
#제 이름은 ___이고, __살 입니다.
#연락처는 _____이고, ____에 살고 있습니다.
#코드 실행
#print(person02.display_info02())

# person02 =Person()
# person02.set_info("윤승재", 21, "010-4395-1454", "부산광역시 해운대구")
# person02.display_info()
# print(person02.display_info())

'''
응용 예제 

다음 지시사항을 읽고 책 제목과 저자 정보를 저장할 수 있는 Book클래스를 생성하세요 -> 객체도 생성하고, 실행 예를 구현하세요
1. 다음과 같은 방법으로 book1과 book2 인스턴스를 생성하세요.

book1 = Book()
book2 = Book()

2. set_info(self, title, author)를 통해 책 제목을 입력하세요.

3.display_info()를 통해 실행 예와 같이 출력되도록 작성하세요

실행 예
책 제목: 파이썬
책 저자: 민경태
책 제목: 어린왕자
첵 저자: 생텍 쥐페리 
'''
# class Book:
#     #여러분들은 클래스 내부에 method들을 정의해야함
#     def set_info(self, title, author, stock):
#         self.title = title
#         self.author = author
#         self.stock = stock
#
#     def display_info(self):
#         print(f"제목 : {self.title}")
#         print(f"저자 : {self.author}")
#
# book1 = Book()
# book2 = Book()
#어떤 method를 사용해서 속성에 값을 대입하고, 어떤 method를 사용하여 정보를 출력할지 코드를 작성해야함

# book1.set_info("파이썬", "민겅태", 3)
# book2.set_info("어린왕자", "생텍 쥐페리", 10)
#
# book1.display_info()
# book2.display_info()
#
# #특정 개체의 속성값을 확인하는 방법 -> 객체명.속성명
# print(book1.title)
# #그러면 속성값만 꺼내는 이유
# print(book1.stock + 2)
