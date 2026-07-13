g = {'A':['B','C'], 'B':['D'], 'C':['E'], 'D':[], 'E':[]}

v = set()
print("DFS:")

def dfs(n):
    if n not in v:
        print(n, end=" ")
        v.add(n)
        for i in g[n]:
            dfs(i)

dfs('A')
