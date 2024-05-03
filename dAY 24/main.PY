with open("my_file.txt", mode="w") as file:
    file.write("Hola! Soy Dheeraj Shukla")

with open("my_file.txt", mode="a") as file:
    file.write("\nIn English this is,\nHello! My name is Dheeraj Shukla")

with open("my_file.txt") as file:
    content = file.read()
    print(content)