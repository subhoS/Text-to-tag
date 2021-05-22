f = open("temp.txt",'r')
a = f.readlines()
new_strings = []
for string in a:
    new_sting = string.replace("\n","<br/>")
    new_strings.append(new_sting)
#print(new_strings)
for i in new_strings:
    print(i)
r = open("Output.txt","w")
for i in new_strings:
    r.write(i)
print("file has been written to output.txt")                  
r.close()
f.close()
    
