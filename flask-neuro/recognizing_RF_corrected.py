#!/usr/bin/env python
# coding: utf-8

# In[1]:


from os import listdir
from os.path import isfile, join
import mne
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from biosppy.signals import ecg
import pandas as pd
import pyedflib
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from art.estimators.classification.scikitlearn import ScikitlearnRandomForestClassifier


# In[2]:


mypath=r'static'
file_list = [f for f in listdir(mypath) if isfile(join(mypath, f))]


# In[3]:


def extract_feature_1(file_name):
    f = pyedflib.EdfReader(file_name)
    n = f.signals_in_file
    signal_labels = f.getSignalLabels()
    sigbufs = np.zeros((n, f.getNSamples()[0]))
    for i in np.arange(n):
        sigbufs[i, :] = f.readSignal(i)
    fs=f.getSampleFrequencies()[0]
    templates_list=[]
    
    for i in range(2, 8):
        signal = sigbufs[i]
        out = ecg.ecg(signal=signal, sampling_rate=fs, show=False)
        templates_list.append(out['templates'])
    templates_table=np.vstack((templates_list))
    return templates_table


# In[4]:


def extract_feature_2(file_name):
    f = pyedflib.EdfReader(file_name)
    n = f.signals_in_file
    signal_labels = f.getSignalLabels()
    sigbufs = np.zeros((n, f.getNSamples()[0]))
    for i in np.arange(n):
        sigbufs[i, :] = f.readSignal(i)
    fs=f.getSampleFrequencies()[0]
    templates_list=[]
    
    for i in range(2, 8):
        signal = sigbufs[i]
        out = ecg.ecg(signal=signal, sampling_rate=fs, show=False)
        templates_list.append(out['templates'])
    templates_table=np.vstack((templates_list))
    return templates_table


# In[5]:


def extract_feature_3(file_name):
    f = pyedflib.EdfReader(file_name)
    n = f.signals_in_file
    signal_labels = f.getSignalLabels()
    sigbufs = np.zeros((n, f.getNSamples()[0]))
    for i in np.arange(n):
        sigbufs[i, :] = f.readSignal(i)
    fs=f.getSampleFrequencies()[0]
    templates_list=[]
    
    for i in range(2, 4):
        signal = sigbufs[i]
        out = ecg.ecg(signal=signal, sampling_rate=fs, show=False)
        templates_list.append(out['templates'])
    templates_table=np.vstack((templates_list))
    return templates_table


# In[6]:


def extract_feature_4(file_name):
    f = pyedflib.EdfReader(file_name)
    n = f.signals_in_file
    signal_labels = f.getSignalLabels()
    sigbufs = np.zeros((n, f.getNSamples()[0]))
    for i in np.arange(n):
        sigbufs[i, :] = f.readSignal(i)
    fs=f.getSampleFrequencies()[0]
    templates_list=[]
    
    for i in range(6, 8):
        signal = sigbufs[i]
        out = ecg.ecg(signal=signal, sampling_rate=fs, show=False)
        templates_list.append(out['templates'])
    templates_table=np.vstack((templates_list))
    return templates_table


# In[7]:


def extract_feature_5(file_name):
    f = pyedflib.EdfReader(file_name)
    n = f.signals_in_file
    signal_labels = f.getSignalLabels()
    sigbufs = np.zeros((n, f.getNSamples()[0]))
    for i in np.arange(n):
        sigbufs[i, :] = f.readSignal(i)
    fs=f.getSampleFrequencies()[0]
    templates_list=[]
    
    for i in range(5, 8):
        signal = sigbufs[i]
        out = ecg.ecg(signal=signal, sampling_rate=fs, show=False)
        templates_list.append(out['templates'])
    templates_table=np.vstack((templates_list))
    return templates_table


# In[8]:


def extract_feature_6(file_name):
    f = pyedflib.EdfReader(file_name)
    n = f.signals_in_file
    signal_labels = f.getSignalLabels()
    sigbufs = np.zeros((n, f.getNSamples()[0]))
    for i in np.arange(n):
        sigbufs[i, :] = f.readSignal(i)
    fs=f.getSampleFrequencies()[0]
    templates_list=[]
    
    for i in range(6, 8):
        signal = sigbufs[i]
        out = ecg.ecg(signal=signal, sampling_rate=fs, show=False)
        templates_list.append(out['templates'])
    templates_table=np.vstack((templates_list))
    return templates_table


# In[9]:


def extract_feature_7(file_name):
    f = pyedflib.EdfReader(file_name)
    n = f.signals_in_file
    signal_labels = f.getSignalLabels()
    sigbufs = np.zeros((n, f.getNSamples()[0]))
    for i in np.arange(n):
        sigbufs[i, :] = f.readSignal(i)
    fs=f.getSampleFrequencies()[0]
    templates_list=[]
    
    for i in range(3, 8):
        signal = sigbufs[i]
        out = ecg.ecg(signal=signal, sampling_rate=fs, show=False)
        templates_list.append(out['templates'])
    templates_table=np.vstack((templates_list))
    return templates_table


# In[10]:


def extract_feature_8(file_name):
    f = pyedflib.EdfReader(file_name)
    n = f.signals_in_file
    signal_labels = f.getSignalLabels()
    sigbufs = np.zeros((n, f.getNSamples()[0]))
    for i in np.arange(n):
        sigbufs[i, :] = f.readSignal(i)
    fs=f.getSampleFrequencies()[0]
    templates_list=[]
    
    for i in range(0, 2):
        signal = sigbufs[i]
        out = ecg.ecg(signal=signal, sampling_rate=fs, show=False)
        templates_list.append(out['templates'])
    templates_table=np.vstack((templates_list))
    return templates_table


# In[11]:


def extract_feature_9(file_name):
    f = pyedflib.EdfReader(file_name)
    n = f.signals_in_file
    signal_labels = f.getSignalLabels()
    sigbufs = np.zeros((n, f.getNSamples()[0]))
    for i in np.arange(n):
        sigbufs[i, :] = f.readSignal(i)
    fs=f.getSampleFrequencies()[0]
    templates_list=[]
    
    for i in range(0, 2):
        signal = sigbufs[i]
        out = ecg.ecg(signal=signal, sampling_rate=fs, show=False)
        templates_list.append(out['templates'])
    templates_table=np.vstack((templates_list))
    return templates_table


# In[12]:


# load, no need to initialize the loaded_rf
loaded_rf_1 = joblib.load(r"RF/RF_1.joblib")
# load, no need to initialize the loaded_rf
loaded_rf_2 = joblib.load(r"RF/RF_2.joblib")
# load, no need to initialize the loaded_rf
loaded_rf_3 = joblib.load(r"RF/RF_3.joblib")
# load, no need to initialize the loaded_rf
loaded_rf_4 = joblib.load(r"RF/RF_4.joblib")
# load, no need to initialize the loaded_rf
loaded_rf_5 = joblib.load(r"RF/RF_5.joblib")
# load, no need to initialize the loaded_rf
loaded_rf_6 = joblib.load(r"RF/RF_6.joblib")
# load, no need to initialize the loaded_rf
loaded_rf_7 = joblib.load(r"RF/RF_7.joblib")
# load, no need to initialize the loaded_rf
loaded_rf_8 = joblib.load(r"RF/RF_8.joblib")
# load, no need to initialize the loaded_rf
loaded_rf_9 = joblib.load(r"RF/RF_9.joblib")


# In[13]:


class_1=[]
class_2=[]
class_3=[]
class_4=[]
class_5=[]
class_6=[]
class_7=[]
class_8=[]
class_9=[]
for i in range(len(file_list)):
    file_name=mypath + '/'+ file_list[i]
    
    feature_vector_1=extract_feature_1(file_name)
    a1=loaded_rf_1.predict(feature_vector_1)
    avg1=sum(a1)/a1.shape[0]
    av1=1 - avg1
    class_1.append("%0.2f" % av1)
    
    feature_vector_2=extract_feature_2(file_name)
    a2=loaded_rf_2.predict(feature_vector_2)
    avg2=sum(a2)/a2.shape[0]
    av2=1 - avg2
    class_2.append("%0.2f" % av2)
    
    feature_vector_3=extract_feature_3(file_name)
    a3=loaded_rf_3.predict(feature_vector_3)
    avg3=sum(a3)/a3.shape[0]
    av3=1 -  avg3
    class_3.append("%0.2f" % av3)
    
    feature_vector_4=extract_feature_4(file_name)
    a4=loaded_rf_4.predict(feature_vector_4)
    avg4=sum(a4)/a4.shape[0]
    av4=1 - avg4
    class_4.append("%0.2f" % av4)
    
    feature_vector_5=extract_feature_5(file_name)
    a5=loaded_rf_5.predict(feature_vector_5)
    avg5=sum(a5)/a5.shape[0]
    av5=1 -  avg5
    class_5.append("%0.2f" % av5)
    
    feature_vector_6=extract_feature_6(file_name)
    a6=loaded_rf_6.predict(feature_vector_6)
    avg6=sum(a6)/a6.shape[0]
    av6=1 -  avg6
    class_6.append("%0.2f" % av6)   
    
    feature_vector_7=extract_feature_7(file_name)
    a7=loaded_rf_7.predict(feature_vector_7)
    avg7=sum(a7)/a7.shape[0]
    av7=1 -  avg7
    class_7.append("%0.2f" % av7) 
    
    feature_vector_8=extract_feature_8(file_name)
    a8=loaded_rf_8.predict(feature_vector_8)
    avg8=sum(a8)/a8.shape[0]
    av8=1 -  avg8
    class_8.append("%0.2f" % av8) 
    
    feature_vector_9=extract_feature_9(file_name)
    a9=loaded_rf_9.predict(feature_vector_9)
    avg9=sum(a9)/a9.shape[0]
    av9=1 -  avg9
    class_9.append("%0.2f" % av9) 


# In[14]:


column_list=[file_list, class_1, class_2, class_3, class_4, class_5, class_6, class_7, class_8, class_9]


# In[15]:


df = pd.DataFrame(np.column_stack(column_list), columns=['File list', 'Class 1', 'Class 2', 'Class 3', 'Class 4', 'Class 5', 'Class 6', 'Class 7', 'Class 8', 'Class 9'])


# In[16]:


df


# In[17]:


df.to_csv('RF.csv')


# In[ ]:




