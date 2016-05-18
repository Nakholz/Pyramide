def createPyramid(file):
    myFile = open(file,'r')
    pyr=[]
    for line in myFile:
        line = line.split()
        line = [int(x) for x in line]
        pyr.append(line)
    return pyr

pyr= createPyramid("pyramide.txt")

def next(x, y, current, it):
  if it + 1 >= len(pyr) :
    print current
    return current
  elif pyr[y+1][x] > pyr[y+1][x+1]:
    print "left"
    current += pyr[y+1][x]
    it += 1;
    next(x, y+1, current, it)
  elif pyr[y+1][x] < pyr[y+1][x+1]:
    print "right"
    current += pyr[y+1][x+1]
    it += 1;
    next(x+1, y+1, current, it)

result = next(0, 0, pyr[0][0], 0);
