import csv
import os
import numpy as np
from scipy import signal


def csvCleaner(dirName, fileName):
    newFileDir = '.\\csv\\csvCleanData\\' + dirName + '\\' + fileName + 'Data'
    csvFilePath = '.\\csv\\csvRecords\\' + dirName + '\\' + fileName + '.csv'
    nbrOfRow = 0
    if not os.path.exists(newFileDir):
        os.makedirs(newFileDir)

        #get information of the file such as date, subject, etc and create other csv files
        with open(csvFilePath, 'r') as csvfile:
            spamreader = csv.reader(csvfile, delimiter = ',')

            for row in spamreader:
                with open(newDir + '/info.txt', 'w+') as info:
                    info.write('\r'.join(row))

                channel = row[5]
                begin = channel.find('AF3')
                end = channel.find('AF4')
                channel = channel[begin: end+3]
                channelList = channel.split(' ')

                for chan in channelList:
                    with open(newDir + '/channelList.txt', 'a+') as channelFileList:
                        channelFileList.write(chan+'\n')
                    channelFile = open(newDir + '/' + chan + '.csv', 'w+')
                    channelFile.close()

                break

            #get information from channels and put it in a different csv file for each channel
            for row in spamreader:
                if nbrOfRow > 5120:
                    for i in range(0, len(channelList)):
                        chan = open(newDir + '/' + channelList[i] + '.csv', 'a')
                        chan.write(str(int(row[i+2].split('.')[0]))+'\n')
                        chan.close()
                nbrOfRow += 1

def csvToPeriodogram(dirName, fileName):
    filePath = '.\\csv\\csvCleanData\\' + dirName + '\\' + fileName + 'Data\\'
    channelList = ['AF3', 'F7', 'F3', 'F4', 'F8', 'AF4']
    strData = ''
    fs = 128

    if os.path.exists(filePath):
        for i in range(0, len(channelList)):
            with open(filePath + channelList[i] + '.csv') as csvfile:
                spamreader = csv.reader(csvfile, delimiter='\r')
                dataSource = []

                for row in spamreader:
                    dataSource.append(int(row[0]))
                dataSource = np.array(dataSource)

                sampleFrequency, powerSpectralArray = signal.periodogram(dataSource, fs, nfft=8)

                for l in range(1, len(powerSpectralArray)):
                    strData += str(powerSpectralArray[l]) + ', '

        strData += dirName + '\n'
        return strData


