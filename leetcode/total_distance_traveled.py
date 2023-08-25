class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # set variable for distance
        dist = 0
        # loops when mainTank is greater or equal to 5
        # adds 50 to distance, subtracts 5 from mainTank
        # then if additional tank is equal or greater than 1, subtract 1 from additional and add one to main
        while mainTank >= 5:
            dist += 50
            mainTank -= 5
            if additionalTank >= 1:
                additionalTank -= 1
                mainTank += 1
        # once the above loop is finished, we now empty the rest of the main tank 1L at a time
        while mainTank > 0:
            dist += 10
            mainTank -= 1
        return dist