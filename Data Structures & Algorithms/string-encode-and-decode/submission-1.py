class Solution:

    def encode(self, strs: List[str]) -> str:
        newString = ''
        for i in strs:
            newString += i + ';-;'
        return newString

    def decode(self, s: str) -> List[str]:
        newList = s.split(';-;')
        newList.pop()
        return newList