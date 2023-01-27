def fahrenheit(cel):
    return ((cel * 9/5) + 32)
cel=int(input())
temp=fahrenheit(cel)
print(f"The temprature in Fahrenheit is {temp}°C")