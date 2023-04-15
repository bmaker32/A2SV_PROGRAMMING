class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        a=[]
        def fun(s,ar,t,re,a):
            r=re[:]
            for x in ar:
                if t-s<x:
                    break
                if (s+x)==t:
                    r.append(x)
                    a.append(r)
                    break
                fun(s+x,ar,t,r+[x],a)
                
            return
        fun(0,sorted(candidates),target,[],a)
        for x in range(len(a)):
            a[x]=sorted(a[x])
        u = [list(x) for x in set(tuple(x) for x in a)]
        print(u)
        return u