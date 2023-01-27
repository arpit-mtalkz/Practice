for i in range (2,21):
    r=open(r"Multiplication_table_of_2",'w')
    for j in range(1,11):
        r.write(f"{i}X{j}={i*j}")
    break