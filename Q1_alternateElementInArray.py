#Statement: Print alternate elements of an array.\
#in same line without commas

#The Python print() function has an argument called end, which prevents jump into the newline.


def printAl(arr,n):
    
    for i in range(0,len(arr)):
        if i%2==0:
            print(arr[i],end = " ")
            
            
        
