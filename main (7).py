#datetime module
from datetime import datetime
dt1 = datetime(year=2019,month=5,day=30)
print(dt1)
d2 = datetime(year=2020,month=4,day=12,hour=2,minute=45)
print(d2)
d3 = datetime(2003,4,15,10,10,5)
print(d3)
#accessing current date and time 
ct = datetime.now()
print("current date and time:",ct)