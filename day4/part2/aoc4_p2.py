import sys

def processFile(file):
    numberOfLines = 0
    for line in file:
        numberOfLines += 1
    file.seek(0)

    lines = [1] * numberOfLines
    sum = 0

    def processLine(index, line):
        numberOfWinningNumbers = 0
        cardSplit = line.split("|")
        winningNumbers = set(cardSplit[0].split()[2::])
        myNumbers = cardSplit[1].split()
        
        for n in myNumbers:
            if n in winningNumbers:
                numberOfWinningNumbers += 1

        for i in range(1, numberOfWinningNumbers+1):
            if index+i < len(lines):
                lines[index+i] += lines[index]
        return lines[index]

    index = 0
    for line in file:
        sum += processLine(index, line)
        index += 1
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

