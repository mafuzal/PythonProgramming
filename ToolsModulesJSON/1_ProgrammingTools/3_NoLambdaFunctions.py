def fahrenheit(temp):
    return ((float(9)/5)*temp+32)


celsius_temperatures = (36.5, 37, 35, 33)

f = map(fahrenheit, celsius_temperatures)

for t in f:
    print(t)
