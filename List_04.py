# 리스트의 탐색과 삭제
# 탐색

heros = ["아이언맨","토르","헐크","스칼렛","토르"]
n = heros.index("헐크")
print(n)

# 삭제

heros = ["아이언맨","토르","헐크"]
h = heros.pop(1)    # 인덱스
print(heros)

heros = ["아이언맨","토르","헐크"]
h = heros.remove("토르")  #데이터
print(heros)