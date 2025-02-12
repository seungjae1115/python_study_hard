#wordlist 내부의 요소들 중 하나를 임의로 선택하기 위해 random 모듈을 도입(import)
'''
사용 예시
'''
# numbers = [1,2,3,4,5]
# chosen_numbers = random.choice(numbers)
# print(chosen_numbers)


# todo - 1 :word_list 에서 단어 하나를 임의적으로 선택하도록 random모듈ㅇㄹ 사용하고,
#  #해당 단어를 chosen_word라는 변수에 담기

#todo-2: 사용자에세 알파벳을 하나 추측해서 입력하라고 요청, 이를 guess 변수에 담으시오
# 그리고 대문자로 입력하는 경우를 방지하기 위해 input 함수 뒤에 .lower를 적용하시오

word_list = ["apple", "banana", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
guess = input("알파벳을 입력하세요. >>> ").lower()
#todo-3 : guess에서 입력한 문자 하나가 chosen_word의 string 문자열 중에 하나의 문자와
# 일치하는지를 반복문을 통해 확인할 수 있도록 프로그램을 작성
# 맞으면 정답 틀리면 오답라이고 출력될 수 잇도록 할것

# for i in range(len(chosen_word)):
#     if guess == chosen_word[i]:
#         print("정답")
#     else:
#         print("오답")

for letter in chosen_word:
     if guess == letter:
         print("정답")
     else:
         print("오답")





