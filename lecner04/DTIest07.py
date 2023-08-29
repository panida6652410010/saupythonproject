idemp = input("รหัสพนักงาน : ")
nameemp = input("ชื่อพนังงาน : ")
salaryemp = float(input("เงินเดือนพนังงาน : "))
sum = salaryemp - (salaryemp * 7/100) - 500
print(f"รหัสพนักงาน {idemp} ชื่อพนักงาน {nameemp} เงินเดือนสุทธิ {sum}")
