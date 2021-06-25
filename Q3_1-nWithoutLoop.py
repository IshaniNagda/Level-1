#Print numbers from 1 to N without the help of loops.

#recursion is used

class Solution:    
    #Complete this function
    def printNos(self,N):
        if N>=1:
            self.printNos(N-1)
            print(N, end=" ")
        else:
            return 1
