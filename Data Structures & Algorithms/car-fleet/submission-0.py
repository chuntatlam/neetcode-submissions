class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # arrange cars in order of position
        # calculate time taken to reach destination (time = distance / speed)
        timeTaken = [ (target - p) / s for p, s in sorted(zip(position, speed), key=lambda x: x[0]) ]
        
        # if car in front has greater time taken than car behind -> joined to a single fleet
        # e.g. timeTaken: [4, 5, 2, 3] -> [5, 5, 3, 3]
        # use stack to pop slower cars behind
        # e.g. timeTaken: [4, 5, 2, 3], stack: [4] -> [4,5], pop 4 [5] -> [5,2], 2 < 5, don't pop -> [5,2,3], pop 2 -> [5,3] 
        # end up with 2 fleets, each reaching destination at time 3 and 5

        stack = []
        for i in range(len(timeTaken)):
            # need to use math.isclose() for equality comparisons for float
            while stack and (timeTaken[i] > stack[-1] or math.isclose(timeTaken[i], stack[-1])):
                stack.pop()
            stack.append(timeTaken[i])
        return len(stack)