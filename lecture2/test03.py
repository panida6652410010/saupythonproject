# แสดงข้อมูลหลายๆ ประเภทใน print เดียว

#1 ใช้ , โดยที่จะมี SPACE ในแต่ละ,
print("SAU",555,123,456,True,10+50)

#2ใช้ + มีข้อแม้ ข้อมูลที่ไม่ใช้ String ต้องแปลงเป็น sting และไม่มี space ให้เหมือนกัน
print("SAU"+str(555)+''+str(123,456)+''+str(True)+''+str(10+50))

#3 ใช้เมธอดชื่อ format
print("SAU {} {} {} {}".format(555,123,456, True, 10+50))
print("SAU {} {} {} {}".format(555,123,456, True, 10+50))

#4 ใช้ f-stsing ***
print(f'SAU {5555} {123.456} {True} {10+50}')

#-------------
#กรณี 1 บรรทัดมีหลาย Statment ให้คั้นด้วย ;
print('aaa');print(False)