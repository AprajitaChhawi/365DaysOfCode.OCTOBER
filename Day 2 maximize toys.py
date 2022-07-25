#User function Template for python3

class Solution:
    def toyCount(self, N, K, arr):
        arr.sort()
        summ = 0
        count = 0
        for i in range(N):
            summ += arr[i]
            if summ <= K:
                count += 1
            else:
                return count
                break
        return count
        # code here


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, K = [int(x) for x in input().split()]
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        print(ob.toyCount(N, K, arr))
# } Driver Code Ends
