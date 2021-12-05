#Find BMI of a person where take mass and height as input from the user 
#BMI=mass in kg/(height in m)2

Mass=int(input("inter your mass"))
Height=int(input("inter your height"))
BMI=Mass/Height**2
print("BMI of the person is {}kg/m\u00b2".format(BMI))
