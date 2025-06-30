# title: Accounts Merge
# timestamp: 2025-06-05 15:03:41
# problemUrl: https://leetcode.com/problems/accounts-merge/
# memory: 20.8 MB
# runtime: 235 ms

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        names = {}
        parents = {}
        def find(email):
            if email not in parents:
                parents[email] = email 
            if parents[email] == email:
                return email
            return find(parents[email])

        def union(email1, email2):
            parents[find(email2)] = find(email1)
        
        for account in accounts:
            name, *emails = account
            emails = list(set(emails))
            names[emails[0]] = name
            find(emails[0])
            for email in emails[1:]:
                union(emails[0], email)
            # print(parents)


        accounts = {}
        for email in parents:
            parent = find(email)
            if parent not in accounts:
                accounts[parent] = []
            accounts[parent].append(email)

        return [[names[email]] + sorted(emails) for email, emails in accounts.items()]
