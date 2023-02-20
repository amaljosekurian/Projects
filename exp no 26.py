str1=input("Enter a string: ")
dict={}
for n in str1:
    if n in dict:
        dict[n]+=1
        print(dict)
    else:
        dict[n]=1
        print(dict)
print("Character Frequency")
for a,b in dict.items():
    print(a,b)