class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    cols = [set() for x in range(9)]
    rows = [set() for x in range(9)]
    grps = dict(((x,y),set())  for x in range(3) for y in range(3))

    ndig = 0
    for m,row in enumerate(board):
      for n,x in enumerate(row):
        if x == ".": continue
        d = int(x)
        cols[n].add(d); rows[m].add(d); grps[(m//3,n//3)].add(d)
        ndig += 1
    
    if sum(len(x) for x in cols)!=ndig: return False
    if sum(len(x) for x in rows)!=ndig: return False
    if sum(len(x) for x in grps.values())!=ndig: return False

    return True