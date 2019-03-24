
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        List , res_list = [] , []
        for i in range(len(s)):
            for j in range(len(s),i,-1):
                if s[i:j] == s[i:j][::-1]:
                    List.append(j-i)
                    res_list.append(s[i:j])
        if len(res_list) == 0:
            return ""
        else:
            m = List.index(max(List))
            return res_list[m]

s=Solution()
ret=s.longestPalindrome('abcba')
print(ret)

