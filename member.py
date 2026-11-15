class member: #คลาส
  def __init__(self,name,visits,months):
    self.name = name
    self.visits = visits
    self.months = months

  def is_at_risk(self): #ฟังชั่น
    return self.visits < 4 and self.months > 6
  
m1 = member("นันทวัฒน์", 3 , 10 ) #Object
m2 = member("ชุมโคตร", 10 , 10 ) #Object
m3 = member("ดอม", 10 , 6 ) #Object

print ("ชื่อสมาชิก : ",m1.name)
print ("ความเสียงเลิกใช้บริการ :", m1.is_at_risk())

print ("ชื่อสมาชิก : ",m2.name)
print ("ความเสียงเลิกใช้บริการ :", m2.is_at_risk())

print ("ชื่อสมาชิก : ",m3.name)
print ("ความเสียงเลิกใช้บริการ :", m3.is_at_risk())


    