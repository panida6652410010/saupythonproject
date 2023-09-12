#โปรแกรมคำนวนหาพื้นที่วงกลม เส้นรอบวงกลม และปริมาตรทรงกลม จากรัศมีที่ป้อนโดยผู้ใช้ทางแป้นพิมพ์ และแสดงผลพื้นที่ เส้นรอบ และปริมาตรทางหน้าจอ

#ขอ 5 ฟังก๋ชัน
import math
#inputRadius
def inputRadius() :
    # r = input('ป้อนรัศมี :' )
    #return r
    
    #r = float( input('ป้อนรัสมี '))
    #return r
    
    #return input('ป้อนรัศมี :')
    
    return float( input('ป้อนรัศมี : '))

#calAreaCircle
def calAreaircle( r ) :
    #area = math.pi * r ** 2
    #area = math.pi * r * r *
    #area = math.pi * math.pow(r,2)
    #return area
    return math.pi * math.pow(r,2)

#calRoundCirle 2 * PI * r


#calCubeCirle 4/3 * PI * r * r * r
def calRoundCircle(r) :
    #round = 2 * math.pi *r
    return 2 * math.pi * r


#calcubeCircle 4/3 * pi *r*r*r
def calCubCircle(r):
    #Cube = 4/3* math.pi *r*r*r
    return 4/3 * math.pi *r*r*r


#showReseuit ขอทั้งหมดทัศนิยม 4 ตำแหน่ง
#พื้นที่วงกลม เส้นรอบวง ปริมาตรทรงกลมเป็น
def showResult():
    radius = inputRadius()
    area = calAreaircle(radius)
    perameter = calAreaircle(radius)
    volume = calAreaircle(radius)
    print('Radius: ' '%.4f' %radius)
    print('Area:' '%.4f' %area)
    print('Perameter:' '%40f' %perameter)
    print('Volume:' '%.4f' %volume)
    
showResult()
