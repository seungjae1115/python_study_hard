from random import choice

MENU ={
    "에스프레소":{
        "재료":{
            "물": 50,
            "커피": 18,
        },
        "가격": 1.5,
    },
    "라떼": {
        "재료": {
            "물":200,
            "우유":150,
            "커피":24,
        },
        "가격":2.5,
    },
"카푸치노": {
    "재료": {
        "물": 250,
        "우유":100,
        "커피":24,
        },
        "가격": 3.0,
    }
}

profit = 0
resources = {
    "물":300,
    "우유":200,
    "커피":100,
}
logo = '''
 '/¯¯¯/|¯¯¯|'‚       '|\¯¯¯\  °   |¯¯¯¯¯¯¯¯|  |¯¯¯¯¯¯¯¯|  
 |    °| |___|'‚  '/¯¯¯/\     \     |       ____|  |       ____|  
 |    °| |     |'   |     '|_|    °|'‚   |       ¯¯| '°|  |       ¯¯¯| |  
 |    °| |¯¯¯| ° |     '|¯|    °|'‚   |      '|¯¯|¸¸'|  |       ¯¯¯¯|  
 |\__¸'\|___| ° |\___\_\___\‚  |__¸¸¸|__|   ° |________|  
 | |     ||     |   | |     |  |      |  |      '|'         |              |  
°'\|__¸'||__¸'|  °'\|___|'°|__¸¸'|  |__¸¸¸|'         |________|  
'''
# print(MENU["라떼"]["재료"]["우유"])
# # 카푸치노의 가격을 콘솔에 출력하시오
# #에스프레소의 물 양을 콘솔에 출력하시오
#
# print(MENU["카푸치노"]["가격"])
# print(MENU["에스프레소"]["재료"]["물"])


# resources 에서 에스프레소 두 잔을 뽑았을 때, 남는 물, 우유, 커피량 연산하고,
# 그 결과를 콘솔에 출력

# resources["물"] -= MENU["에스프레소"]["재료"]["물"]*2
# resources["커피"] -=  MENU["에스프레소"]["재료"]["커피"]*2
#
# print(resources)
#
# profit += MENU["에스프레소"]["가격"]*2
# print(profit)


#off라고 입력되면 종료
#report 라고 입력되면 resources와 profit을 참조하여 manual과 같은 방식으로 출력할 것
#잘못 입력했을 경우 잘못 입력하셨습니다 라는 안내문이 출력될 것

#choice가 라떼라는 str데이터라면, 라떼를 만드는데 필요한 재료를 조회하는 방법은 무엇일까?

#함수 정의
def is_resources_enough(order_ingredients):
    """DocString : 함수/클래스.메서드 가 어떤 작동하는지 '사람들에게' 설명해주는 기능
    주문 받은 음료를 resources에서 재료 차감을 하고 난 후, 음료 만들기가 가능하면
    True반환, 아니면 False 반환
    :param : order_ingredients
    :return : True / False"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"죄송합니다. {item}이(가) 부족합니다.")
            return  False
        return True    #else 인쓴 이유: if문이 실행 안됐으면 어차피 True라서.
def process_coins():
    """동전들을 입력 받아 전채 금액을 반환하는 함수 call3()유형"""
    #쿼터, 다임, 니켈, 페니 네 종류의 동전
    #쿼터 = 0.25 달러
    #다임 = 0.1 달러
    #니켈 = 0.05 달러
    #페니 = 0.01 달러
    #quarters, dimes, nickels, pennies
    # quarters = int(input("쿼터 동전을 몇 개 넣으시겠습니까? >>> ")) * 0.25
    # dimes = int(input("다임 동전을 몇 개 넣으시겠습니까? >>> ")) * 0.1
    # nickels = int(input("니켈 동전을 몇 개 넣으시겠습니까? >>> ")) * 0.05
    # pennies = int(input("페니 동전을 몇 개 넣으시겠습니까? >>> ")) * 0.01

    # return quarters + dimes + nickels + pennies
    # 축약 버전 -> 지역변수가 너무 많아서

    total = 0.0
    total += int(input("쿼터 동전을 몇 개 넣으시겠습니까? >>>"))*0.25
    total += int(input("다임 동전을 몇 개 넣으시겠습니까? >>> ")) * 0.1
    total += int(input("니켈 동전을 몇 개 넣으시겠습니까? >>> ")) * 0.05
    total += int(input("페니 동전을 몇 개 넣으시겠습니까? >>> ")) * 0.01

    return total

#들어온 동전 금액과 가격을 비교하는 함수를 정의
def is_transaction_successful(money_received, drink_cost):
    """process_coins()의 결과값과 음료 가격을 매개변수로 받아
    동전이 가격보다 높으면 True / 아니면 False 반환
    그리고 True면 profit에 음료 가격만큼 추가해줘야함"""

    charge = money_received-drink_cost
    if charge >= 0:
        #profit에 돈 추가해야합니다. -> drink_cost만큼. profit->전역변수
        global profit
        profit += drink_cost
        print(f"잔돈 ${charge}를 반환합니다.")
        return True
    else:
        print(f"동전이 충분하지 않습니다. 금액을 ${money_received}를 반환합니다.")
        return False

def make_coffee(drink_name, order_ingredients):
    """resources에 있는 재료에서 MENU["음료이름"]["재료"]들을 차감함.
    -> 차감은 무조건 이루어짐 음료 나오는 안내문 작성"""
    for item in order_ingredients:   #resources를 반복 돌리지 않는 이유는 drink_name이
        resources[item] -= order_ingredients[item]  #에스프레소일 때 오류발생하기 때문
    print(f"{drink_name}가 나왔습니다. 맛있게 드세요!")

is_on = True
print(logo)
while is_on:
    choice = input("어떤 음료를 드시겠습니까? 에스프레소/라떼/카푸치노 >>>")
    if choice == "off":
        is_on = False
        print("자판기가 종료되었습니다.")

    elif choice == "report":
        print(f"물 : {resources["물"]}ml \n우유 : {resources["우유"]}ml \n커피 : {resources["커피"]}g")
        print(f"돈 : ${profit}")

        #자판기에 메뉴명을 정확히 입력했을 시 처리과정
        #1.자원이 충분한지 확인해서 T/F
        #2.T라면 돈을 받아서 계산->해당 금액의 가격보다 높은지 확인해서 T/F반환
        #3.T라면 음료를 만들어주는데, resources dict에 있는 수량을 감소 / 음료 가격만큼 +시켜줘야함
    elif choice in MENU:
        drink = MENU[choice]
        if is_resources_enough(drink["재료"]):
            #이상의 조건식이 T라면 2.단계로 넘어가야함.
            money_received = process_coins()  #함수 호출한 결과값을 변수에 대입
            if is_transaction_successful(money_received,drink["가격"]):
                #재료를 차감하고 음료 만들어서 사용자에게 제공
                #재료 차감부분을 is_resources_enough()함수를 참조하여 작성
                #여기에 작성하고 추후에 함수화시킬 예정
                #기본적으로 dict의 value를 뽑아내서 차감해야함
                # resources["물"] -= drink["재료"]["물"]
                # resources["우유"] -= drink["재료"]["우유"]
                # resources["커피"] -= drink["재료"]["커피"]
                # print(f"{choice}가 나왔습니다. 맛있게 드세요!")
                make_coffee(choice,drink["재료"])

    else:
        print("잘못 입력하셨습니다. 다시 입력하세요")
