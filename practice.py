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
# weather = input("오늘 날씨는 어때요?")
# if(weather =="비" or weather=="눈"):
#     print("우산을 챙기세요")
# elif weather =="미세먼지":
#     print("마스크를 챙기세요")
# else :
#     print("준비물 필요 없어요.")
# #여기서 Input은 항상 문자로 받기 때문에 int로 변환하려면 따로 변환 해줘야 한다.
# temp = int(input("기온은 어때요?"))
# if 30<=temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10<=temp and temp <30:
#     print("괜찮은 날씨에요")
# elif 0<=temp and temp<10: #= 0<=temp<10
#     print("외투를 챙기세요")
# else:
#     print("추워요. 나가지 마세요")

#for 똑같은 문장 여러번 (중복)
# for waiting_no in[0,1,2,3,4]:
#     print("대기번호 :{0}".format(waiting_no))

# for waiting_no2 in range(5): #0,1,2,3,4
#     print("대기번호 :{0}".format(waiting_no2))

# for waiting_no2 in range(1,6): #1,2,3,4,5
#     print("대기번호 :{0}".format(waiting_no2))

# starbucks = ["아이언맨","토르","아이엠그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

#while
# customer ="토르"
# index = 5
# while index>=1:
#     print("{0},커피가 준비되었습니다. {1}번 남았어요.".format(customer,index))
#     index-=1
#     if index ==0:
#         print("커피는 폐기처분 되었습니다. ")

#무한 루프
# customer = "아이언맨"
# while True:
#     print("{0},커피가 준비되었습니다. 호출 {1}회.".format(customer,index))
#     index +=1

#손님이름이 맞으면 탈출
# customer = "토르"
# person = "unknown"
# while person !=customer :
#     print("{0},커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")
        
#continue, break
absent = [2,5] #결석
no_book = [7] #책을 안가져옴
for student in range(1,11): #1~10
    if student in absent:#만약 부른 학생이 결석이라면
        continue#결석학생은 스킵한다.
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(no_book))
        break #여기서 수업 종료 (반복문 탈출)
    print("{0}, 책을 읽어봐".format(student))

#한줄 for 출석번호 앞에 100을 붙이기로 했다. 
students =[1,2,3,4,5]
print (students)
students = [i+100 for i in students]
print(students)
#학생 이름을 길이로 변환
students2 = ["iron man","thor", "I am groot"]
students2 = [len(i) for i in students2]
print(students2)
#학생 이름을 대문자로
students3 = ["iron man","thor", "I am groot"]
students3 = [i.upper() for i in students3]
print(students3)

#퀴즈 택시기사 1명, 50명의 승객과 매칭 기회 , 총 탑승 승객 수를 구하는 프로그램
#승객별 소요시간은 5~50분 사이의 난수, 소요시간 5~15사이의 승객만 매칭해야 한다. 
from random import *
cnt  =0
for i in range(1,51):
    time = randrange(5,51)#5~50분 사이의 난수
    if 5<=time<=15:#5~15분 손님 승객수 증가,매칭 성공
        print("[0] {0}번째 손님 (소요시간:{1}분)".format(i,time))
        cnt +=1
    else : #매칭 실패
        print("[] {0}번째 손님 (소요시간 :{1}분".format(i,time))
print("총 탑승 승객 :{0}분".format(cnt))

#함수
def open_account():
    print("새로운 계좌가 생성되었습니다")
open_account()

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다".format(balance+money))
    return balance +money
balance = 0
balance = deposit(balance, 1000)
print(balance)

def withdraw (balance, money):
    if balance >=money :
        print("출금이 완료되었습니다. 전액은 {0}원 입니다".format(balance-money))
        return balance -money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다".format(balance))
        return balance
balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)

def withdraw_night(balance, money):#수수료
    commission = 100
    return commission, balance - money - commission #튜플 형식으로 여러개 값 반환
commission, balance = withdraw_night(balance, 500)
print("수수료{0}원이며, 잔액은 {1}원입니다".format(commission, balance))

#기본값
#def profile(name, age, main_lang):
    #print("이름:{0}\t나이:{1}\t주 사용 언어:{2}".format(name, age, main_lang))
#profile("유재석",20,"파이썬")
#profile("김태호",25,"자바")

#같은학교 같은 반, 같은 수업
def profile(name, age=7, main_lang="파이썬"):#기본값있으면, 값 전달 받을때 없으면 디폹트, 있으면 받은 것으로 실행
    print("이름:{0}\t나이:{1}\t주 사용 언어:{2}".format(name, age, main_lang))
profile("유재석")
profile("김태호")

#키워드 값
def profile(name, age, main_lang):
    print(name, age, main_lang)
profile(name="유재석",main_lang="파이썬",age=20) #키워드 해당값이 알아서 순서 맞춰서 들어감

#가변함수이용한 함수 호출
def profile(name, age, lang1, lang2, lang3, lang4,lang5):
    print("이름:{0}\t나이:{1}\t".format(name, age),end=" ")#여기서 end" "는 이어서 다음문장 출력한다는 ㄱ서
    print(lang1, lang2, lang3,lang4,lang5)
profile("유재석",20, "python","jave","C","c++","c#")#만약 하나 더 넣고 싶다면?
profile("김태호",25,"kotlin","Swift","","","")#매번 따옴표 넣어야 하는가?

def profile2(name, age, *language):#가변인자
    print("이름:{0}\t나이:{1}\t".format(name, age),end=" ")#여기서 end" "는 이어서 다음문장 출력한다는 ㄱ서
    for lang in language :
        print(lang, end=" ")
    print()
profile2("유재석",20, "python","jave","C","c++","c#","javascript")
profile2("김태호",25,"kotlin","Swift")

#지역변수, 전역변수
gun = 10

def checkpoint(soldiers):#경계근무
    gun  = 20#지역변수 gun
    print("[함수 내] 남은 총 :{0}".format(gun))
print("전체 총 :{0}".format(gun))#얘는 전역변수 사용
checkpoint(2)#2명이 경계 근무 나감  얘는 지역변수 사용
print("남은 총: {0}".format(gun))#얘도 전역변수 사용
def checkpoint2(soldiers):#경계근무
    global gun #전역변수 gun을 사용하라는 의미
    gun = gun -soldiers
    print("[함수 내] 남은 총 :{0}".format(gun))
checkpoint2(2)

def checkpoint_ret(gun, soldiers):
    gun = gun-soldiers
    print("[함수 내] 남은 총 :{0}".format(gun))#지역변수를 리턴하고 
    return gun
gun = checkpoint_ret(gun,2)#리턴한 값을 그대로 받으면서 전역변수 처럼 사용

#퀴즈
def std_weight(height,gender): #키m, 단위(실수), 성별 "남자"/"여자"
    if gender =="남자":
        return height * height *22
    else:
        return height *height*21
height = 175 #cm 단위
gender = "남자"
weight = round(std_weight(height/100, gender),2) #함수와 키 단위가 다르므로. 소수점 아래 2글자 까지만 받자.
print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height, gender, weight))

#표준 입출력
print("python","java",sep=",") #출력할 때 넣는 ,에 무엇을 넣을 지 결정한다. 
print("python","java",sep=",", end="?") #print따로인 문장이 한 문장에 나온다. end는 문장의 끝부분을 ~로 바꿔달라는 의미
print("무엇이 더 재밌을 까요?")
import sys
print("python","java",file=sys.stdout) #표준 출력으로 처리
print("python","java",file = sys.stderr) #표준 에러로처리 (확인해서 프로그램 처리해야한다.)

scores = {"수학":0,"영어":50,"코딩":100}
for subject, score in scores.items():#키와 값 모두 쌍으로 
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(4),sep=":")#왼쪽정렬ljust오른쪽정렬 rjust

#은행 대기 순번표 001,002,003...
for num in range(1,21):
    print("대기번호 : "+ str(num).zfill(3))#3자리로 채우는데 빈공간은 0으로 채운다.

#answer = input("아무값이나 입력하세요 : ")
#print("입력하신 값은 " +answer +"입니다.")#숫자면 앞에 str로 감싸줘야 한다. 즉, 사용자 입력은 항상 문자열 형태라는 것이다. 

#다양한 출력 포맷
#1. 빈자리는 빈 공간으로 두고, 오른 족 정렬을 하되 총 10자리 공간 확보
print("{0:>10}".format(500))
#2. 양수는 +로 표시, 음수는 -로 표시(부호 출력)
print("{0: >+10}".format(500))
print("{0:>+10}".format(-500))
#왼쪽정렬 빈칸을 밑줄로 채움_
print("{0:_<+10}".format(500))
#3자리 마다 콤마를 찍어주기
print("{0:,}".format(1000000000))
#3자리 마다 콤마 찍고 부호도 붙이기
print("{0:+,}".format(10000000000))
print("{0:+,}".format(-10000000000))
#3자리마다 콤마 붙이고, 부호, 자릿수 확보, 빈자리는 ^로 채우기
print("{0:^<+30,}".format(10000000000))
#소숫점 출력
print("{0:f}".format(5/3))
#소숫점 자릿수 조절
print("{0:.2f}".format(5/3))#소숫점 3째자리에서 반올림

#파일 입출력
score_file = open("score.txt","w",encoding="utf8")#쓰기 목적의 파일 열고 닫기
print("수학 : 0",file=score_file)
print("영어 : 50",file=score_file)
score_file.close()

score_file = open ("score.txt","a",encoding="utf8")#덮어쓰기
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")#얘는 엔터가 자동으로 생성이 안되서 넣어줘야 한다. 
score_file.close()

score_file=open("score.txt","r",encoding="utf8")
print(score_file.read())#값 가져와서 읽기
score_file.close()

score_file=open("score.txt","r",encoding="utf8")
print(score_file.readline())#줄별로 읽기, 한줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end = "") #줄바꿈 안하고 싶으면 end = ""붙이면 된다. 
print(score_file.readline())
print(score_file.readline())
score_file.close()

#몇줄인지 모르고 처리할 때, 
score_file=open("score.txt","r",encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

score_file=open("score.txt","r",encoding="utf8")
lines = score_file.readlines() #모든 라인을 가져와서 리스트로 저장
for line in lines:
    print(line, end = "")
score_file.close()

#pickle
import pickle
profile_file = open ("profile.pickle","wb")#쓰고 b(바이너리타입)
profile = {"이름": "박명수","나이":30,"취미": ["축구","골프","코딩"]}
print(profile)
pickle.dump(profile,profile_file)#프로필의 정보를 file에 저장
profile_file.close()

import pickle
profile_file = open ("profile.pickle","rb")#읽고 b(바이너리타입)
profile = pickle.load(profile_file)#file정보 프로필에 불러오기
print(profile)
profile_file.close()

#with(파일 입출력쉽게)
import pickle
with open("profile.pickle","rb") as profile_file:
    print(pickle.load(profile_file))

with open("study.txt","w",encoding="utf8")as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt","r",encoding="utf8")as study_file:
    print(study_file.read())

#퀴즈
# for i in range(1,51):
#     with open(str(i)+"주차.txt", "w",encoding="utf8") as report_file:
#         report_file.write("-{0} 주차 주간보고 -".format(i))
#         report_file.write("\n부서 : ")
#         report_file.write("\n이름 : ")
#         report_file.write("\n업무 요약 : ")

#클래스
#마린 : 공격유닛, 군인, 총 쏠 수 있음
name = "마린"#유닛이름
hp = 40#유닛 체력
damage = 5#유닛의 공격력
print("{}유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp,damage))
#탱크 : 공격유닛, 탱크, 포를 쏠 수 있는데, 일반모드/시즈모드
tank_name = "탱크"
tank_hp = 150
tank_damage= 35
print("{}유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp,tank_damage))
def attack(name, location, damage):
    print("{0}:{1} 방향으로 적군을 공격 합니다.[공격력{2}]".format(name, location, damage))
attack(name, "1시",damage)
attack(tank_name, "1시",tank_damage)
#탱크가 하나 더 생긴다면? - > ㄱㅖ속해서 생성해내야 한다. (비효율)->클래스로 묶자
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0}유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp,self.damage))
marine1= Unit("marine1",40,5)
marine2 = Unit("marine2",40,5)
tank = Unit("tank",150,35)

#__init__(생성자) 입력해야하는 값 (필수)수를조절

#멤버변수 (클래스의 변수를 외부에서도 멤버 변수로 쓸 수 있다)
#레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80,5)
print("유닛이름 :{0},공격력:{1}".format(wraith1.name,wraith1.damage))
#마인드 컨트롤 :상대방 유닛을 내것으로 만드는 것(빼앗음)
wraith2= Unit("빼앗은 레이스", 80,5)
wraith2.clocking = True #변수를 추가로 할당(대신 wraith1에는 없다.)->확장 한 객체에만 적용
if wraith2.clocking ==True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

#메소드
#공격유닛
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    def attack(self, location):
        print("{0}:{1}방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name,location,self.damage))
    def damaged(self, damage):
        print("{0}:{1}데미지를 입었습니다.".format(self.name, self.damage))
        self.hp -=damage
        print("{0}:현재 체력은 {1}입니다.".format(self.name,self.hp))
        if self.hp <=0:
            print("{0}:파괴되었습니다.".format(self.name))
#파이어 뱃:공격유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃",50,16)
firebat1.attack("5시")
#공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)
#일반 유닛
class Unit_:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

#상속 공격유닛과 일반유닛의 비슷한 부분을 상속하자
class AttackUnit_(Unit_):
    def __init__(self, name, hp, damage):
        Unit_.__init__(self,name,hp)#일반유닛 가져오고 나머지는 채워준다.
        self.damage = damage
    def attack(self, location):
        print("{0}:{1}방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name,location,self.damage))
    def damaged(self, damage):
        print("{0}:{1}데미지를 입었습니다.".format(self.name, self.damage))
        self.hp -=damage
        print("{0}:현재 체력은 {1}입니다.".format(self.name,self.hp))
        if self.hp <=0:
            print("{0}:파괴되었습니다.".format(self.name))
firebat1 = AttackUnit_("파이어뱃",50,16)
firebat1.attack("5시")
#공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)
#부모 클래스 2개 이상 받아보자.(다중상속)
#드랍쉽 :공중유닛, 수송기, 마린/파이어뱃/탱크등을 수송해서 다른 곳에 떨어뜨려줌. 공격기능 없음
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed =flying_speed
    def fly(self, name, location):
        print("{0}:{1} 방향으로 날아갑니다. [속도{2}]".format(name, location,self.flying_speed))
#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self, name, hp,damage, flying_speed):
        AttackUnit_.__init__(self,name, hp,damage)
        Flyable.__init__(self, flying_speed)
#발키리:공중공격 유닛 한번에 14발 미사일 발사
valkyrie = FlyableAttackUnit("발키리",200,6,5)
valkyrie.fly(valkyrie.name,"3시")

#연산자 오버로딩
class _Unit:
    def __init__(self, name, hp,speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0}:{1}방향으로 이동합니다. [속도{2}]".format(self.name, location,self.speed))
class _AttackUnit(_Unit):
    def __init__(self, name, hp, speed,damage):
        _Unit.__init__(self,name,hp,speed)#일반유닛 가져오고 나머지는 채워준다.
        self.damage = damage
    def attack(self, location):
        print("{0}:{1}방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name,location,self.damage))
    def damaged(self, damage):
        print("{0}:{1}데미지를 입었습니다.".format(self.name, self.damage))
        self.hp -=damage
        print("{0}:현재 체력은 {1}입니다.".format(self.name,self.hp))
        if self.hp <=0:
            print("{0}:파괴되었습니다.".format(self.name))
class _FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self, name, hp,damage, flying_speed):#지상 스피드는 0
        _AttackUnit.__init__(self,name, hp,0,damage)
        Flyable.__init__(self, flying_speed)
    def move(self, location):
        print("[공중유닛이동]")
        self.fly(self.name,location)
#벌쳐 : 지상 유닛,기동성이 좋음
vulture = _AttackUnit("벌쳐", 80,10,20)
#배틀 크루저 :공중유닛, 체력 좋음, 공격력 좋음
battlecuiser = _FlyableAttackUnit("배틀클루저",500,25,3)
vulture.move("11시")
battlecuiser.fly(battlecuiser.name,"9시")
#연산자 오버로딩을 통해서 알아서 move를 쓰는데 공중유닛이면 fly쓰고 지상유닛이면 move 쓰도록
battlecuiser.move("9시")
from random import *
#pass
class BuildingUnit(Unit):
    def __init__(self, name, hp,location):
        pass#일단 넘어간다는 의미(완성 된 것처럼)
#서플라이 디폿 :건물, 1개건물 = 8유닛
supply_depot =BuildingUnit("서플라이 디폿", 500,"7시")
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")
def game_over():
    print("Plyaer :gg")#good game
    print("[Player]님이 게임에서 퇴장하셨습니다.")
game_start()
game_over()
class BuildingUnit_(_Unit):
    def __init__(self, name, hp, location):
        #_Unit.__init__(self, name, hp, 0)# 빌딩이니까 스피드 0
        super().__init__(name, hp, 0)#문제는 다중상속에서 발생
        self.location = location


class _Unit_:
    def __init__(self, name, hp,speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0}유닛이 생성되었습니다.".format(name))
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0}:{1}방향으로 이동합니다. [속도{2}]".format(self.name, location,self.speed))
    def damaged(self, damage):
        print("{0}:{1}데미지를 입었습니다.".format(self.name, self.damage))
        self.hp -=damage
        print("{0}:현재 체력은 {1}입니다.".format(self.name,self.hp))
        if self.hp <=0:
            print("{0}:파괴되었습니다.".format(self.name))
class _AttackUnit_(_Unit_):
    def __init__(self, name, hp, speed,damage):
        _Unit.__init__(self,name,hp,speed)#일반유닛 가져오고 나머지는 채워준다.
        self.damage = damage
    def attack(self, location):
        print("{0}:{1}방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name,location,self.damage))
class Marine(_AttackUnit_):
    def __init__(self):
        _AttackUnit.__init__(self, "마린",40,1,5)

        #스팀팩 : 일정시간동안 이동 밑 공격속도를 증가, 체력 10소모
    def stimpack(self):
        if self.hp >10:
            self.hp -=10
            print("{0}:스팀팩을 사용합니다. (hp 10감소".format(self.name))
        else:
            print("{0}:체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

class Tank(_AttackUnit_):
    #시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능(이동불가)
    #한번 적용 시키면 모든 탱크에 대해서 작동 (클래스 바로 밑에 적어보자.)
    seize_developed=False#시즈모드 개발 여부
    def __init__(self):
        _AttackUnit.__init__(self, "탱크",150,1,35)
        self.seize_mode =False
    def set_seize_mode(self):
        if Tank.seize_developed ==False:
            return#시즈모드 아니면 나간다
        #현재 시즈모드가 아닐때->시즈모드 작동
        if self.seize_mode ==False:
            print("{0}: 시즈모드로 전환합니다".format(self.name))
            self.damage *=2
            self.seize_mode = True
        #현재 시즈모드 일때 ->시즈모드 해제
        else:
            print("{0}:시즈모드를 해제합니다. ".format(self.name))
            self.damage/=2
            self.seize_mode = False
class Wraith(_FlyableAttackUnit):
    def __init__(self):
        _FlyableAttackUnit.__init__(self, "레이스",80,20,5)
        self.clocked = False #클로킹 모드 (해제상태)
    def clocking(self):
        if self.clocked ==True: #클로킹 모드 ->해제
            print("{0} :클로킹 모드 해제합니다.".format(self.name))
            self.clocked =False
        else:#클로킹 모드 해제->설정
            print("{0} :클로킹 모드 설정합니다.".format(self.name))
            self.clocked =True
game_start()
m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

#전군 이동 
for unit in attack_units:
    unit.move("1시")
#탱크 시즈모득 ㅐ발 
Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")
#공격모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 :클로킹)
for unit in attack_units:
    if isinstance(unit, Marine):  #클래스의 인스턴스 여부확인
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()
#전군 공격
for unit in attack_units:
    unit.attack("1시")
#전군 피해
for unit in attack_units:
    unit.damaged(randint(5,21)) #공격은 랜덤으로 받음 
#게임 종료
game_over()

#퀴즈
class House:
    def __init__(self, location, house_type, deal_type, price,completion_year):
        self.location =location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print(self.location,self.house_type,self.deal_type,self.price,self.completion_year)

houses = []
house1 = House("강남","아파트","매매","10억","2010년")
house2 = House("마포","오피스텔","전세","5억","2007년")
house3 = House("송파","빌라","월세","500/50","2000년")
houses.append(house1)
houses.append(house2)
houses.append(house3)
print("총 {0}대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()

#예외처리

# try:
#     print("나누기 전용 계산기 입니다.")
#     num1=int(input("첫번째 숫자를 입력하세요 :"))
#     num2=int(input("두번째 숫자를 입력하세요 :"))
#     print("{0}/{1} = {2}".format(num1,num2, int(num1/num2)))
# #num에 숫자가 아닌 다른 수를 넣었을때,0을 넣었을 때도 오류
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:#오류문자 그대로 출력
#     print(err)


# try:
#     print("나누기 전용 계산기 입니다.")
#     nums = []
#     nums.append(int(input("첫번째 숫자를 입력하세요 :")))
#     nums.append(int(input("두번째 숫자를 입력하세요 :")))
#     nums.append(int(num[0]/num[1]))
#     print("{0}/{1} = {2}".format(nums[0],nums[1], nums[2]))
# #num에 숫자가 아닌 다른 수를 넣었을때,0을 넣었을 때도 오류
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:#오류문자 그대로 출력
#     print(err) 
# except:
#     print("알 수 없는 에러가 발생하였습니다.")#나머지 모든 에러에 대해서 여기서 처리
#     # except Exception as err: 오류메세지 정확하게 출력하고 싶을 때
#     # print("알 수 없는 에러가 발생하였습니다.")#나머지 모든 에러에 대해서 여기서 처리

#에러발생시키기
# try :
#     print("한자리 숫자 나누기 전용 계산기 입니다.")
#     num1 = int(input("첫번째 숫자를 입력하세요 :"))
#     num2 = int(input("두번째 숫자를 입력하세요 :"))
#     if num1 <=10 or num2>=10:
#         raise ValueError #오류 발생시켜서 아래 예외 상황으로 이동하도록 한다.
#     print("{0}/{1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다.한자리 숫자만 입력하세요")

#사용자 정의 예외처리 
# class BigNumberError(Exception): #내가 만든 오류, 메세지 던져주고 싶을 때
#     def __init__(self, msg):
#         self.msg =msg
#     def __str__(self):
#         return self.msg
# try :
#     print("한자리 숫자 나누기 전용 계산기 입니다.")
#     num1 = int(input("첫번째 숫자를 입력하세요 :"))
#     num2 = int(input("두번째 숫자를 입력하세요 :"))
#     if num1 >=10 or num2>=10:
#         raise BigNumberError("입력값 :{0},{1}".format(num1,num2))#이 메세지를 가지고 있다가 
#     print("{0}/{1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다.한자리 숫자만 입력하세요")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요")
#     print(err)#여기서 출력할 것이다. 
# #finally 오류 발생과 상관없이 언제나 실행되는 것 
# finally: 
#     print("계산기를 이용해 주셔서 감사합니다.")

#퀴즈
# class SoldOutError(Exception): #내가 만든 오류, 메세지 던져주고 싶을 때
#     pass
# chicken = 10
# waiting = 1
# while(True):
#     try:
#         print("[남은치킨 :{0}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#         if order>chicken:
#             print("재료가 부족합니다")
#         elif order<=0:
#             raise ValueError
#         else:
#             print("[대기번호 {0}] {1}마리 주문이 완료되었습니다.".format(waiting, order))
#             waiting +=1
#             chicken -=order
#         if chicken ==0:
#             raise SoldOutError
#     except ValueError:
#         print("잘못된 값을 입력하였습니다.")
#     except SoldOutError:
#         print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
#         break

#모듈

