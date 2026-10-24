'''
encode:
for s in strs:
    get the length, e.g.
    use delimiter to signify end of the length
    e.g. strs: ["4444", "333"]
    encoded: 4,44443,333 -> using ',' as the delimiter
    need delimiter because s could start with a number too

decode:
take the encoded string, s
get the length of first string
find the delimiter, convert the s before delimiter to int
e.g. 4,44443,333 find first ',' convert '4' to 4
the next 4 char in s is added to res []
repeat step to find next delimiter
if no more delimiter, end
'''

class Solution:

    delimiter = ","

    def encode(self, strs: List[str]) -> str:
        encoded_s = ""
        for s in strs:
            encoded_s += str(len(s)) + self.delimiter + s
        return encoded_s

    def decode(self, s: str) -> List[str]:
        i, res = 0, []
        while i < len(s):
            l = ""
            while s[i] != self.delimiter:
                l += s[i]
                i += 1
            l = int(l)
            i += 1
            res.append(s[i:i + l])
            i += l
            l = ""
        print(res)
        return res
