import sys

visited = set()

def checkRight(r, c) -> str:
    if c >= len(lines[r]):
        return ""
    elif lines[r][c].isdigit():
        visited.add((r, c))
        return lines[r][c] + checkRight(r, c+1)
    else:
        return ""

def checkLeft(r, c) -> str:
    if c < 0:
        return ""
    elif lines[r][c].isdigit():
        visited.add((r, c))
        return checkLeft(r, c-1) + lines[r][c]
    else:
        return ""

def processGear(r, c) -> int:
    global visited
    rNeigh = cNeigh = [-1, 0, 1]
    count = 0
    product = 1
    for rn in rNeigh:
        for cn in cNeigh:
            curNumber = ""
            if min(r+rn, c+cn) >= 0 and r < len(lines) and c < len(lines[r]) and lines[r+rn][c+cn].isdigit() and not (r+rn, c+cn) in visited and count < 3:
                visited.add((r+rn, c+cn))
                count += 1
                curNumber += lines[r+rn][c+cn]
                curNumber = checkLeft(r+rn, c+cn-1) + curNumber
                curNumber = curNumber + checkRight(r+rn, c+cn+1)
                product *= int(curNumber)
    return product if count == 2 else 0

def processFile(file):
    r, c = 0, 0
    sum = 0
    global lines 

    lines = [line.strip() for line in file]
    for r in range(len(lines)):
        for c in range(len(lines[r])):
            if lines[r][c] == "*":
                sum += processGear(r, c)
    return sum

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

