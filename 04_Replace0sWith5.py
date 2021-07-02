#Given a number N. The task is to complete the function convertFive() which replace all zeros in the number with 5 and returns the number.

class Solution:
    def convertFive(self,n):
        str_num=str(n)
        size=len(str_num)
        new_num=""
        for i in range(0,size):
            if str_num[i]!="0":
                new_num+=str_num[i]
            else:
                new_num+="5"
        
        return int(new_num)
