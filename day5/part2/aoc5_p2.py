import sys

allMaps = {}
START_MAP = "seed"

class GenericMap:
    def __init__(self, mapSource, mapDestination):
        self.mapSource = mapSource
        self.mapDestination = mapDestination
        self.ranges = []

    def appendRange(self, range):
        self.ranges.append(range)

def findRange(seedNumber):
    global START_MAP
    closestSource = float("inf")

    for destination, source, length in allMaps[START_MAP].ranges:
        destination, source, length = int(destination), int(source), int(length)
        if seedNumber >= source and seedNumber < source + length:
            return (source + length) - seedNumber
        if source > seedNumber:
            closestSource = min(closestSource, abs(source-seedNumber))

    return closestSource

def findLocation(seedNumber):
    global START_MAP
    currentKey = START_MAP 
    currentVal = int(seedNumber)

    while currentKey in allMaps:
        currentMap = allMaps[currentKey]
        for destination, source, length in currentMap.ranges:
            destination, source, length = int(destination), int(source), int(length)
            if currentVal >= source and currentVal < source + length:
                currentVal = currentVal - source + destination 
                break
        currentKey = currentMap.mapDestination

    return currentVal
    

def processFile(file):
    line = file.readline()
    seeds = line.strip().split(" ")[1:]
    global allMaps
    currentMap = GenericMap("tmp", "tmp") 
    minLocation = float("inf") 

    while line:
        line = file.readline()
        if len(line.strip()) > 0: 
            if line[0].isalpha(): 
                sourceAndDestination = line.split(" ")[0].split("-")
                source = sourceAndDestination[0]
                destination = sourceAndDestination[2]
                currentMap = GenericMap(source, destination)
                allMaps[source] = currentMap
            else:
                currentMap.appendRange(line.strip().split(" "))
    
    i = 0
    while i+1 < len(seeds):
        source = int(seeds[i])
        length = int(seeds[i+1])
        seedIndex = source
        while seedIndex < source + length:
            minLocation = min(minLocation, findLocation(seedIndex))
            seedIndex += findRange(seedIndex)
        i += 2

    return minLocation

def openFile(filePath):
    try:
        with open(filePath, 'r') as file:
            answer = processFile(file)
            print(f"Answer: {answer}")

    except Exception as e:
        print(f"Error while opening file: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py filename")
    else:
        file_path = sys.argv[1]
        openFile(file_path)

