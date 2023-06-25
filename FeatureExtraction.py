import csv
import pywt
import numpy as np
# import scipy.signal
# import matplotlib.pyplot as plt
# from scipy.fftpack import fft, ifft
# from statsmodels.tsa.ar_model import AutoReg


def wavelet_features(preprocessed_signals, wavelet, level):

    features = []
    for signal in preprocessed_signals:
        # Compute the DWT of the preprocessed signal
        coeffs = pywt.wavedec(signal, wavelet, level=level)
        res = coeffs[0]
        features.append(res)
    
    wavelets = 'wavelets_data.csv'
    # Save the reconstructed data
    with open(wavelets, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Freq', 'Data'])  # Write header
        writer.writerows(zip(range(len(features)), features))  # Write data row


    print("DWT Is Done \n")
    return features



def morphology_features (preprocessed_signals):
    features = []
    for signal in preprocessed_signals:
        mean = np.mean(signal)
        maximum = np.max(signal)
        minimum = np.min(signal)
        std_dev = np.std(signal)

        signalfeatures = [mean, maximum,minimum,std_dev]
        features.append(signalfeatures)

    print("MOR Is Done \n")

    return features



'''

def PSD_features(filt_signals, sampling_rate):

    features = []
    for signal in filt_signals:
        signal = fft(signal)
        N = len(signal)
        n= np.arange(N)
        T=N/sampling_rate
        freq = n/T
        features.append(freq)

    
    psd = 'PSD_data.csv'
    # Save the reconstructed data
    with open(psd, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Freq', 'Data'])  # Write header
        writer.writerows(zip(range(len(features)), features))  # Write data rows
 

    print("PSD Is Done \n")
    return features
'''