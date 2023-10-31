class DtiTest03 :
    # data
    infoA = 10
    
    #constructor จะเป็นตัวทำให้ object ที่สร้างจากคลาสเดียวกันไม่จำเป็นต้องเหมือนกัน
    # constructor จะทำงานทุกครั้งที่มีการสร้าง Object
    def _init_(self,infoB,infoC) :
        self.infoB = infoB
        self.infoC = infoC
        print('Wow Wow Wow...')
        
    #method
    def showixAndInfo(self,mix) :
        print(self.infoA + self.infoB + self.infoC + mix)
    
#สร้าง Object
sau1 = DtiTest03(20,30)
sau2 = DtiTest03(10,100)
sau3 = DtiTest03(20,30)