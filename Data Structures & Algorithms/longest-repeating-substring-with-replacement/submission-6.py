class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # length of window - most freq character <= k to be valid
        # to check validity, we will use:
        # r - l + 1 - h[most_freq_char] <= k
        # use hashmap to keep track of character frequency

        l = 0
        max_length = 0
        freq_count = [0] * 26
        for r in range(len(s)):
            freq_count[ord(s[r]) - ord("A")] += 1
            while r - l + 1 - max(freq_count) > k: # max(freq_count) -> O(26)
                freq_count[ord(s[l]) - ord("A")] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)
        
        return max_length