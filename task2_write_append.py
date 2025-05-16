text= input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(text + "\n")
print("Data successfully written to output.txt.")

add = input("\nEnter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(add + "\n")
print("Data successfully appended.")

print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    info = file.read()
    print(info)
