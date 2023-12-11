import sys

RULES = {"red": 12, "green": 13, "blue": 14}

def remove_non_alphanumeric_keep_spaces(string):
    return ''.join(e for e in string if e.isalnum() or e.isspace())

def validateGame(line):
    for i in range(len(line)):
        if line[i] in RULES:
            if int(line[i-1]) > RULES[line[i]]:
                return 0
    return int(line[1])

def parseFile(file):
    sum = 0
    for line in file:
        alnumLine = remove_non_alphanumeric_keep_spaces(line)
        alnumLine = alnumLine.split()
        sum += validateGame(alnumLine)
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


