def par(num):
    return(num % 2 == 0)
        

print("Dime un número")
num = int(input())
index = 1
while(index < num):
   
    index = index + 1
    
    if (par(index)):
         print(index)