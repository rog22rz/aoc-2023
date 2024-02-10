import sys

def processFile(file):
    ans = 1 
    firstLine = file.readline()
    parts = firstLine.split()
    raceLengths = [int(part) for part in parts if part.isdigit()]
    secondLine = file.readline()
    parts = secondLine.split()
    distances = [int(part) for part in parts if part.isdigit()]

    for i in range(len(raceLengths)):
        winCount = 0
        raceLength = raceLengths[i]
        for holdTime in range(raceLength):
            speed = raceLength - holdTime
            dist = holdTime * speed
            if dist > distances[i]:
                winCount += 1
        ans *= winCount

    return ans

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


