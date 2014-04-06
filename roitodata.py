
import numpy as np
import scipy
import matcompat

# if available import pylab (from matlibplot)
try:
    import matplotlib.pylab as plt
except ImportError:
    pass

def roitodata(save_fld):

    # Local Variables: I_cum, bkg, save_fld, k, j, l, m_bloc, I, background, avg, data
    # Function calls: load, save, nanmean, CC, NaN, cd, length, importdata, roitodata, mean, dir, size
    #% ROITODATA(save_fld) loads CC from save_fld for data extraction from I.mat
    #%Example:
    #% [data,bkg] = roitodata(save_fld)
    os.chdir(save_fld)
    np.load('CC.mat')
    m_bloc = dir('*I*.mat')
    data = np.array([])
    background = np.array([])
    avg = np.array([])
    bkg = np.array([])
    for j in np.arange(1., (length(m_bloc))+1):
        I_cum = importdata((m_bloc[int(j)-1].name))
        for k in np.arange(1., (length(I_cum))+1):
            #%looping through files
            
        data = np.array(np.hstack((data)))
        background = np.array(np.hstack((background, bkg)))
        
    plt.save('data.mat', 'data')
    plt.save('bkg.mat', 'background')
    return [data, bkg]