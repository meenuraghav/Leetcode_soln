#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
        c=0
        num=N
        while (N>0):
            n=N%10
            N=N//10
            if n==0:
                continue
            if num%n==0:
                c=c+1
        return c    
     
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends