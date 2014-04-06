
import numpy as np
import scipy
import matcompat
from os import chdir,listdir

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def stackstoroi(save_fld, sd):

    # Local Variables: I_bw2, I_cum, I_bw1, I, I_overlay, locs, CC, i,
    # j, img_content, I_edge, m_bloc, I_mean, marks, save_fld, sd
    # Function calls: save, stackstoroi, mad, findpeaks, cat, bwareaopen,
    #  length, edge, bwconncomp, importdata, max, threshold, mode, cd, dir, mean
    #% STACKSTOROI(image_fld,sd) loads *I*.mat from save_fld for image
    #% segmentation. sd is how many standard deviations above the mean the 
    #% threshold is set for segmentation.  Outputs:
    #% CC: connected components found in I_bw2
    #% I_mean: averaged image of *I*.mat
    #% I_bw2: binary image containing image segementation of *I*.mat
    #% I_overlay: overlay of identified ROI over I_mean
    #%Example:
    #% [CC,I_mean,I_bw2,I_overlay] = stackstoroi(save_fld,sd);
    chdir(save_fld)
    m_bloc = listdir('*I*.mat*')
    i_cum = np.array([])
    img_content = np.array([])
    if length(m_bloc) == 11:
        for i in np.arange(1, 12.0):
            i_cum = cat(3, i_cum, importdata((m_bloc[int(i)-1].name)))
            
    else:
        I_cum = importdata((m_bloc[0].name))
        
    
    for j in np.arange(1., (length(I_cum))+1):
        I = I_cum[:,:,int(j)-1]
        img_content[int(j)-1] = np.mean(I.flatten(1))
        
    [marks, locs] = findpeaks(img_content, 'minpeakdistance', 100.)
    I_mean = np.mean(I_cum[:,:,int(locs)-1], 3.)
    #%I_bw1 = bwspecial(otsu(I_mean,3));
    I_bw1 = threshold(I_mean, (mode(I_mean.flatten(1))+np.dot(sd, mad(I_mean.flatten(1), 1.))))
    I_bw2 = bwareaopen(I_bw1, 20., 4.)
    CC = bwconncomp(I_bw2)
    I_edge = edge(I_bw2)
    I_overlay = I_mean
    I_overlay[int(I_edge)-1] = 10.*matcompat.max(I_mean.flatten(1))/9.
    plt.save('CC.mat', 'CC')
    return [CC, I_mean, I_bw2, I_overlay]