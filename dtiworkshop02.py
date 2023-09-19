#โปรแกรมตรวจสอบน้ำหนักรถบรรทุกของด่านช่างน้ำหนักว่ารถบรรทุกนั้นมีน้ำหนักรถผ่านเกรณฑ์หรือไม่
#หากน้ำหนักเกิน 1000k ให้แสดงข้อความว่า "รถน้ำหนักไม่ผ่านเกรณฑ์" แต่หากน้ำหนักตั้งแต่
#1000k ลงมาให้แสดงข้อความว่า "รถน้ำหนักผ่านเกรณฑ์" โดยให้ป้อนทะเบียนรถบรรทุก
#และน้ำหนักรถบรรทุกทางแป้นพิมพ์

#วิเคราะห์
#มองหา feature การทำงานว่ามีอะไรบ้าง เพื่อจะไปสร้างเป็น funtion
#รับค่าทะเบียนรถ น้ำหนักรถ -> inputCarDetail
#ตรวจสอลน้ำหนักรถ และแสดงผล -> checkCarAndShowWeight

def inputCarDetail() :
    carNo = input('ป้อนทะเบียนรถ :')
    carWeight = float(input('ป้อนน้ำหนักรถ :'))
    return carNo,carWeight

def checkCarAndShowweight(carNo,carWeight) :
    if carWeight > 1000 :
        print(f'ทะเบียน {carNo} น้ำหนักไม่ผ่านเกณฑ์')
    else:
        print (f'ทะเบียนรถ {carNo} น้ำหนักผ่านเกรณฑ์')
        
        
        
    print("----------------------")
    print("TruckChecker")
    print("----------------------")
    
    carNo, carWeight = inputCarDetail()
    print("----------------------------")
    checkCarAndShowweight(carNo,carWeight)
    print("--------------------------")