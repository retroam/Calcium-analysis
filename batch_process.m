%m-file for batch processing of calcium data
tic
% close all; clear all;clc;

image_fld = 'C:\Users\rka2p\Desktop\Calcium analysis\file_folder';
save_fld = 'C:\Users\rka2p\Desktop\Calcium analysis\save_folder';
imagestostacks(image_fld,save_fld);
sd = 7;%sd from  mean of image intensity to set as threshold
[CC,I_mean,I_bw2,I_overlay] = stackstoroi(save_fld,sd);
imagesc(I_overlay); axis off;
[data,bkg] = roitodata(save_fld);
figure; plot(data);
toc