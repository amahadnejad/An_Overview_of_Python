# A Simple Array
names = ["John", "David", "Sara"]

# Show a List Value
print(names[0])
print(names[1])
print(names[2])

# Looping Array Elements
cars = ['Ford', 'Honda', 'BMW']
for i in cars:
    print(i)

# Removing From List
cars.pop(1)
for i in cars: # Show The List After Remove
    print(i)

# Another Way To Remove
cars.remove("BMW")
for i in cars: # Show The List After Remove
    print(i)

# Adds an Element at The end of the List
cars.append("Toyota")
for i in cars: # Show The List After Adding
    print(i)

# Remove All Elements From List
cars.clear()
for i in cars: # Show The List After Remove
    print(i)

# Getting a Copy From a List
cars2 = cars.copy()
for i in cars2:
    print(i)