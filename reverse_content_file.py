f1 = open("sample.txt", "r")
text = ""
ch = f1.read(1)
while ch != "":
    text = ch + text
    ch = f1.read(1)
f2 = open("reverse.txt", "w")
f2.write(text)
print("Reversed content written successfully")
f1.close()
f2.close()
