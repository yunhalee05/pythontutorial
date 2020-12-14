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
print(python.find("Java")#얘는 원하는 값이 없으면 -1반환
# print(python.index("Java"))얘는 오류가 난다. -그냥 에러 내버린다. 
print("hi")#만약 인덱스에서 오류가 나버리면 이 문장은 실행 안된다. 그러나 find는 -1출력하고 다음 것도 계속해서 출력한다. 

print(python.count("n"))#몇번 실행되는지 알려준다. 

print("a"+"b")
print("a","b")



