# with open('../test.txt', 'r') as file:
#     lines = file.readlines()

# calibration_sum = 0

# for line in lines:
#     line = line.strip()
#     dig1 = 0
#     dig2 = 0
#     for val in line:
#         if val.isdigit():
#             dig1 = val
#             break
#     for val in reversed(line):
#         if val.isdigit():
#             dig2 = val
#             break
#     calibration_sum += ((int(dig1) * 10) + int(dig2))

# print(calibration_sum)


from string import digits as numeric_digits

spelled_digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

with open("../test.txt") as file:
    lines = file.read().split("\n")

total_calibration = 0

for line in lines:
    found_digits = []

    for digit in numeric_digits:
        first_idx = line.find(digit)
        last_idx = line.rfind(digit)
        if first_idx != -1:
            found_digits.append((first_idx, digit))
        if last_idx != -1:
            found_digits.append((last_idx, digit))

    for spelled_digit, value in spelled_digits.items():
        first_idx = line.find(spelled_digit)
        last_idx = line.rfind(spelled_digit)
        if first_idx != -1:
            found_digits.append((first_idx, value))
        if last_idx != -1:
            found_digits.append((last_idx, value))

    found_digits.sort()
    
    if found_digits:
        first_digit = found_digits[0][1]
        last_digit = found_digits[-1][1]
        total_calibration += int(f"{first_digit}{last_digit}")

print(total_calibration)

