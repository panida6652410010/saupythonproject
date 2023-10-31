# คุณสมบัติเด่น Inheritance สืบทอด คือ การที่คลาสหนึ่ง สืบทอดอีดคลาสหนึ่ง ***(re-use)
# สืบทอด มีแม่ (super class/parent) มีลูก (sub class/child)
# แม่มีอะไร ลูกมีด้วย เมื่อมีการสืบทอด (Inheritance)

# คุณสมบัติเด่น Polymorphism (ห้องรูป:พฤติกรรมเดียวแต่วิธีการต่างกัน) คือ การที่คลาสลูกเอาเมธอตคลาสแม่มาเขียนใหม่
class Sau01 :
    infoA = 10
    
    def showhi() :
        print('Hi....')
        
class Sau02(Sau01) : # Inhertitance
    infoB = 20
    
    def showHey () :
        print('Hey....')
        
    # overiding method : Polymorphism
    def showhi():
        print('Hi Hi Hi....')
        
ob1 = Sau01()
ob2 = Sau02()
ob2.showhi()
