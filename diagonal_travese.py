   n = len(mat)
        m = len(mat[0])
        dic = defaultdict(list)
        res=[]

        for r in range(n):
            for c in range(m):
                dic[r+c].append(mat[r][c])

        for elem in dic:
            if elem%2:
                res.append(dic[elem])
            else:
                res.append(dic[elem][::-1])
        out =[]
        for i in res:
            for j in i:
                out.append(j)
        return out
    
