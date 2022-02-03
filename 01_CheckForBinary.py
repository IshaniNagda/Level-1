#Given a non-empty sequence of characters str, return true if sequence is Binary, else return false
#hellooo
def isBinary(str):
    
    for i in str:
        if i not in "01":
            return 0
        
    return 1
