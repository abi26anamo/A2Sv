class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        n = len(accounts)
        self.rep = [i for i in range(n)]
        self.size = [1 for i in range(n)]
        email_to_id = {}
        
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                if email in email_to_id:
                    self.union(email_to_id[email], i)
                else:
                     email_to_id[email] = i
                
        merged_accounts = defaultdict(list)
        for i, account in enumerate(accounts):
            root = self.find(i)
            merged_accounts[root].extend(account[1:])
        
        result = []
        for root, emails in merged_accounts.items():
            name = accounts[root][0]
            result.append([name] + sorted(set(emails)))

        return result

    def find(self, x):
        if self.rep[x] == x:
            return x
        curr = self.find(self.rep[x])
        self.rep[x] = curr
        return curr

    def union(self, u, v):
        u_rep = self.find(u)
        v_rep = self.find(v)

        if self.size[u_rep] > self.size[v_rep]:
            self.rep[v_rep] = u_rep
            self.size[u_rep] += self.size[v_rep]
        else:
            self.rep[u_rep] = v_rep
            self.size[v_rep] += self.size[u_rep]
