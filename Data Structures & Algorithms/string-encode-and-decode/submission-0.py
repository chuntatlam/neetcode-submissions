'''
encode:
list of str -> join with delimiter outside of 256 valid ASCII characters
e.g. \u241f

decode:
encoded.split(delimiter)
'''

class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter = "\u241f"
        return delimiter.join(strs)

    def decode(self, s: str) -> List[str]:
        delimiter = "\u241f"
        return s.split(delimiter)
