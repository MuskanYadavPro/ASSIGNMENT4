try:
    with open('sample.txt', 'r') as file:
        print("Reading file content:")
        count = 1
        for line in file:
            print("Line", count, ":", line.strip())
            count += 1
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
