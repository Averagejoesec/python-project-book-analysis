filename = "practice/numbers.txt"

with open(filename, "r") as file:
    contents = file.readlines()
    contents = [int(num) for num in contents]
    print(f"For the file contents: {contents}")
    max_num = 0
    for num in contents:
        if num > max_num:
            max_num = num
    print(f"The maximum number in the file is: {max_num}")
