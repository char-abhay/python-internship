numbers = []

print("Enter numbers one by one.")
print("Type 'done' to finish.\n")

while True:

    value = input("Enter number: ")

    if value.lower() == "done":
        break

    numbers.append(int(value))

count = len(numbers)

total = 0
even = 0
odd = 0

maximum = numbers[0]
minimum = numbers[0]

sorted_list = True

for i in range(count):

    total += numbers[i]

    if numbers[i] % 2 == 0:
        even += 1
    else:
        odd += 1

    if numbers[i] > maximum:
        maximum = numbers[i]

    if numbers[i] < minimum:
        minimum = numbers[i]

    if i < count - 1:
        if numbers[i] > numbers[i + 1]:
            sorted_list = False

average = total / count

print("\n------ Number Analyzer ------")
print(f"Numbers      : {numbers}")
print(f"Count        : {count}")
print(f"Sum          : {total}")
print(f"Average      : {average:.2f}")
print(f"Maximum      : {maximum}")
print(f"Minimum      : {minimum}")
print(f"Even Count   : {even}")
print(f"Odd Count    : {odd}")
print(f"Sorted       : {sorted_list}")