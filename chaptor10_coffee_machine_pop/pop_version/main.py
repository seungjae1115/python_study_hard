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

# print(MENU["라떼"]["재료"]["우유"])
# # 카푸치노의 가격을 콘솔에 출력하시오
# #에스프레소의 물 양을 콘솔에 출력하시오
#
# print(MENU["카푸치노"]["가격"])
# print(MENU["에스프레소"]["재료"]["물"])

profit = 0
resources = {
    "물":300,
    "우유":200,
    "커피":100,
}
# resources 에서 에스프레소 두 잔을 뽑았을 때, 남는 물, 우유, 커피량 연산하고,
# 그 결과를 콘솔에 출력

resources["물"] -= MENU["에스프레소"]["재료"]["물"]*2
resources["커피"] -=  MENU["에스프레소"]["재료"]["커피"]*2

print(resources)

profit += MENU["에스프레소"]["가격"]*2
print(profit)
