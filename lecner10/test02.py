# เขียนข้อมูลลงไฟล์
# เปิดไฟล์เพื่อเขียนข้อมูลลงไฟล์
f_dti = open('myfile01.txt','W',encoding='utf-8')

f_dti.write('Wow...')
f_dti.write('Wo...\n')
f_dti.write('สวัสดีทุกคน...\n')

f_dti.close()

print('บันทึกข้อมูลลงไฟล์เรียบร้อยแล้ว...')
