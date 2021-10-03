#User function Template for python3
import sys
import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        visited = [False]*V
        heap = []
        heapq.heappush(heap,(0,-1,0))
        weight = []

        while len(heap)>0:
            temp = heapq.heappop(heap)

            if visited[temp[2]] == True:
                continue
            visited[temp[2]] = True
            weight.append(temp[0])
            for nbr in adj[temp[2]]:
                if visited[nbr[0]] == False:
                    heapq.heappush(heap,(nbr[1],temp[2],nbr[0]))
        return sum(weight[1:])
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends
