class Solution:
    # Corner cases:
    # if strs = [] -> return "" -> return []
    # if strs = [""] -> return "" -> return [""]

    # if strs = [","]

    # if strs = [" "]

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "ñ"
        return "é".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "ñ":
            return []
        return s.split("é")
