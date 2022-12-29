class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        for i in range(len(cpdomains)):
            cpdomains[i] = cpdomains[i].split(" ")
            cpdomains[i][1] = cpdomains[i][1].split(".")
        dictionary ={}
        for x in cpdomains:
            l = len(x[1])
            i = 0
            for i in range(l):
                cd = ".".join(x[1][i:l])
                dictionary[cd] = dictionary.get(cd, 0) + int(x[0])
                i+=1
        output = []
        for x in dictionary:
            value  = dictionary[x]
            output.append(f'{value} {x}')
        return output
            
            
