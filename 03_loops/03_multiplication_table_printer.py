number = int(input("Please Enter which number table you want? :"))

for i in range(1,10+1):
    if i == 5:
        continue
    print(number,"x",i,"=",number*i)

