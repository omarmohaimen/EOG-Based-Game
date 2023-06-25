from scipy import signal
from scipy.signal import butter,filtfilt
import statistics
import numpy as np


def Butter_Bandpass_Filter(input_signals,low_cutt_off,high_cutt_off,sampling_rate,order):
    nyq_rate = 0.5 * sampling_rate
    f_low=low_cutt_off/nyq_rate
    f_high=high_cutt_off/nyq_rate
    filtered = []
    for signal in input_signals:
        Numerator,denominator = butter(order, [f_low,f_high], btype='band', output='ba', analog=False, fs=None)
        filtered.append(filtfilt(Numerator,denominator,signal))
    print("Butter_Bandpass_Filter Is Done \n")
    return filtered




def Resampling(Signals, SamplingRate):
    resampled_signals = []
    for Signal in Signals:
        resampled_signals.append(signal.resample(Signal,SamplingRate))
    print("Resampling Is Done \n")
    return resampled_signals



def DC_Component(Signals,Mode):
    # if mode = 1 the DC component will be added
    # if mode = -1 the DC component will be removed
    DC_Signals = []
    for Signal in Signals:
        Mean = statistics.mean(Signal)
        Mean = Mean * Mode
        DC_Signals.append([(Signal[i] + Mean) for i in range (len(Signal))])
    print("DC_Component Is Done \n")
    return DC_Signals



def GetConcatenateSignals (Signals):
    ConcatenatedSignals = []
    for i in range(0,len(Signals),2):
        ConcatenatedSignals.append(Signals[i] + Signals[i+1])
    return ConcatenatedSignals


