    def max_of_subarrays(self,arr,n,k):
        ans = []
        q = deque()
        
        if k==1:
            return arr
        
        for i in range(n):
            while q and q[-1][0]<=arr[i]:
                q.pop()
            while q and q[0][1]<=i-k:
                q.popleft()
            q.append((arr[i], i))
            if i>=k-1:
                ans.append(q[0][0])
                
        return ans
