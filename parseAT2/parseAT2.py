'''
Python script to read the recorded timehistory from NGA database

input : path to the timehistory file
output : the acceleration time history with dt
'''
import os

def parse(fname):
    if not os.path.exists(fname):
        return {'Acc' : -1, 'dt':-1 , 'NPTS':-1, 'error':-1}
    accFile = open(fname)
    # Burn through the first 3 lines
    for i in range(3):
        burn = accFile.next()

    infoLine = accFile.next()
    data = infoLine.split(',')
    NPTS = int(data[0].split('=')[1].strip())
    dt = float(data[1].split('=')[1].strip().split(' ')[0].strip())
    acc = []
    for line in accFile:
        data = line.split(' ')
        data = [float(d.strip()) for d in data if len(d) > 0]
        acc += data

    assert len(acc) == NPTS

    return {'Acc':acc , 'dt': dt, 'NPTS':NPTS, 'error':0}
