# turtle이라는 모듈을 사용할건데, Turtle, Screen 클래스를 import 할겁니다
from turtle import Turtle, Screen
import random

t = Turtle()        # Turtle 클래스의 객체 생성, 이름은 t
screen = Screen()   # Screen 클래스의 객체 생성
t.shape("turtle")
t.color("white")
screen.bgcolor("black")
t.penup()
t.forward(100)
t.pendown()
t.forward(200)

# for _ in range(10):   # 그냥 반복을 10번 하는 거고 변수를 사용하지 않았기 때문에 _를 썼습니다(i나 n이 아니라)
#     t.penup()
#     t.forward(20)
#     t.pendown()
#     t.forward(20)

# t.left(90)
# t.forward(100)

# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)

# for _ in range(4):
#     t.forward(100)
#     t.left(90)

# for _ in range(3):
#     t.forward(100)
#     t.left(120)


def dotted_line():
    for _ in range(10):
        t.penup()
        t.forward(5)
        t.pendown()
        t.forward(5)


# for _ in range(4):
#    dotted_line(10)
#    t.left(90)
#
# for _ in range(3):
#     dotted_line(10)
#     t.left(120)
#
# for _ in range(5):
#     dotted_line(10)
#     t.left(72)
#
# for _ in range(6):
#     dotted_line(10)
#     t.left(60)

def draw_dotted_figures(num):
    for _ in range(num):
        dotted_line()
        t.left(360/num)

random = random.Random()

colors = [
    "dodger blue",
    "peru",
    "dark khaki",
    "sea green",
    "crimson",
    "cornsilk",
    "pale violet red",
    "dark slate blue",
    "royal blue",
    "papaya whip",
    "khaki",
    "dark sea green",
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
    "tomato",
    "dark olive green",
    "mint cream",
    "sienna",
]

t.speed(20)
# for i in range(3,11,1):   #종료값은 그 전까지 작동
#     t.color(random.choice(colors))
#     draw_dotted_figures(i)

def draw_figures(num):
    if num > 2:
        t.color(random.choice(colors))
        for _ in range(num):
            t.forward(100)
            t.left(360/num)
    else:
        print("도형을 그릴 수 없습니다.")
        return

# draw_figures(2)
#draw_figures(4)
# for i in range(11):
#     draw_figures(i)

# for _ in range(6):
#     t.forward(100)
#     t.left(60)

'''
    .heading():
        거북이가 바라보는 방향을 나타내는 속성으로 도(degree) 단위로 나타남
        
        해당 메서드는 콘솔창에 float 형태로 출력됨
        0도: 동
        90도:북
        180:서
        270:남
    .setheading():
        특정 각도로 회전시키는 메서드
    .circle():
        거북이가 원을 그림
'''
# t.forward(100)
# print(t.heading())
# t.right(90)
# print(t.heading())

# t.circle(100)
# t.color(random.choice(colors))
# t.setheading(10)
# t.circle(100)
# t.color(random.choice(colors))
# t.setheading(t.setheading()+10)
# t.circle(100)

# for _ in range(360//10):
#     t.circle(100)
#     t.color(random.choice(colors))
#     t.setheading(t.heading()+10)


#이상의 네 줄의 코드를 응용하여 draw_spriograph(size_of_gap)로 함수화 하시오

def draw_spriograph(size_of_gap):
    for _ in range(360//size_of_gap):
        t.circle(100)
        t.color(random.choice(colors))
        t.setheading(t.heading()+size_of_gap)
# t.speed(0)
# draw_spriograph(5)







screen.exitonclick()