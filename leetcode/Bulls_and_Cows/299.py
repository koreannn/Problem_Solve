class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            elif guess[i] in set(secret):
                cows += 1
        
        return str(bulls) + "A" + str(cows) + "B"

# test
print(Solution().getHint("1807", "7810")) # "1A3B"
print(Solution().getHint("1123", "0111")) # "1A1B"

