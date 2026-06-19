numbers = []
while True:
    inp = input("Enter a number: ")
    if inp == 'done':
        break
    try:
        value = float(inp)
        numbers.append(value)
    except:
        print("Invalid input")

print('Maximum:', max(numbers))
print('Minimum:', min(numbers))
