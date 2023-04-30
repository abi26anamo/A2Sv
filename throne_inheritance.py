class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.inheritance_heirarchy = defaultdict(list)
        self.deads = set()
        
    def birth(self, parentName: str, childName: str) -> None:
        self.inheritance_heirarchy[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deads.add(name)

    def getInheritanceOrder(self) -> List[str]:
        curOrder = []
        def dfs(node):
            
            for child in self.inheritance_heirarchy[node]:
                if child not in self.deads:
                    curOrder.append(child)
                
                if child in self.inheritance_heirarchy:
                    dfs(child)
            return curOrder
        if self.kingName not in self.deads:
            curOrder.append(self.kingName)
            
        return dfs(self.kingName)
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
