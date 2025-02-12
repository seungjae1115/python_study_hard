#age = input("당신의 나이는 몇 살입닉가? >>>")
#print(type(age))
#print(f"단신은 내년에 {age+1}살이 됩니다.") -> 오류 발생
'''
input() 함수의 결과값은 언제나 str입니다. -> 즉, 수학 연산을 하기 위해서는 
별도의 과정이 필요합니다.

이때 필요한 함수가 '형변환 함수'입니다.(conversion)
'''
#age1 = input("당신의 나이는 몇살입니까? >>> ")
#print(type(age1))  #결과값 str
#age1_int = int(age1)  # str인 age1을 int로 자료형을 변환시켜서
                      #age1_int라는 새로운 변수에 대입
#print(type(age_int))
#print(f"당신으ㄴ 내년에 {age1_int+1}살이 됩니다.") #여기서는 오류 발생 X
'''
자주 쓰이는 형변환 함수
1. int() -> str 또는 float을 int로 변경-> 소수의 경우 버림
2.float() -> str 또는 int로 변경 -> 정수의 경우 .0 붙여줌
3. round()-> 반올림 해주는 함수 
'''
# temp = int(3.8)
# print(temp)
# temp2 = float(4)
# print(temp2)
#
#temp3= round(3.8)

'''
bmi 계산기를 작성하기

1. 키(cm)를 이1력 받아 (input()를 쓰라는 의미) 변수 height에 저장 
2. 몸무게 (kg)을 입ㄹ력받아 weight에 저장
3. 몸무게/ 키(m)의 제곱)을 계산하면 bmi 지수가 나옴
4.bmi 지수를 int로 출력하세요 ->int 함수 사용하라는 의미 
5.bmi 지수를 소수점 셋째자리에서 반올림하여 둘째자릭가지 출력하기 -> round 함수 쓰기
'''
#weight = input(f"당신의 몸무게는 몇 kg입니까? >>>")
#weight = float(weight)
#height = input(f" 당신의 키는 몇 cm입니까? >>>")
#height = float(height)
#height = (height / 100)
#bmi = weight / (height**2)
#bmi_int = int(bmi)
#bmi_round = round(bmi, 2)
#print(f"당신의 bmi지수는 {bmi_int}입니다.")
#print(f"당신의 bmi 지수는 {bmi_round}입니다.")

height = float(input("당신의 키는 몇 cm입니까? >>> "))/ 100
weight = float(input("당신의 몸무게는 몇 kg입니까? >>> "))
print(f"당신의 bmi지수는 {int(weight/(height**2))}입니다")
print(f"당신의 bmi지수는 {round(weight/height**2) , 2}입니다.")

