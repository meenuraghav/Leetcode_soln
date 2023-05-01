#User function Template for python3
class Solution:

	def print2largest(self,arr, n):
        max=arr[0]
        smax=-1
        for i in range(1,len(arr)):
            if arr[i]>max:
                smax=max
                max=arr[i]
            elif (arr[i]<max and arr[i]>smax):
                smax=arr[i]
                
        return smax 


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends