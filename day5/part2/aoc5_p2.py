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

def findNewSeedRanges(seedRanges, mapRange):
    i = 0
    newSeedRanges = []
    oldSeedRanges = []
    while i < len(seedRanges):
        # Variables relating to each seed ranges
        seedStart, seedLength = int(seedRanges[i]), int(seedRanges[i+1])
        seedEnd = seedStart + seedLength
        # Variables relating to each map range
        offset = int(mapRange[1]) - int(mapRange[0])
        mapRangeStart, mapRangeEnd = int(mapRange[1]), int(mapRange[1]) + int(mapRange[2])
        # Merge intervals problem. Need to handle 6 cases
        # 1. end < rangeStart
        if seedEnd <= mapRangeStart:
            oldSeedRanges.extend([seedStart, seedLength])
        # 2. start < rangeStart and end > rangeStart and end < rangeEnd
        elif seedStart < mapRangeStart and seedEnd > mapRangeStart and seedEnd <= mapRangeEnd:
            oldSeedRanges.extend([seedStart, mapRangeStart - seedStart])
            newSeedRanges.extend([mapRangeStart - offset, seedEnd - mapRangeStart])
        # 3. start > rangeStart and start < rangeEnd and end > rangeEnd
        elif seedStart >= mapRangeStart and seedStart < mapRangeEnd and seedEnd >= mapRangeEnd:
            newSeedRanges.extend([seedStart - offset, mapRangeEnd - seedStart])
            if seedEnd != mapRangeEnd:
                oldSeedRanges.extend([mapRangeEnd, seedEnd - mapRangeEnd])
        # 4. start < rangeStart and end > rangeEnd
        elif seedStart < mapRangeStart and seedEnd >= mapRangeEnd:
            oldSeedRanges.extend([seedStart, mapRangeStart - seedStart])
            newSeedRanges.extend([mapRangeStart - offset, mapRangeEnd - mapRangeStart])
            oldSeedRanges.extend([mapRangeEnd, seedEnd - mapRangeEnd])
        # 5. start > rangeStart and end < rangeEnd
        elif seedStart >= mapRangeStart and seedEnd < mapRangeEnd:
            newSeedRanges.extend([seedStart - offset, seedEnd - seedStart])
        # 6. start > rangeEnd
        elif seedStart >= mapRangeEnd:
            oldSeedRanges.extend([seedStart, seedLength])
        i += 2

    return [newSeedRanges, oldSeedRanges]

def processFile(file):
    global allMaps
    currentMap = GenericMap("tmp", "tmp") 
    minLocation = float("inf") 

    # Process file data
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
    
    # For each map, apply mapRanges to seedRangse. Similar to applying mappings in place.
    currentKey = START_MAP
    while currentKey in allMaps:
        currentMap = allMaps[currentKey]
        i = 0
        newSeedRange, oldSeedRange = [], []
        for mapRange in currentMap.ranges:
            new, oldSeedRange = findNewSeedRanges(seedRanges, mapRange)
            newSeedRange.extend(new)
            seedRanges = oldSeedRange
        newSeedRange.extend(oldSeedRange)
        seedRanges = newSeedRange
        currentKey = currentMap.mapDestination

    # Look for min location if final ranges
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

