import sys

rankMap = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "1": 1,
        } 

def sortSameHand(hand):
    return tuple(rankMap[c] for c in hand)

def sortHands(hand):
    hmap = {}
    for card in hand:
        hmap[card] = 1 + hmap.get(card, 0)
    if 5 in hmap.values():
        return 7
    if 4 in hmap.values():
        return 6
    if 3 in hmap.values() and 2 in hmap.values():
        return 5
    if 3 in hmap.values():
        return 4
    if list(hmap.values()).count(2) == 2:
        return 3
    if 2 in hmap.values():
        return 2
    return 1

def sortKey(handTuple):
    return sortHands(handTuple[0]), sortSameHand(handTuple[0])

def processFile(file):
    allHands = []
    for line in file:
        parsedLine = line.strip().split()
        allHands.append(parsedLine)
    sortedHands = sorted(allHands, key=sortKey)

    totalScore = 0
    for i, hand in enumerate(sortedHands):
        totalScore += (i+1) * int(hand[1])
    return totalScore

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


