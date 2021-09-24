class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        unitsByType = [i[1] for i in boxTypes]
        boxIn = 0
        filling = 0
        while True:
            maxUnit = max(unitsByType)
            maxUnitPos = unitsByType.index(maxUnit)
            unitsByType[maxUnitPos] = 0
            for i in range(boxTypes[maxUnitPos][0]):
                filling += maxUnit
                boxIn += 1
                if boxIn+1 > truckSize:
                    return filling