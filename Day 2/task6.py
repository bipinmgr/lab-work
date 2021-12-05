#You live 4 miles from university . The bus drives at 25mph but spends 2 minutes at each
#of the 10 stopes on the way, how long wiill the bus journey take?Alternatively, you could run to university.
#You jog the first mile at 7mph: then run the next tow at 15mph :before jogging the last at 7mph again.
#will this be quicker or slower than the bus?

distanc=4
x=25

#bus stops at 10 places and spent 2 minutes
stop_time = 10+2
e=1/x
t=e*60
total_time=t+stop_time
print(f"the total time to reach university by bus{total_time}")

#runs with the speed of 7mph
y=7
z=1/y
time_a=z*60
w=15
q=2/w
time_b=q*60
t=7
u=1/t
time_c=u*60
total_time2=time_a + time_b +time_c
print(f"The total time for walking is {total_time2}")
if total_time2 > total_time:
    print(f"Walking is faster to reach university")
