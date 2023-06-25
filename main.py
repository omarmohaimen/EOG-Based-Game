import Preprocessing as Pre
import ReadingSignals as RS
import Classification
import FeatureExtraction
import numpy as np
from matplotlib import pyplot as plt
def Get_Prepared_Signals(Signal_Type):
    """
        Args:
            Signal_Type (int): '1' for applying functions on Test Dataset.
                            & 'else' for applying functions on Train Dataset.
        Returns:
            list: Features of the selected data set.
        """
    if Signal_Type==1:
        Path ="Dataset/Test/*"
    else:
        Path = "Dataset/Train/*"
    # Get signals
    Signals = RS.GetSignals(Path)
    # PrintMovements(Signals)
    # concatenate Signals
    ConcSignals = Pre.GetConcatenateSignals(Signals)
    # PrintMovements(ConcSignals)

    # Filtering Signals
    Filtered_Signals = Pre.Butter_Bandpass_Filter\
        (ConcSignals, low_cutt_off=1, high_cutt_off=30, sampling_rate=176, order=2)
    # PrintMovements(Filtered_Signals)

    # Resampling Signals
    Resampled_Signals = Pre.Resampling(Filtered_Signals, 50)
    # PrintMovements(Resampled_Signals)

    # Removing Or Adding DC Component
    #DC_Train_Signals = Pre.DC_Component(Resampled_Signals, -1)
    # PrintMovements(DC_Train_Signals)

    # -------------------------------> Feature Extraction <---------------------------------------
    # Wavelets
    DWT_Train_Signals = FeatureExtraction.wavelet_features(Resampled_Signals, wavelet='db1', level=2)
    # PrintMovements(DWT_Train_Signals)
    # PSD
    #PSD_Train_Signals = FeatureExtraction.PSD_features(DC_Train_Signals, sampling_rate=176)
    # PrintMovements(PSD_Train_Signals)

    # Morphological
    Mor_Train_Signals = FeatureExtraction.morphology_features(Resampled_Signals)
    # PrintMovements(Mor_Train_Signals)

    Features = DWT_Train_Signals
    return Features

def getMovements(Signals):
    movementSignals = int(len(Signals)/4)
    signal = []
    for i in range(0,4):
        Movesig = []
        for index in range(i*4,(i*4)+ movementSignals-1):
            Movesig.append(Signals[index])
        signal.append(Movesig)
    return signal

def PrintMovements(signals):
    Signals=getMovements(signals)
    print(len(Signals))
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))
    axs[0][0].plot(np.arange(0, len(Signals[0])), Signals[0])
    axs[0][0].set_title("Down signal")
    plt.xlabel("Time T")
    plt.ylabel("Amplitude A")

    axs[0][1].plot(np.arange(0, len(Signals[1])), Signals[1])
    axs[0][1].set_title("Left Signals")
    plt.xlabel("Time T")
    plt.ylabel("Amplitude A")

    axs[1][0].plot(np.arange(0, len(Signals[2])), Signals[2])
    axs[1][0].set_title("Right Signals")
    plt.xlabel("Time T")
    plt.ylabel("Amplitude A")

    axs[1][1].plot(np.arange(0, len(Signals[3])), Signals[3])
    axs[1][1].set_title("Up Signals")
    plt.xlabel("Time T")
    plt.ylabel("Amplitude A")
    plt.legend()
    plt.show()


Features = Get_Prepared_Signals(-1)
Signal_Labels = Classification.GetLabels(Features)
# # Test = Get_Prepared_Signals(1)
# # test_label = Classification.GetLabels(Test)
# SVMTrain = Classification.Train_SVM_Classifier(Features, Signal_Labels,Test,test_label)
# RFTrain = Classification.Train_RF_Classifier(Features, Signal_Labels,Test,test_label)
# # LRTrain = Classification.Train_LR_Classifier(Features, Signal_Labels,Test,test_label)
# DTTrain = Classification.Train_DT_Classifier(Features, Signal_Labels,Test,test_label)

SVMTrain = Classification.Train_SVM_Classifier(Features, Signal_Labels)
RFTrain = Classification.Train_RF_Classifier(Features, Signal_Labels)
# LRTrain = Classification.Train_LR_Classifier(Features, Signal_Labels)
DTTrain = Classification.Train_DT_Classifier(Features, Signal_Labels)

if SVMTrain > DTTrain:
    print("SVM classifier is better with train accuracy : %.2f%%" % round(SVMTrain*100, 2))
elif SVMTrain == DTTrain:
    print("Both has the same accuracy : %.2f%%" % round(DTTrain*100, 2))
else:
    print("Decision Tree classifier is better with train accuracy: %.2f%%" % round(DTTrain*100, 2))

# print("test accuracy: ", y_pred)
# fig, axs = plt.subplots(2,2, figsize=(12, 8))
# axs[0][0].plot(np.arange(0, len(Amp)), Amp)
# axs[0][0].set_title("original signal")
# plt.xlabel("Time T")
# plt.ylabel("Amplitude A")

# plt.figure(figsize=(12,6))
# plt.plot(np.arange(0,len(Amp)),Amp, label='original signal')
# plt.plot(np.arange(0, len(filtered_signal)), filtered_signal, label='Filtered Signal')
# plt.legend()
# plt.show()