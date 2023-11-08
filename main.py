def dataCapture():
    name = input("Type your name: ")
    age = input("Type your age: ")
    country = input("Type your natural country: ")
    
    dados = [name, age, country]
    
    return dados

userData = dataCapture()

# Print captured data
print("Charged data:")
print("Name:", userData[0])
print("Age:", userData[1])
print("Country:", userData[2])
# print(len(userData))
