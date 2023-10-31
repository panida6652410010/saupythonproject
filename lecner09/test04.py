# คุณสมบัติ Encapsulation (ห่อหุ้ม data/attribute/field/property)
class DtiTest05 :
    #datha
    infoA = 10 #ไม่ได้ Encap
    __infoB = 20 #Encap ดูจาก _???? มันถูกกำหนด acess_modifier เป็น private
    
    def __init__(self,infoC,infoD) :
        self.infoC = infoC # ไม่ได้ Encap
        self.__infoD = infoD # Encap คูจาก __???? -> เป็นการกำหนด acess_modifier เป็น private
    
    #เมื่อได้ตาม Emcap จะต้องมีเมธอต 2 ตัวเสมอ คือ get,set ของ data ตัวขึ้น
    def setInfoB(self,infoB) : #กำหนดค่าให้กับ data
        self.__infoB = infoB
        
    def getInfoB(self) : 
        return self.__infoB
    
    def setInfoD(self,infoD) :
        self.__infoD = infoD
        
    def getInfoB(self) :
        return self.__infoD
    
    def showInfo(self) :
        print(self.infoA,end ='')
        print(self.__infoB,end='')
        print(self.infoC,end ='')
        print(self.__infoD)
        print('----------------')
        
ob1 = DtiTest05(30,40)
ob2 = DtiTest05(30,100)
ob1.showInfo() # 10 20 30 40 
ob1.infoA = 555
# ob1.__infoB =999 #ไม่เปลี่นนค่า เพราะมันถูก Encap
ob1.setInfoB(999)
ob1.showInfo() # 555 999 30 40
print(ob1.getInfoB() + ob1.getInfoD())