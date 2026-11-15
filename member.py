class member: #คลาส
  def __init__(self,name,visits,months,monthly_fee):
    self.name = name
    self.visits = visits
    self.months = months
    self.monthly_fee = monthly_fee

  def is_at_risk(self): #เมธอด
    return self.visits < 4 and self.months > 6

  def total_paid(self): #เมธอด
    return self.months * self.monthly_fee
  
m1 = member("นันทวัฒน์", 3 , 10 ,900) #Object
m2 = member("ชุมโคตร", 10 , 9 ,900) #Object
m3 = member("ดอม", 10 , 8 ,900) #Object

print ("ชื่อสมาชิก : ",m1.name)
print ("ความเสียงเลิกใช้บริการ :", m1.is_at_risk())
print ("ค่าบริการ :", m1.total_paid() ,"บาท")

print ("ชื่อสมาชิก : ",m2.name)
print ("ความเสียงเลิกใช้บริการ :", m2.is_at_risk())
print ("ค่าบริการ :", m2.total_paid(),"บาท")

print ("ชื่อสมาชิก : ",m3.name)
print ("ความเสียงเลิกใช้บริการ :", m3.is_at_risk())
print ("ค่าบริการ :", m3.total_paid(),"บาท")
