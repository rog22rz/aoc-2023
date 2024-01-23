import sys

def processLine(line):
    product = 0
    cardSplit = line.split("|")
    winningNumbers = set(cardSplit[0].split()[2::])
    myNumbers = cardSplit[1].split()

    for n in myNumbers:
        if n in winningNumbers:
            if product == 0:
                product = 1
            else:
                product *= 2
    return product

def processFile(file):
    sum = 0
    for line in file:
        sum += processLine(line)
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

