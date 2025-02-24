num = int(input("Enter the number of factors: "))
for i in range(1,num+1):
    if num % i == 0 :
        print(i,end = " ")
        i+=1
