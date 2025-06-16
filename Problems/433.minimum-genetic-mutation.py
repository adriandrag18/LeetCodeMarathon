# title: Minimum Genetic Mutation
# timestamp: 2025-06-16 15:37:54
# problemUrl: https://leetcode.com/problems/minimum-genetic-mutation/
# memory: 18 MB
# runtime: 0 ms

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank: 
            return -1

        def mutate(gene):
            res = []
            l = [c for c in gene]
            for i, c in enumerate(l):
                for new in 'ACGT':
                    if new == c:
                        continue
                    l[i] = new
                    s = ''.join(l)
                    if i == 7:
                        print(s)
                    if s in bank:
                        res.append(s)
                    l[i] = c
            print(gene, res)
            return res                    
        
        def dfs(gene, depth):
            if gene in seen:
                return depth
            seen.add(gene)

            if gene == endGene:
                return depth

            for mutated in mutate(gene):
                if mutated not in seen:
                    if (res := dfs(mutated, depth + 1)) != -1:
                        return res
            
            return -1
        
        seen = set()
        return dfs(startGene, 0)

