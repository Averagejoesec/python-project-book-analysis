name = input("Please enter your full name: ")

print(f"Your name in uppercase: {name.upper()}")

print(f"Your name in lowercase: {name.lower()}")

print(f"Total number of characters (excluding spaces): {len(name.strip(' '))}")

print(f"Your name reversed: {name[::-1]}")