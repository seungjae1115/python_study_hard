height = float(input("당신의 키는 몇 cm입니까? >>> "))/ 100
weight = float(input("당신의 몸무게는 몇 kg입니까? >>> "))1
bmi = round((weight/height**2) , 2)
if bmi >25.00:
    print(f"당신의 bmi지수는 {bmi}이고, 비만입니다.")
elif bmi >23.00 :
        print(f"당신의 bmi지수는 {bmi}이고, 과체중입니다.")
elif bmi > 18.50:
        print(f"당신의 bmi지수는 {bmi}이고,정상입니다.")
else:
    print(f"당신의 bmi지수는 {bmi}이고,저체중입니다.")
