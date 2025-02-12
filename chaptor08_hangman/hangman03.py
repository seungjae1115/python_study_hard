import random #특정 모듈을 사용한다는 것을 맨 처음에 명시

'''
"".join(반복가능객체)method : . 앞에 문자열을 기준으로 반복가능 객체으로
요소들을 합쳐서 str으로 변환
'''
# temp = ["안", "녕", "하", "세", "요"]
# hello = "".join(temp)
# print(hello)
# print("/".join(temp))
# print(" ".join(temp))

word_list = ["apple", "banana", "camel"]
chosen_word = random.choice(word_list)

display = []
# todo-1:"_"가 적용된 display를 구현
# todo-2: 사용자가 추측을 반복할 수 있도록 while 반복문을 작성하세요
#  즉, display에선 더이상 "_"가 없을 때 반복문이 멈출 수 있도록 작성.
#  반복문 종료 후 print("정답입니다.")를 출력하도록 작성



for letter in chosen_word:
    display.append("_")
print(display)

while "_" in display:
    guess = input("알파벳을 입력하세요. >>> ").lower()

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    print(display)
print(" ".join(display))
print("정답입니다!")

