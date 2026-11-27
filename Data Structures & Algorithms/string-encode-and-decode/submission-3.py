class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += str(len(i))+"#"+i
        return(s) 

    def decode(self, s: str) -> List[str]:
        i = 0
        le = ""
        temp = []

        while i < len(s):
            if s[i] != "#":
                le += s[i]
                i += 1
            else:
                t = s[i+1:i+1+int(le)]
                i = i + 1 + int(le)
                le = ""
                temp.append(t)

        return temp


