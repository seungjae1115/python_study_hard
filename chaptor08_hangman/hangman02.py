import random

word_list = ["apple", "banana", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

# todo-1: 비어있는 list에 display를 만드시오.
#  chosen_word의 각 문자 개수 마다 "_"를 추가하시오. 예를 들어 chosen_word == "apple"이라면
#  display = ["_", "_", "_", "_", "_"] 이 입력되야함 chosen_word읨 문자 개수만큼
#  "_"가 생김

display = []
# for _ in range(len(chosen_word)):   #변수가 사용되지 않았으므로 i가 아니라 _ 사용함
#     display.append("_")
# print(display)

# 향상된 for문
for letter in chosen_word:
    display.append("_")
print(display)

# todo-2; chosen_word의 각 문자들을 반복시키세요
#  만약 그 위치의 문자가 guess와 일치하면 해당 위치의 display에서 해당 문자를 공개 하세요
#  ex) 사용자가 "P"를 입력했고 chosen_word가 "apple"이라면 display = ["_", "p", "p", "_", "_"]로
#  바뀌어야함

guess = input("알파벳을 입력하세요. >>> ").lower()
for i in range(len(chosen_word)):
    if chosen_word[i]== guess:
        display[i] = guess

print(display)