def getAStarIndices(cells, startIndex, endIndex):
{
    closedCells = getClosedCells(cells, startIndex, endIndex)
    if closedCells == None: return None
    if len(closedCells) == 0: return None

    AStarIndices = []
    traceCell = closedCells[len(closedCells)-1]
    while(traceCell.parentIndex != None):
        AStarIndices.append(traceCell.index);
        traceCell = traceCell.getParentCell(closedCells)
    AStarIndices = reversed(AStarIndices)
    return AStarIndices
}

def getClosedCells(cells, startIndex, endIndex):
{
    openCells = []
    closedCells = []

    openCells.append(AStarCell(startIndex, None, startIndex, endIndex))

    while True:
        openCells = sorted(openCells, key=lambda AStarCell: AStarCell.f)
        currentCell = openCells[0]
        closedCells.append(currentCell)
        openCells.pop(0)

        if closedCells[len(closedCells)-1].index.x == endIndex.x and closedCells[len(closedCells)-1].index.y == endIndex.y: break

        for adjacentCell in currentCell.getAdjacentCells(cells, startindex, endIndex):
            if adjacentCell.isInCellList(closedCells): continue
            if adjacentCell.isInCellList(openCell) == False: openCells.append(adjacentCell)

        if len(openCells <= 0): break

    return closedCells
}

class AStarCell:
{
    index = IntegerVector(0,0)
    parentIndex = IntegerVector(0,0)
    g = 0.0
    h = 0.0
    f = 0.0

    def __init__(self, index, parentIndex, startIndex, endIndex): 
        self.index = index
        self.parentIndex = parentIndex
        self.g = self.getIndexDistance(self.index, startIndex)
        self.h = self.getIndexDistance(self.index, endIndex);
        self.f = self.g + self.h

    def getIndexDistance(index, targetIndex):
        return abs(index.x-targetIndex.x) + abs(index.y-targetIndex.y)
    
    def getAdjacentCells(cells, startIndex, endIndex):
        adjacentCells = []
        for i in range(-1,2):
            for j in range(-1,2):
                if i*j != 0: continue
                adjacentIndex = IntegerVector(self.index.x + i, self.index.y + j)
                if adjacentIndex.x < 0 or adjacentIndex.y < 0 : continue
                if adjacentIndex.x >= len(cells) or adjacentIndex >= len(cells[0]): continue
                if cells[adjacentCell.x][adjacentCell.y] == None: continue
                adjacentCells.append(AStarCell(adjacentindex, self.index, startIndex, endIndex))
        return adjacentCells
    
    def isInCellList(cellList):
        for cell in cellList:
            if self.index.x == cell.index.x and self.index.y == cell.index.y: return True
        return False
    
    def getParentCell(cellList):
        for cell in cellList:
            if self.parentIndex.x == cell.index.x and self.parentIndex.y == cell.index.y: return cell
        return None  
}

class IntegerVector:
{
    x = 0
    y = 0

    def __init__(self, x, y): 
        self.x = x
        self.y = y
}