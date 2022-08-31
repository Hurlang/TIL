# 1
# word = 'ssafy'
# print(word)
# print(id(word)) # 2570962748464
# word = 'test'
# print(word)
# print(id(word)) # 2570957840176

# # 2
# print('apple'.find('p')) # 있으면 찾는 문자의 가장 왼쪽순서 인덱스를 반환
# print('apple'.find('k')) # 없으면 -1 반환
# print('apple'.index('k')) # 없는 문자이면 에러발생 ValueError: substring not found

# # 3
# print('abc'.isalpha()) # True
# print('ㄱㄴㄷ'.isalpha()) # True
# print('123'.isalpha()) # False

# print('Ab'.isupper()) # False

# # 4
# print('a,b,c'.split(',')) # ['a', 'b', 'c']
# print('a b c'.split()) # ['a', 'b', 'c']

# # 5
# msg = 'hI! Everyone, I\'m ssafy'

# print(msg) # hI! Everyone, I'm ssafy
# print(msg.capitalize()) # Hi! everyone, i'm ssafy
# print(msg.title()) # Hi! everyone, i'm ssafy
# print(msg.upper()) # HI! EVERYONE, I'M SSAFY
# print(msg.lower()) # hi! everyone, i'm ssafy
# print(msg.swapcase()) # Hi! eVERYONE, i'M SSAFY

# # 6
# print('*'.join('ssafy')) # s*s*a*f*y
# print(' '.join(['3','5','8','9'])) # 3 5 8 9

# # 7
# a = {'사과','바나나'}
# print(a.add('수박'))
# a.add('수박')
# print(a)

# # 8
# a = {'사과', '바나나', '수박'}
# b = {'포도', '망고'}
# c = {'사과', '포도', '망고', '수박', '바나나'}

# print(a.isdisjoint(b)) # True a와 b는 서로소인가?
# print(b.issubset(c)) # True b가 c의 하위셋인가?
# print(a.issuperset(c)) # False a가 c의 상위셋인가?

# # 9
# dic = {
#     'hi':1,
#     'hi':2
# }
# print(dic)
# dic['hi'] = 3
# print(dic) 

# # 10
# import copy
# a = [1, 2, ['a', 'b']]
# b = copy.deepcopy(a)
# b[2][0] = 'c'
# print(a, b) # [1, 2, ['a', 'b']] [1, 2, ['c', 'b']]