myDict={
    "Pankha": "Fan",
    "Dabba": "Box",
    "Vastu": "item"
}
print("options are : ", myDict.keys())
a=input("Enter your hindi word:\n")
print("Your English word will be", myDict.get(a))