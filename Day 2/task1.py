from typing import Sequence

#Convert Second into day,hour, minutes and seconds

sec=86400
hour=sec/3600
day=sec/86400
min=sec/60
print(hour,day,min)

a=int(input("Inter the amount of sec you want to convert"))
hour=a/3600
day=a/86400
min=a/60
print("Final value when given sec is converted is {}hr".format(hour))
print("Final value when given sec is converted is {}day".format(day))
print("Final value when given sec is converted is {}min".format(min))