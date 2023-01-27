def remove(string,word):
    string=string.replace(word,"")
    return string.strip()
string1=input()
word=input
s=remove(string1,word)
print(s)