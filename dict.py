#사용자가 키를 입력하면 밸류 프린트

dictionary = {"야구": "LG 트윈스 짱", "농구": "전자랜드 짱", "배구":"한국전력 짱", "씨름":"의성군청 짱"}

# list
print("<수진이의 스포츠 세상>")
print("야구")
print("농구")
print("배구")
print("씨름")

command = input("이 중에 수진이가 좋아하는 스포츠는?")

if command in dictionary:
    print(dictionary[command])
else: 
    print("목록에 있는 단어를 입력해주세요")