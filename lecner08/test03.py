#OOP
class DtiSau :
    #data/property member ค่าข้อมูล
    stu_name = ''
    score = 0
    gpa = 0
    
    #method member คือ การทำงาน (เขียนแบบฟังก์ชั่น เพียงแต่ว่ามันอยู่ใน class เท่านั้นเลย)
    def hiStudent(self) :
        print(f'สวัสดี{self.stu_name}')
        
    def showScoreAndGrade(self) :
        print(f'คะแนน{self.score} ได้ GPA : {self.gpa}')
        
#สร้าง Object
obj01 = DtiSau() #ชื่อคลาสที่มี() เราเรียกว่าเป็นการสั่งให้ comstructor ของคลาสทำงาน
obj02 = DtiSau()

obj01.stu.name = 'สมชาย'
obj01.hiStudent()
obj02.stu_name = 'สมหญิง'
obj02.score = 99
obj02.gpa = 3.99
