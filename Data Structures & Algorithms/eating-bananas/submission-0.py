'''
fastest timeTaken = len(piles)
h must be >= len(piles)
for fastest timeTaken, rate is max(piles)
optimal k exists between 1 and max(piles)
i.e. 1 <= k <= max(piles)

use binary search to find optimal k
1. k = max(piles) // 2
   calculate timeTaken
   check with h
   if timeTaken < h, half k again and check
   if timeTaken > h, set k = halfway point between when timeTaken < h, and current k
   need to keep track of last k where timeTaken > h, and last k where timeTaken < h
'''

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def calculateTimeTaken(piles: list[int], k: int) -> int:
            totalTimeTaken = 0
            for pile in piles:
                timeTakenForPile = -(-pile // k) # ceiling division
                totalTimeTaken += timeTakenForPile
            return totalTimeTaken

        # k: max(piles) -> timeTaken < h
        # k: 1 -> timeTaken >= h
        # maintain two states of k
        low_k, high_k = 1, max(piles)

        # binary search between low_k and high_k, recording k when timeTaken <= h
        res = high_k
        while low_k <= high_k:
            k = (low_k + high_k) // 2
            t = calculateTimeTaken(piles, k)
            if t <= h:
                res = k
                high_k = k - 1
            else:
                low_k = k + 1
        return res
