import sys

# Could be greatly improved by making findLowerRange and findUpperRange binary searches for their respective ranges.
# You would know you have found the lowerRange if distance for holdLength - 1 is < winningDistance whereas 
# distance for holdLength + 1 > winningDistance. Reverse that logic for upperRange
# Similarly, for lowerRange, look for left of binarySearch if distances are increasing and distance < winningDistance.
# Follow same logic for upperRange. 

def findLowerRange(raceLength, winningDistance):
    holdLength = 0
    distance = holdLength * (raceLength - holdLength)
    while distance <= winningDistance:
        holdLength += 1
        distance = holdLength * (raceLength - holdLength)
    return holdLength

def findUpperRange(raceLength, winningDistance):
    holdLength = raceLength - 1
    distance = holdLength * (raceLength - holdLength)
    while distance <= winningDistance:
        holdLength -= 1
        distance = holdLength * (raceLength - holdLength)
    return holdLength

def processFile(file):
    firstLine = file.readline()
    parts = firstLine.split()
    raceLength = int(''.join(map(str, parts[1:])))
    secondLine = file.readline()
    parts = secondLine.split()
    winningDistance = int(''.join(map(str, parts[1:])))

    lowerRange = findLowerRange(raceLength, winningDistance)
    upperRange = findUpperRange(raceLength, winningDistance)

    return upperRange - lowerRange + 1

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

