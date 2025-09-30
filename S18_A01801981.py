temperatures=[20,30,21,26,27,31,36]
avgTemperature=sum(temperatures)/len(temperatures)
print("The average Temperature is", avgTemperature)

for temperture in temperatures:
    if temperture >= avgTemperature:
        print(temperture, "is above average")
    else:
        print(temperture, "is below average")
