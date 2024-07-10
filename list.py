jaewang = ["이재왕", '27', '010-7383-****']
name = jaewang[0]
age = jaewang[1]
phone = jaewang[2]

print(type(jaewang))
print(name, age, phone)

names = [['강수경', '강혜나', '김민석'], ['20', '21', '22'], ['010-****-****', '010-****-****', '010-****-****']]
print(names[0][0:2])

numbers = [1,2,3,4,5]
result = numbers[2] + numbers[-1]
print(result)

print(len(names[0]))

# 리스트에 요소 추가하기
last = [1,2,3]
last.append(30)
print(last)
last.remove(3)
print(type(last))



