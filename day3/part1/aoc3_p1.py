import sys

lines = []
isAdjacent = set()
cur = ""

def checkIfAdjacent(r, c):
    cNeigh = rNeigh = [-1, 0, 1]
    for rn in rNeigh:
        for cn in cNeigh:
            if min(r+rn, c+cn) >= 0 and r+rn < len(lines) and c+cn < len(lines[r]) and (lines[r+rn][c+cn] != "." and not lines[r+rn][c+cn].isdigit()):
                return True
    return False

def processArrayElement(r, c):
    global cur
    ans = 0
    
    if lines[r][c].isdigit():
        cur += lines[r][c]
        if c-1 >= 0 and (r, c-1) in isAdjacent:
            isAdjacent.add((r, c))
        else:
            if checkIfAdjacent(r, c):
                isAdjacent.add((r, c))

    if (c+1 < len(lines[r]) and not lines[r][c+1].isdigit() or c+1 >= len(lines[r])) and (r, c) in isAdjacent:
        ans = int(cur)

    if not lines[r][c].isdigit():
        cur = ""
   
    return ans        


def processFile(file):
    r, c = 0, 0
    sum = 0
    global lines 
    lines = [line.strip() for line in file]
    for r in range(len(lines)):
        for c in range(len(lines[r])):
            sum += processArrayElement(r, c)
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

