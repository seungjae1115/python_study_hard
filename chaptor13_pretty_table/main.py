'''
외부 패키지 설치

좌측 상단 메뉴버튼(햄버거) ->file ->setting(설정:ctrl alt s)
좌측 리스트에서 project : 프로젝트명으로 되어있는 부분 클릭
->python interpreter
->좌측상단 + 눌러서 필요한 패키지 검색 및

'''
from prettytable import PrettyTable

from chaptor13_pretty_table.pokemon_data import pokemon_data
from pokemon_data import pokemon_data


table = PrettyTable()
table.field_names = ["번호", "이름", "타입"]
table.add_row(2, "라이츄", "전기")

# for i in range(0,26,1):
#     table.add_row(pokemon_data[i])

print(table)