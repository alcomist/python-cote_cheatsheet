class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        used = {}
        max_len = 0
        start = 0
        for index, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char]+1
            else:
                max_len = max(max_len, index - start + 1)
            used[char] = index
        return max_len

if __name__ == '__main__':

    s = "abcabcbb"
    sol = Solution()
    if sol.lengthOfLongestSubstring(s) == 3:
        print('ok')

    s = "bbbbb"
    if sol.lengthOfLongestSubstring(s) == 1:
        print('ok')

    s = "pwwkew"
    if sol.lengthOfLongestSubstring(s) == 3:
        print('ok')
