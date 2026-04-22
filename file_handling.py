try:
    file = open("data.txt", "r")
    data = file.read()
    print(data)
    file.close()
except FileNotFoundError:
    print("File not found")
    with open("data.txt", "r") as file:
        data = file.read()
        print(data)
