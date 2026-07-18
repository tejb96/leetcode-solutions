class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs)==0:
            return ""
        min_cols = min(len(word) for word in strs)
        total_rows=len(strs)

        longest_prefix=[]

        for i in range(min_cols):
            all_match=True
            for j in range(1, total_rows):
                if(strs[j][i]!=strs[0][i]):
                    all_match=False
                    break
            if not all_match:
                break
            longest_prefix.append(strs[0][i])
        return ''.join(longest_prefix)




        