class Unit:
    def __init__(self):
        print("Unit 생성자")
class Flyable:
    def __init__(self):
        print("Flyable 생성자")
class FlyableUnit(Unit,Flyable): 
    def __init__(self):
        super().__init__()#순서상의 맨 마지막에 상속받는 클래스에 대해서만 상속된다.다 상속 받고 싶을 떄는
        Unit.__init__(self)#두개 다 따로따로 받아줘야 한다. 
        Flyable.__init__(self)

#드랍쉽
dropship = FlyableUnit()