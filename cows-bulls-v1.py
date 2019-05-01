number = [1, 2, 3, 4]
print("Number:", number)

guess = [4, 5, 3, 1]
# print("Guess:", guess)

total = 0
for digit in guess:
    count = number.count(digit)
    print("Digit:", digit, "Count:", count)
    total = total + count

print("Total:", total)

# total = cows + bulls

bulls = 0
for digit in guess:
    if number.count(digit) != 0:
        if number.index(digit) == guess.index(digit):
            bulls = bulls + 1

print("Bulls:", bulls)
print("Cows:", total - bulls)
