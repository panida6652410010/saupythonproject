class Test04 :
    data1 = 10
    
    #constructor
    def _init_(self,data2,data3):
        print('Hi...')
        self.data2 = data2
        self.data3 = data3
        
    def showSumData(self) :
        print(self.data1 + self.data2 + self.data3)
        self.showow()
        
    def showow(self) :
        print('Wow Wow Wow...')
        
objA = Test04(20,30)
objB = Test04(10,20)
objC = Test04(20,30)
