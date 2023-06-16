import numpy as np
import scipy
from os import chdir,listdir
import matplotlib.pylab as plt
import skimage


def stackstoroi(save_fld, sd):
    chdir(save_fld)
    m_bloc = listdir('*I*.mat*')
    i_cum = np.array([])
    img_content = np.array([])
    if len(m_bloc) == 11:
        for i in np.arange(1, 12.0):
            i_cum = np.concatenate((i_cum, np.load(m_bloc[int(i)-1])))
            
    else:
        I_cum = np.load(m_bloc[0].name)

    for j in np.arange(1., (len(I_cum))+1):
        I = I_cum[:,:,int(j)-1]
        img_content[int(j)-1] = np.mean(I.flatten(1))
    # [marks, locs] = findpeaks(img_content, 'minpeakdistance', 100.)
    # I_mean = np.mean(I_cum[:,:,int(locs)-1], 3.)
    # I_bw1 = threshold(I_mean, (mode(I_mean.flatten(1))+np.dot(sd, mad(I_mean.flatten(1), 1.))))
    # I_bw2 = bwareaopen(I_bw1, 20., 4.)
    # CC = bwconncomp(I_bw2)
    # I_edge = edge(I_bw2)
    # I_overlay = I_mean
    # I_overlay[int(I_edge)-1] = 10.*np.max(I_mean.flatten())/9.
    # np.save('CC.npy', CC)
    # return [CC, I_mean, I_bw2, I_overlay]
    return [CC, I_mean, I_bw2, I_overlay]
