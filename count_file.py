f = open("sample.txt", 'r')
text = f.read()
char_c = len(text)
word_c = len(text.split())
line_c = len(text.splitlines())
vow_c = 0
for ch in text.lower():
    if ch in "aeiou":
        vow_c += 1
print(char_c)
print(word_c)
print(line_c)
print(vow_c)
f.close()
