from bisect import bisect_left, bisect_right

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        pos = []
        digits = []

        for i, ch in enumerate(s):
            if ch != '0':
                pos.append(i)
                digits.append(int(ch))

        k = len(digits)

        # powers of 10
        pow10 = [1] * (k + 1)
        for i in range(1, k + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # prefix number
        prefNum = [0] * (k + 1)
        for i in range(1, k + 1):
            prefNum[i] = (prefNum[i - 1] * 10 + digits[i - 1]) % MOD

        # prefix digit sums
        prefSum = [0] * (k + 1)
        for i in range(1, k + 1):
            prefSum[i] = prefSum[i - 1] + digits[i - 1]

        ans = []

        for l, r in queries:
            left = bisect_left(pos, l)
            right = bisect_right(pos, r) - 1

            if left > right:
                ans.append(0)
                continue

            L = left + 1      # 1-based
            R = right + 1

            length = R - L + 1

            x = (prefNum[R] - prefNum[L - 1] * pow10[length]) % MOD
            digit_sum = prefSum[R] - prefSum[L - 1]

            ans.append((x * digit_sum) % MOD)

        return ans