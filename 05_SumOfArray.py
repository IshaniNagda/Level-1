#Given an integer array Arr[] of size N. The task is to find sum of it.


class Solution:

	def _sum(self,arr, n):
   		sum=0
   		for i in range(0,n):
   		    sum+=arr[i]
   		return sum
