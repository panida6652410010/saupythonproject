# อ่านข้อมูลจากไฟล์
f_dti = open('myfile01.txt','r',encoding='utf-8')
 
try :
    data = f_dti.readline()
    print(data)
    data = f_dti.readline()
    print(data)
    data = f_dti.readlines()
    print(data,end='')
except Exception :
    print('ติดต่อ 0255888...')
finally :
    f_dti.close()