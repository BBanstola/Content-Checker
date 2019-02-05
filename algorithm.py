import numpy as np

M=100
N=100
NALIGN=200

STOP=0
UP=1
LEFT=2
DIAG=3

MATCHSCORE=5
MISMATCHSCORE=-3
GAPSCORE=-4

def SmithWaterman(firstText,secondText):
    if len(firstText) == 0:
        return 0
    elif len(secondText) == 0:
        return 0

    M = 100
    N = 100
    NALIGN = 200

    STOP = 0
    UP = 1
    LEFT = 2
    DIAG = 3

    MATCHSCORE = 5
    MISMATCHSCORE = -3
    GAPSCORE = -4

    i=0
    j=0
    tmp=0
    length=0
    distance = np.empty([M, N])
    trace = np.empty([M, N])
    # alignX=np.empty([NALIGN])
    # alignY=np.empty([NALIGN])
    alignX = ["" for x in range(NALIGN)]
    alignY = ["" for x in range(NALIGN)]

    for i in range (0,len(firstText)):
        distance[i][0]=0
    for j in range(0, len(secondText)):
        distance[0][j] = 0
    for i in range (0,len(firstText)):
        trace[i][0]= STOP
    for j in range(0, len(secondText)):
        trace[0][j] = STOP

    minDist=0
    minI=0
    minJ=0

    for i in range (0,len(firstText)):
        for j in range(0, len(secondText)):
            dist=0
            trace[i][j]=STOP

            if firstText[i-1] ==secondText[j-1]:
                tmp=distance[i-1][j-1]-MATCHSCORE
            else:
                tmp=distance[i-1][j-1]-MISMATCHSCORE

            if tmp < dist:
                dist = tmp
                trace[i][j] =DIAG

            tmp = distance[i-1][j-1] - GAPSCORE

            if tmp < dist:
                dist=tmp
                trace[i][j]=UP

            tmp = distance[i][j - 1] - GAPSCORE
            if tmp < dist:
                dist = tmp
                trace[i][j] = LEFT

            distance[i][j]=dist

            if dist<minDist:
                minDist=dist
                minI=i
                minJ=j

    iAlign=0

    for i in range(len(firstText),minI,-1):
        alignY[iAlign]="*"
        alignX[iAlign]=firstText[i-1]
        iAlign=iAlign+1

    for j in range(len(secondText),minJ,-1):
        alignY[iAlign]=secondText[j-1]
        alignX[iAlign]="*"
        iAlign=iAlign+1

    while trace[i][j]!= STOP:
        if trace[i][j]==DIAG:
            alignY[iAlign] = secondText[j - 1]
            alignX[iAlign] = firstText[i - 1]
            i=i-1
            j=j-1
            iAlign=iAlign+1
        elif trace[i][j]==LEFT:
            alignY[iAlign] = secondText[j - 1]
            alignX[iAlign] = "-"
            j=j-1
            iAlign=iAlign+1
        elif trace[i][j]==UP:
            alignY[iAlign] = "-"
            alignX[iAlign] = firstText[i - 1]
            i=i-1
            iAlign=iAlign+1

    while i>0:
        alignY[iAlign] = 0
        alignX[iAlign] = firstText[i - 1]
        i=i-1
        iAlign=iAlign+1

    while j>0:
        alignY[iAlign] = secondText[j - 1]
        alignX[iAlign] = 0
        j=j-1
        iAlign=iAlign+1


    if len(firstText)< len(secondText):
        length=len(firstText)
    else:
        length=len(secondText)

    return (-1 * float((minDist)/(length)*100))










