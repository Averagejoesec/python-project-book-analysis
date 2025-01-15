sen1 = input("Enter sentence 1: ")
sen2 = input("Enter sentence 2: ")
sen3 = input("Enter sentence 3: ")

filename = "user_sentences.txt"

with open(filename, "w") as file:
    file.writelines(sen1 + "\n----------")
    file.writelines("\n" + sen2 + "\n----------")
    file.writelines("\n" + sen3)

print(f"Sentences have been saved to {filename}.")