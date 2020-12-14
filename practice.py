print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(3*(3+1))

print('풍선')
print("나비")
print("z"*5)


print(5<10)
print(not True)


print(not(5<2))

#애완 동물을 소개해 주세요~
print("우리집 개이름은 연탄, 4살, 산책 좋아함, 어른")
animal = "강아지"
name = "연탄"
age = 4
hobby = "산책"
is_adult = age>=3

print("우리짐 "+animal +"의 이름은" +name)
print(name +"는" +str(age)+"살입니다.")
print (name,"는",age,"살입니다.")#윗문장과 같은의미고 str없이도 쓸수 있는데, 여기서, 는 띄어쓰기를 의미한다. 
print(name +" 는 어른일까요?" + (str)(is_adult))

'''주석처리'''

station = "사당"
print(station+"행 열차가 들어오고 있습니다.")

print(1+1)
print(2**3)#**는 제곱이다. 
print(5//3)#몫을 구하기
print(10>3)
print(4<=7)
print(3==5)
print(3+5==8)
print(1!=4)
print(not(1!=3))
print((3>0)and(3<5))
print((3>0)&(3<5))
print((3>0)or(3>5))
print((3>0)|(3>5))
print(5>4>3)
print(5>4>7)

number = 2+4*3
print(number)
number = number+2
print(number)
number+=2
print(number)

print(abs(-5))#절댓값
print(pow(4,2))#4^2
print(max(4,3))
print(min(2,4))
print(round(3.14))#반올림

from math import * #mate안의 모든 것을 이용하겠다. 
print(floor(4.99))#내림
print(ceil(3.14))#올림
print(sqrt(16))#제곱근

from random import*
print(random())#랜덤으로 난수 뽑기 0.0~1.0미만의 임의의 값을 생성
print(random()*10)#10미만의 임의의 값 생성
print(int(random()*10))#0부터 10미만의 임의의 값 생성
print(int(random()*10)+1)#1부터 10이하의 랜덤수 출력

print(randrange(1,45))#1부터 45미만의 수 생성
print(randrange(1,46))

print(randint(1,45))#양끝을 모두 포함한 랜덤 수 출력

from random import *
date = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월"+ str(date)+"일로 선정되었습니다.")

sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고, 
파이썬은 쉬워요
"""#줄바꿈까지 포함  
print(sentence3)          

jumin = "229922-9229999"
print("성별 : "+jumin[7])
print("연 : " +jumin[0:2])#0~2직전까지 출력
print("월 : " +jumin[2:4])
print("일 : " +jumin[4:6])
print("생년월일 : "+jumin[:6])#처음부터 6직전까지
print("뒤 7자리 : "+jumin[7:14])
print("뒤 7자리 : "+jumin[7:])#7번째부터 끝까지
print("뒤 7자리 (뒤에서부터) : "+jumin[-7:])#맨뒤에서 6번째부터 끝까지

python = "python is Amazing"       
print(python.lower())#다 소문자로 
print(python.upper())
print(python[0].isupper())#대문자인지 여부 확인
print(len(python))#파이썬 길이 반환
print(python.replace("python","java"))#특정문자를 변경

index = python.index("n")#몇번째에 이 문자가 있는지 알려준다. 
print(index)
index = python.index("n", index+1)#두번째 n을 찾는다. 
print(index)
#print(python.find("Java")#얘는 원하는 값이 없으면 -1반환
# print(python.index("Java"))얘는 오류가 난다. -그냥 에러 내버린다. 
print("hi")#만약 인덱스에서 오류가 나버리면 이 문장은 실행 안된다. 그러나 find는 -1출력하고 다음 것도 계속해서 출력한다. 

print(python.count("n"))#몇번 실행되는지 알려준다. 

print("a"+"b")
print("a","b")

print("나는 %d살 입니다." %20)
print("나는 %s를 좋아합니다." %"파이썬")
print("나는 %c가 좋아요."%"B")
print("나는 %s살 입니다. " %20)
print("나는 %s와 %s를 좋아해요" %("파란","빨간"))
print("나는 {}살 입니다".format(20))
print("나는 {}과 {}를 좋아해요".format("파란","빨간"))
print("나는 {1}과 {0}를 좋아해요".format("파란","빨간"))
print("나는 {age}살이며, {color}색을 좋아해요".format(age=20,color = "red"))
print("나는 {color}살이며, {age}색을 좋아해요".format(age=20,color = "red"))

age =20
color = "red"
print(f"나는 {age}살이며, {color}색을 좋아해요")

#탈출문자
print("백문이 불여일견 백견이 불여일타")
print("백문이 불여일견 \n백견이 불여일타")
print("저는 \"나도코딩\"입니다")
print("저는 '나도코딩'입니다")
print('저는 \'나도토딩\'입니다')
#\\ : 문장내에서 하나의 \
print("\\I'm")#출력은 \하나만 나온다

#\r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")#pine을 앞으로 이동
#\b :백스페이스(한글자 삭제)
print("Redd\bApple")
#\t :tab
print("Red\tApple")

#퀴즈
url = "http://naver.com"
my_str = url.replace("http://","")
print(my_str)
my_str=my_str[:my_str.index(".")]#처음부터 . 직전까지만 자른다.
print(my_str)
password = my_str[:3] + str(len(my_str))+ str(my_str.count("e")) +"!"
print("{0}의 비밀번호는 {1}입니다.".format(url, password))
#서로 다른 사이트에 대한 다른 비밀번호 제공
url = "http://daum.com"
my_str = url.replace("http://","")
print(my_str)
my_str=my_str[:my_str.index(".")]#처음부터 . 직전까지만 자른다.
print(my_str)
password = my_str[:3] + str(len(my_str))+ str(my_str.count("e")) +"!"
print("{0}의 비밀번호는 {1}입니다.".format(url, password))

#리스트[] 지하철 칸별로 여러명
subway1 = 10
subway2 = 20
subway3 = 30

subway= [10,20,30]
print(subway)

subway= ["유재석","조세호","박명수"]
print(subway)

#조세호가 몇번째 칸에 있냐
print(subway.index("조세호"))
#하하가 다음 정류장에서 탔다
subway.append("하하")
print(subway)
#정형돈을 유재석 조세호사이에 넣어보자
subway.insert (1,"정형돈")
print(subway)
#지하철에 있는 사람을 한명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)
# print(subway.pop())
# print(subway)
# print(subway.pop())
# print(subway)

#같은 이름의 사람이 몇명 있는가
subway.append("유재석")
print(subway.count("유재석"))

#정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)
#뒤집기도 가능
num_list.reverse()
print(num_list)
#모두지우기
num_list.clear()
print(num_list)

#다양한 자료형 함께 사용
mix_list = ["조세호", 20, True]
print(mix_list)
#list 확장
num_list.extend(mix_list)
print(num_list)

#사전 (단어나오고 설명)key는 중복이 안되고 key에 맞는 value만
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))
#print(cabinet[5]) 정해지지 않은 키값이여서 오류 발생(대괄호는 []오류 발생시키고 프로그램 종료시킨다)
print(cabinet.get(5))#get을 이용하면 값이 없어도 프로그램 종료 되지 않고 none이라고 뜨고 계속해서 다음 것 실행시킨다. 
#none말고 기본값을 쓰고 싶다면
print(cabinet.get(5,"사용가능"))
print(3 in cabinet) #key 있으면 true, 없으면 false
cabinet = {"A-3":"유재석", "B-100" : "김태호 "}#string도 가능하다.
print(cabinet["B-100"])

#새손님
print(cabinet)
cabinet["c-20"]="조세호"#이미 사용중이면 업데이트 된다. 
print(cabinet)
cabinet["A-3"] = "김종국"
print(cabinet)
#간 손님
del cabinet["A-3"]
print(cabinet)
#key들만 출력
print(cabinet.keys())
#value들만 출력
print(cabinet.values())
#key-value 출력
print(cabinet.items())
#목욕탕 폐점
cabinet.clear()
print(cabinet)


#튜플(변경되지 않는 애들)
menu = ("돈까스","치즈까스")
print(menu[0])
print(menu[1])

#menu.add("생선까스") tuple은 값을 추가하는 것 불가(변경 불가, 고정값에 사용)
name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)
(name, age, hobby) = ("김종국", 20, "코딩")#튜플을 이용하면 쉽게 가능
print(name, age, hobby)

#set(집합) 중복이 안되고 순서가 없다
my_set = {1,2,3,3,3}#중복 허용 안함
print(my_set)
java = {"유재석","김태호","양세찬"}
python = set(["유재석","박명수"])

#교집합
print(java&python)
print(java.intersection(python))

#합집합
print(java|python)
print(java.union(python))

#차집합(자바는 하는데 파이썬 모르는 사람)
print(java-python)
print(java.difference(python))

#python할 줄 아는 사람 늘어남
python.add("김태호")
print(python)

#java를 까먹음
java.remove("김태호")
print(java)


#자료구조의 변경
menu = {"커피","우유","주스"}
print(menu,type(menu))#{}

menu = list(menu)
print(menu, type(menu))#[]

menu = tuple(menu)
print(menu, type(menu))#()

#퀴즈
from random import *
users = range(1,21)#1~20숫자 생성
print(type(users))#여기서는 타입이 range여서 list의 특성 쓸 수가 없다
users =list(users)
print(type(users))
print(users)
shuffle(users)
print(users)
winners = sample(users,4)#리스트에서 4명 뽑는다(중복 안된다)
print("--당첨자 발표--")#치킨은 1명 커피는 3명이다.
print("치킨당첨자 : {0}".format(winners[0]))
print("커피당첨자 : {0}".format(winners[1:]))
print("--conglaturation--")


#if

