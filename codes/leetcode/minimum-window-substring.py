class Solution:
    def minWindow(self, s: str, t: str) -> str:

        return 'INVALID'


if __name__ == '__main__':

    s = "ADOBECODEBANC"
    t = "ABC"
    sol = Solution()
    r = sol.minWindow(s, t)
    print(r)
    if r == 'BANC':
        print('ok')


