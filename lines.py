file=open("sample.txt")
content=file.read()
count=0
conlist=content.split("\n")
for i in conlist:
    if i:
        count+=1
print("The number of lines are : ", count)
