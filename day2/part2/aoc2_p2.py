import sys

def remove_non_alphanumeric_keep_spaces(string):
    return ''.join(e for e in string if e.isalnum() or e.isspace())

def computePower(line):
    minCubes = {"red": 0, "green": 0, "blue": 0}
    for i in range(len(line)):
        if line[i] in minCubes:
            minCubes[line[i]] = max(minCubes[line[i]], int(line[i-1]))
    power = 1
    for _, val in minCubes.items():
        power *= val
    return power


def parseFile(file):
    sum = 0
    for line in file:
        alnumLine = remove_non_alphanumeric_keep_spaces(line)
        alnumLine = alnumLine.split()
        sum += computePower(alnumLine)
    return sum

def processFile(filePath):
    try:
        with open(filePath, 'r') as file:
            answer = parseFile(file)
            print(f"Answer: {answer}")
    except Exception as e:
        print(f"Error while opening file: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py filename")
    else:
        file_path = sys.argv[1]
        processFile(file_path)
