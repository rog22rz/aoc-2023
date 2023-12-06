import sys

def getCalibrationValue(line):
    firstDigit, lastDigit = 0, 0
    for c in line:
        if c.isdigit():
            firstDigit = c
            break
    for c in line[::-1]:
        if c.isdigit():
            lastDigit = c
            break
    return firstDigit + lastDigit;

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

