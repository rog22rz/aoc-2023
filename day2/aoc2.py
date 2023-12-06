import sys

def processFile(filePath):
    try:
        with open(filePath, 'r') as file:
            print("test")
    except Exception as e:
        print(f"Error while opening file: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py filename")
    else:
        file_path = sys.argv[1]
        processFile(file_path)


