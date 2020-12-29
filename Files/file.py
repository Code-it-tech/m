myfile = open('test.txt')
content = myfile.read()
print(content)

with open("test.txt",mode="r") as mynewfile:
    contents2 = mynewfile.read()
    print(contents2)

with open("test.txt",mode="w") as mynewfile:
    contents1 = mynewfile.write("Adding new Line")
    print(contents1)