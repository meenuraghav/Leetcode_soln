#User function Template for python3

class Solution:
    def printTriangle(self, N):
        for i in range(2*N-1):
            totalEle=i+1 if i<N else 2*N-i-1
            for j in range(totalEle):
                print("*",end=' ')
            print()


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends