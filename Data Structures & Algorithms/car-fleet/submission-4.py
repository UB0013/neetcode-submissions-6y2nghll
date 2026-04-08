class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined =[]
        timeset =[0]
        for i in range (len(speed)):
            combined.append((position[i],speed[i]))
        combined = sorted (combined, reverse= True)
        print(combined)
        for p, s in combined:
            time = (target-p)/s
            if time > timeset [-1]:
                timeset.append(time)
        return len(timeset)-1




        return 0
        