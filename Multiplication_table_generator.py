file = open("table_reader.txt","w+")

num  = int(input("Enter a number : "))

for i in range(1,num+1):
    result = num*i
    print(result)
    file.write(str(f"The Multiply between {i} * {num} is {result}") + "\n")

file.close()
