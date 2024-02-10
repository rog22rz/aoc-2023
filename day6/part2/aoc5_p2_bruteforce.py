import sys

def processFile(file):
    ans = 1 
    firstLine = file.readline()
    parts = firstLine.split()
    raceLength = int(''.join(map(str, parts[1:])))
    secondLine = file.readline()
    parts = secondLine.split()
    winningDistance = int(''.join(map(str, parts[1:])))

    winCount = 0
    for holdTime in range(raceLength):
        speed = raceLength - holdTime
        dist = holdTime * speed
        if dist > winningDistance:
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

