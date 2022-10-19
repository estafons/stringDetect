import math
from stringDetect.models import FretBoard, Position
from typing import Dict

def simpleModel(fretBetas: Dict):
    """
        example Dict structure
        {string1:{
                freti: betai}
                }
            string2:{
                freti: betaij}
                }
                ...
        }
        """
    fretboardDict = {}
    for stringNo, beta in fretBetas.items():
        fretboardDict[stringNo] = {0: beta}
        for fret in range(1, 24):
            betaF_S = beta*2**(fret/6)
            fretboardDict[stringNo][fret] = betaF_S
    fretboard = FretBoard.fromJson(fretboardDict)
    #print(fretBoard)
    return fretboard



def detectString(fretboard: FretBoard, inharmonicity: float, fundamental) -> Position:
    positions = fretboard.getPositionsWithFundamental(fundamental)
    closestDiff = 10
    for position in positions:
        currDiff = abs(position.beta - inharmonicity)
        if  currDiff < closestDiff:
            closestDiff = currDiff
            currPos = position
    return currPos
    
    