name = "นันทวัฒน์ ชุมโคตร"
visits = 10
months = 10

def is_at_risk(visits,months):
  return visits < 4 and months > 6 

print ("ชื่อสมาชิก : ",name)
print ("จำนวนที่เข้าใช้งาน : ",visits)
print ("เป็นสมาชิกมา : ",months , " เดือน ")
print ("ความเสียงเลิกใช้บริการ :",is_at_risk(visits,months) )











