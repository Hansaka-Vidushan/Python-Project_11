# file open
file = open("Data.txt" , "r+t")

# Data Read
for i , line in enumerate(file):
    print(i, " " , line)

while True:
    contents = file.readline()
    if not contents:
        break
    print(contents)


# Data Write
for i in range(1,100):
    file.write(str(i))

# file close
file.close()

# File open and close
with open("Data.txt" , "w") as file:
    file.write("hansaka")


