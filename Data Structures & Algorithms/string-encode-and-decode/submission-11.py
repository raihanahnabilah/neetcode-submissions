class Solution:

    # natural instict: to include the ","
    # but idont think it goes well though bcs it's a UTF-8 characters

    # so we wanna do another character

    def encode(self, strs: List[str]) -> str:
        # Method 1
        # if len(strs) == 0: 
        #     return ""            
        # return ",".join(strs)

        # Method 2
        res = []
        for string in strs:
            stringLength = len(string)
            res.append(str(stringLength) + "$" + string)        
        return "".join(res)
            

    def decode(self, s: str) -> List[str]:
        # Method 1
        # if s == "":
        #     return []
        # return s.split(",")

        # Method 2
        res = []
        if len(s) == 0:
            return res
        # print("Checking s", s)
        # arrayS = s.split("$")
        # print("ArrayS", arrayS)
        print(s)
        
        i = 0
        while i < len(s):
            findLengthIndex = i
            while s[findLengthIndex] != "$":
                findLengthIndex += 1
            lengthString = int(s[i:findLengthIndex])

            startStringIndex = findLengthIndex + 1
            endStringIndex = startStringIndex + lengthString
            res.append(s[startStringIndex:endStringIndex])
            i = endStringIndex


        # for i, char in enumerate(s):
        #     if char == "$" and s[i+1].isnumeric():
        #         print("true")
        #         startIndex = i+2
        #         endIndex = startIndex + int(s[i+1])
        #         print("checking s",startIndex, endIndex, s[startIndex:endIndex])
        #         res.append(s[startIndex:endIndex])
        #     else:
        #         continue
        return res

