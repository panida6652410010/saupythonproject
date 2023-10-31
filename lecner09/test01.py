class DtiTest01 :
    pass

class DtiTes02 :
    #data/atribute/property/field คือ ตัวแปรประเภทหนึ่ง
    infoA = ''
    infoB = 20
    
    #method คือ ฟังก์ชันประเภทหนึ่ง
    def shoWhi(self) :
        print('Hi...')
    
    def shoWInfoAandB(self) :
        print(self.infoA)
        print(self.infoB)
        
#สร้าง Object 
objA = DtiTes02()
objB = DtiTes02()
sombat = DtiTes02()

objA.infoA = 'xxx'
objB.infoB = 100

print(objA.infoA + objB.infoB)

sombat.shoWInfoAandB()