def knapSack(W, wt, val, n):
    K = [[ 0 for x in range(W+1)] for x in range(n+1)]
 
    # Build table K[][] in bottom up manner
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
		
            else:
                K[i][w] = K[i-1][w]
 
    return K[n][W]
 
# Driver program to test above function
val = [10000, 1000, 100, 10]
wt = [1, 2, 4, 8]
W = 8
n = len(val)
print (knapSack(W, wt, val, n))
