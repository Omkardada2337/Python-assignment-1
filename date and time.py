from datetime import datetime as d
dt=d.today()
print(dt)
d1=dt.strftime("%d / %m / %Y")
d2=dt.strftime("%d / %m / %y")
d3=dt.strftime("%I : %M %p")
d4=dt.strftime("%H : %M : %S %p")
d5=dt.strftime("%d / %m / %Y %B ")
d6=dt.strftime("%d - %b - %Y")
print(d1)
print(d2)
print(d3)
print(d4)
print(d5)
print(d6)