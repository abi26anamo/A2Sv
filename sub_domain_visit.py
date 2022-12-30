class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        domain_count = defaultdict(int)
        
        for domain in cpdomains:
            
            count,domain = domain.split()
            count = int(count)
            domain_count[domain]+=count
            i=0
            while i <len(domain):
                if domain[i]!=".":
                    i +=1
                elif domain[i]=='.':
                    domain = domain[i+1:]
                    domain_count[domain]+=count
                    i=0
        res =''
        stack =[]
        for domain in domain_count:
            res+=str(domain_count[domain])+' '+domain
            stack.append(res)
            res =''
        return stack
            
