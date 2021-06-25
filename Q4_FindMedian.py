#Given an array arr[] of N integers, calculate the median
 
class Solution:
	def find_median(self, v):
	    v.sort()
	    self.size=int(len(v))
	    if self.size%2==0:
	        self.ans= (v[int(self.size/2)] +v[(int((self.size/2)-1))])/2
	        return int(self.ans)
	        
	    else:
	        self.ans=(v[int(self.size/2)])
	        return int(self.ans)
