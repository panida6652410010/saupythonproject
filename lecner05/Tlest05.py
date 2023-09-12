#คำนวณเงินที่จะแชร์กัน ป้อนเงิน ป้อนคน แล้วคำนวณและแสดงเงินที่จะแชร์กันทางหน้าจอ
#โดยให้เขียนเป็นฟังก์ชั่น ขอ 2 ฟังก์ชั่น
#cast/conversion

#รับค่าข้อมูล
def inputMoneyPerson() :
    money = float(input ('ป้อนเงิน : ') )
    person =int(input('ป้อนคน :') )
    return money,person

#คำนวณ แล้วแสดงผล
def calAndShoneyMoneyShare(money,person) :
    #เงิน ขอทศนิยม 2 ตำแหน่ง แชร์กันขอเป็นเลขจำนวณเต็มปัดขึ้น
    print(f'จำนวนเงิน {money} บาท คน {person} คน แชร์กันคนละ {money/person} บาท')
    print("จำนวนเงิน","%.2f" % money, "บาท คน",person,"คน แชร์กันคนละ", round(money/person),"บาท")
    print("จำนวนเงิน"+""+ str("%.2f" % money)+""+"บาท คน"+""+str(person) +""+"คน แชร์กันคนละ"+""+str(round(money/person)))
    print("จำนวนเงิน {} บาท คน {} คน แชร์กันคนละ {} บาท " .format("%.2f"%money,person,round(money,person)))
    print("จำนวน้งิน %s บาท คน %s คน แชร์กันคนละ %s บาท " %("%.2f"%money,person,round(money/person)))
    
    
    
money, person = inputMoneyPerson()

calAndShoneyMoneyShare(money,person)