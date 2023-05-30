class Unions:
    def __init__(self,n):
        self.rep = {i:i for i in range(n)}
        self.size = {i:1 for i in range(n)}
    
    def find(self,k):
        temp = k 
        while self.rep[k] != k:
            k = self.rep[k]
        while self.rep[temp] != temp:
            parent = self.rep[temp]
            self.rep[temp] = k
            temp = parent 
        return k
    def union(self,x,y):
        xrep = self.find(x)
        yrep = self.find(y)
        if self.size[xrep] > self.size[yrep]:
            self.size[xrep] += self.size[yrep]
            self.rep[yrep] = xrep
        else:
            self.size[yrep] += self.size[xrep]
            self.rep[xrep] = yrep
    def connected(self,x,y):
        xrep = self.find(x)
        yrep = self.find(y)

        return xrep == yrep
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        uf = Unions(len(accounts))
        email2name = {}
        for i, account in enumerate(accounts):
            emails = account[1:]
            for email in emails:
                if email in email2name: uf.union(email2name[email], i)
                email2name[email] = i
        for email, idx in email2name.items():
            print(email, idx, uf.find(idx))   
            
        merged_list = defaultdict(list)
        for email, idx in email2name.items():
            merged_list[uf.find(idx)].append(email)

        final_list = [[accounts[root][0]] + sorted(emails) for root, emails in merged_list.items()]
        return final_list