import numpy as np
import glob

def ConvertLines2List (path):
    signal = open(path,'r')
    SignalLines = signal.readlines()
    Amplitudes = []
    for i in range(len(SignalLines) - 1):
        l = SignalLines[i + 1]
        Amplitudes.append(int(l))
    return Amplitudes


def GetSignals(path):
    Data = glob.glob(path)
    Signals = []
    for Label in Data:
        SignalsPath=glob.glob(Label+"/*")
        for SignalPath in SignalsPath :
            Signals.append(ConvertLines2List(SignalPath))
    return Signals