#using break for terminating the loop if reached the desired state
for i in range(10):
    print(i)
    if(i==5):
        break
#using continue to stop the current iteration and move on the other
for i in range(10):
    if i==5:
        continue
    print(i)
#pass is a null statement in python it instructs to do nothing
i=4
if i<0:
    pass
print("Hello World")