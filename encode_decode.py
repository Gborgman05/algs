class Solution:

    def encode(self, strs: List[str]) -> str:
        return str(strs).replace("'", "").replace(" ", "")

    def decode(self, s: str) -> List[str]:
        print(s)
        if s == '[]':
            return []
        if s:
            return s.replace("[", "").replace("]", "").split(",")
        