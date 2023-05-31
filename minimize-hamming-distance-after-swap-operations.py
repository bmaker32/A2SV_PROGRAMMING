class Solution(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        """
        :type source: List[int]
        :type target: List[int]
        :type allowedSwaps: List[List[int]]
        :rtype: int
        """
        d = {}
        def find(x):
            d.setdefault(x,x)
            if d[x] != x:
                d[x] = find(d[x])
            return d[x]
        
        def union(x,y):
            s1 = find(x)
            s2 = find(y)
            d[s2] = s1
        
        for swap in allowedSwaps:
            union(swap[0],swap[1])
        
        components = defaultdict(list)
        for k,v in d.items():
            if k ==v :
                components[k].append(k)
            else:
                parent = find(v)
                components[parent].append(k)
        
        visited = set()
        hammingd = 0
        for comp,mem in components.items():
            srcDict = defaultdict(int)
            targetDict = defaultdict(int)
            for idx in mem:
                visited.add(idx)
                srcDict[source[idx]] += 1
                targetDict[target[idx]] += 1
            
            common = 0
            for k in srcDict.keys():
                if k in targetDict:
                    common += min(srcDict[k],targetDict[k])
            hammingd += len(mem) - common
            
        for i,v in enumerate(source):
            if i not in visited and source[i] != target[i]:
                hammingd += 1
        
        return hammingd