''' idea :  can use the sliding window approach for problems of the type which requires us to find longest substrings. 
            typically, a start and an end pointer, until we get a repeated character, we keep increasing the end pointer
            else, we move the start pointer'''

def lengthOfLongestSubstring(self, s):
        charMap = {}
        for i in range(256):
            charMap[i] = -1
        ls = len(s)
        i = max_len = 0
        for j in range(ls):
            # Note that when charMap[ord(s[j])] >= i, it means that there are
            # duplicate character in current i,j. So we need to update i.
            if charMap[ord(s[j])] >= i:
                i = charMap[ord(s[j])] + 1
            charMap[ord(s[j])] = j
            max_len = max(max_len, j - i + 1)
        return max_len
