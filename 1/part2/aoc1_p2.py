import sys

def checkIsSpelledOut(line, charPointer):
    numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    for key, val in numbers.items():
        lengthOfNumber = len(key)
        l, r = charPointer, charPointer + lengthOfNumber
        if r <= len(line) and line[l:r] == key:
            return val
    return -1

def getCalibrationValue(line):
    firstDigit, lastDigit = 0, 0
    for i in range(len(line)):
        if line[i].isdigit():
            firstDigit = line[i]
            break
        else:
            spelledOut = checkIsSpelledOut(line, i)
            if spelledOut != -1:
                firstDigit = spelledOut
                break
    for i in range(len(line)-1, -1, -1):
        if line[i].isdigit():
            lastDigit = line[i]
            break
        else:
            spelledOut = checkIsSpelledOut(line, i)
            if spelledOut != -1:
                lastDigit = spelledOut
                break
    calibrationValue = str(firstDigit) + str(lastDigit);
    return calibrationValue; 

def processFile(filePath):
    try:
        with open(filePath, 'r') as file:
            sum = 0
            for line in file:
                sum += int(getCalibrationValue(line))
            print("The sum of all of the calibration values is: " + str(sum))
    except Exception as e:
        print(f"Error while opening file: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py filename")
    else:
        file_path = sys.argv[1]
        processFile(file_path)


