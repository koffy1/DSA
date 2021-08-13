class Solution:
    def spiralOrder(self, matrix):
        startRow = 0
        startColumn = 0
        endRow = len(matrix)
        endColumn = len(matrix[0])
        outputArray = []
        numberVisited = len(matrix) * len(matrix[0])
        while 0 < numberVisited:
            counter = startColumn
            while counter < endColumn and numberVisited > 0:
                outputArray.append(matrix[startRow][counter])
                numberVisited -= 1
                counter += 1
            counter = startRow + 1
            while counter < endRow and numberVisited > 0:
                outputArray.append(matrix[counter][endColumn - 1])
                numberVisited -= 1
                counter += 1
            counter = endColumn - 1
            while counter > startColumn and numberVisited > 0:
                outputArray.append(matrix[endRow - 1][counter - 1])
                numberVisited -= 1
                counter -= 1
            counter = endRow - 1
            while counter > startRow + 1 and numberVisited > 0:
                outputArray.append(matrix[counter - 1][startColumn])
                numberVisited -= 1
                counter -= 1
            
            startRow += 1
            startColumn += 1
            endRow -= 1
            endColumn -= 1
        return outputArray