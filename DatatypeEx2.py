#Declareing the var Cars
Cars = [56,78,34,21,56,34, 125,45, 89, 75,12,56,]
#finding largest ,smallest and sum of cars
Largest = max(Cars)
smallest = min(Cars)
sumofcars = sum(Cars)
#print("Cars : " + str(Cars))
Cars = (list(set(Cars)))
#sorting list
Cars.sort()
Cars.reverse()
#Displaying results
print(str(Cars),smallest,Largest,sumofcars)

