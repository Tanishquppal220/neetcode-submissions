class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            temp =  f"{len(i)} "
            for j in i:
                temp+=chr(ord(j)+3)
            res+=temp+" "
        return res
    def decode(self, s: str) -> List[str]:
        s = s.strip()
        if s == "":
            return []
        l = s.split(" ")
        # if l[0] == "0":
        #     return [""]
        res = []
        print(l)
        for i in range(0,len(l),2):
            print(l[i])
            if int(l[i]) == 0:
                res.append("") 
                continue
            temp = ""
            for j in l[i+1]:
                temp+=chr(ord(j)-3)
            res.append(temp)
        return res