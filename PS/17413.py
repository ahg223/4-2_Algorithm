
String = input()
chunk = []

Flag = True
temp = ""
for char in String:
    if char == "<":
        if temp !="": chunk.append(temp)
        Flag = False
        temp = "<"
        
    elif char == ">":
        temp += char
        chunk.append(temp)
        Flag = True
        temp = ""
        
    elif Flag and char == " ": 
        chunk.append(temp)
        chunk.append(" ")
        temp = ""

    else: temp += char

if temp!="": chunk.append(temp)

for word in chunk:
    if word[0] == "<": print(word,end="")
    else: print(word[::-1], end="")
print()
