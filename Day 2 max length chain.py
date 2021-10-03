#User function Template for python3

'''
class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
'''

def maxChainLen(Parr, n):
        l=[]
        for i in Parr:
            l.append([i.b,i.a])
        l=sorted(l)
        # return l
        las=l[0][0]
        s=1
        for i in range(1,n):
            if(l[i][1]>las):
                s+=1
                las=l[i][0]
        return s
    # Parr:  list of pair
    #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

if __name__ =='__main__':
    tcs = int(input())

    for _ in range(tcs):
        n=int(input())

        arr=[int(x) for x in input().split()]

        Parr=[]

        i=0
        while n*2>i:

            Parr.append(Pair(arr[i],arr[i+1]))

            i+=2

        #print(Parr,len(Parr))

        print(maxChainLen(Parr, n))
# } Driver Code Ends
