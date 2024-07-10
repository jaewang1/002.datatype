# 인풋함수를 통해서 사용자 이름을 입력 받는다.
name = input("이름을 입력하세요.: ")
age = input("나이를 입력하세요.: ")
email = input("이메일 주소를 입력하세요.: ")
phone = input("연락처를 입력하세요.: ")

dic = {name: {'나이': age, '이메일 주소': email, '연락처': phone}}
print(dic)


exchange = {'달러': 1320, '엔화': 950, '위안': 182}
chul = [13, 200, 13]

total = (exchange['달러'] * chul[0] + exchange['엔화'] * chul[1] + exchange['위안'] * chul[2])
print('가지고 계신 돈은 ', total, '원 입니다.')

