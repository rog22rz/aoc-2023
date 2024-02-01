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

def findNewSeedRanges(aRange, source, length):
    offset = int(aRange[1]) - int(aRange[0])
    mapRangeStart, mapRangeEnd = int(aRange[1]), int(aRange[1]) + int(aRange[2])
    seedStart, seedLength, seedEnd = int(source), int(length), int(source) + int(length)
    newRanges = []
    #Merge intervals problem. Need to handle 6 cases
    #1. end < rangeStart
    if seedEnd <= mapRangeStart:
        newRanges.append([seedStart, seedLength])
    #2. start < rangeStart and end > rangeStart and end < rangeEnd
    elif seedStart < mapRangeStart and seedEnd > mapRangeStart and seedEnd <= mapRangeEnd:
        newRanges.append([seedStart, mapRangeStart - seedStart])
        newRanges.append([mapRangeStart - offset, seedEnd - mapRangeStart])
    #3. start > rangeStart and start < rangeEnd and end > rangeEnd
    elif seedStart >= mapRangeStart and seedStart < mapRangeEnd and seedEnd >= mapRangeEnd:
        newRanges.append([seedStart - offset, mapRangeEnd - seedStart])
        newRanges.append([mapRangeEnd, seedEnd - mapRangeEnd])
    #4. start < rangeStart and end > rangeEnd
    elif seedStart < mapRangeStart and seedEnd >= mapRangeEnd:
        newRanges.append([seedStart, mapRangeStart - seedStart])
        newRanges.append([mapRangeStart - offset, mapRangeEnd - mapRangeStart])
        newRanges.append([mapRangeEnd, seedEnd - mapRangeEnd])
    #5. start > rangeStart and end < rangeEnd
    elif seedStart >= mapRangeStart and seedEnd < mapRangeEnd:
        newRanges.append([seedStart - offset, seedEnd - seedStart])
    #6. start > rangeEnd
    elif seedStart >= mapRangeEnd:
        newRanges.append([seedStart, seedLength])
    print("newRanges", newRanges)
    return newRanges

def processFile(file):
    global allMaps
    currentMap = GenericMap("tmp", "tmp") 
    minLocation = float("inf") 

    #Process file data
    line = file.readline()
    seedRanges = line.strip().split(" ")[1:]
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
    
    #For each map, go through the seed ranges, and apply the map to obtain new seed ranges
    currentKey = START_MAP
    while currentKey in allMaps:
        currentMap = allMaps[currentKey]
        i = 0
        newSeedRanges = []
        while i+1 < len(seedRanges):
            source = int(seedRanges[i])
            length = int(seedRanges[i+1])
            for aRange in currentMap.ranges:
                print("aRange", aRange)
                for r in findNewSeedRanges(aRange, source, length):
                    newSeedRanges.append(r[0])
                    newSeedRanges.append(r[1])
            i += 2
        seedRanges = newSeedRanges
        if currentMap.mapSource == "seed":
            print("seedRanges", seedRanges)
            sys.exit()
        currentKey = currentMap.mapDestination

    #Look for min location if final ranges
    for i, r in enumerate(seedRanges):
        if i % 2 == 0:
            minLocation = min(minLocation, r)

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

