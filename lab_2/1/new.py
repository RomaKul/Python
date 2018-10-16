
print("hI")

file1= open("first.txt", "r")
file2=open('second.txt')
file3=open("final.txt","w")
file3.close()
file3=open("final.txt","a")

msg=file2.readlines()

len= len(msg)

for i, line in enumerate(file1):
    if(i>=len):
        break
    print("w")
    file3.write(line+msg[i])

file1.close()
file2.close()
file3.close()