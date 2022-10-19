from readline import get_begidx
from typing import Dict, List, Mapping
from dataclasses import dataclass
import math

def computeStandardTuningFundamental(stringNo, fret):
    standardTuning = [40, 45, 50, 55, 59, 64]
    midi = standardTuning[stringNo] + fret
    return 2**((midi-69)/12)*440

def computeStandardTuningMidi(fundamental):
    return round(12* math.log2(fundamental/440) + 69)

@dataclass
class Position:
    stringNo: int
    fretNo: int

    def __str__(self):
        return 'fret: ' + str(self.stringNo) +'string: ' + str(self.fretNo)

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return (self.stringNo == other.stringNo) and (self.fretNo == other.fretNo)

@dataclass
class FretBeta:
    position: Position
    beta: float

@dataclass
class FretBoard:
    # size_strings: int
    # size_frets: int
    fretboard: Mapping[Position, FretBeta]
    standardTuning = [40, 45, 50, 55, 59, 64]

    @classmethod
    def fromJson(cls, jsonDict: Dict): 
        """example structure
        {string1:{
                fret1: beta1,fret2:beta2..
                }
            string2:{
                fret1: beta21, ...
                }
                ...
        }
        """
        fretboardDict = {}
        for stringNo, value in jsonDict.items():
            for fretNo, beta in value.items():
                f = Position(stringNo, fretNo)
                b = FretBeta(f, beta)
                fretboardDict[f] = b
        return FretBoard(fretboardDict)

    def getBeta(self, stringNo, fret) -> FretBeta:
        sf = Position(stringNo, fret)
        return self.fretboard[sf]



    def getPositionsWithFundamental(self, fundamental):
        midi = computeStandardTuningMidi(fundamental)
        res = []
        for stringNo, openMidi in enumerate(self.standardTuning):
            if (24 >= midi - openMidi >= 0):
                res.append(self.getBeta(stringNo, midi-openMidi))
        return res

