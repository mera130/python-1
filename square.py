n = int(input("Enter a number: "))

squares = []
evensquares = []
oddsquares = []

for i in range(1, n + 1):
    square = i * i
    squares.append(square)

    if square % 2 == 0:
        evensquares.append(square)
    else:
        oddsquares.append(square)

print("All squares:", squares)
print("Even squares:", evensquares)
print("Odd squares:", oddsquares)
