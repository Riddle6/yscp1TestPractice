# Collect some data from users


name = input("Please enter your first name: ").strip()

while True:
    try:
        age = int(input("Please enter your age: "))

        if age > 0:
            break
        else:
            print("Error! Do not enter your age as a negative number.")

    except ValueError:
        print("Invalid Value! Please try again.")


city = input("Please enter your city: ").strip()

user = {"name": name, "age": age, "city": city}
print(user)

for key in user:
    print(key)

for key, value in user.items():
    print(key, value)
    key1 = user.items('name')
    print(key1)

print("Data Values: \n")
for value in user.values():
    print(value)

grades = {'Hannah': 90, 'Gavin': 45, 'Cameron': 87, 'Hunter': 91, 'Eva': 73, 'Connor': 2, 'Christian': 98}

for student, grade in grades.items():
    print(f"{student}: {grade}")