
function[CC,I_mean,I_bw2,I_overlay] = stackstoroi(save_fld,sd)

% STACKSTOROI(image_fld,sd) loads *I*.mat from save_fld for image
% segmentation. sd is how many standard deviations above the mean the 
% threshold is set for segmentation.  Outputs:
% CC: connected components found in I_bw2
% I_mean: averaged image of *I*.mat
% I_bw2: binary image containing image segementation of *I*.mat
% I_overlay: overlay of identified ROI over I_mean

%Example:
% [CC,I_mean,I_bw2,I_overlay] = stackstoroi(save_fld,sd);

cd(save_fld);
m_bloc = dir('*I*.mat*');
I_cum  = [];
img_content = [];
if length(m_bloc)== 11
    for i = 1:11
        I_cum = cat(3,I_cum,importdata(m_bloc(i).name));
    end
    
else
   I_cum = importdata(m_bloc(1).name);
end
    
  for j = 1:length(I_cum)
      I = I_cum(:,:,j);
      img_content(j) = mean(I(:));
  end
  [marks,locs] = findpeaks(img_content,'minpeakdistance',100);
    I_mean = mean(I_cum(:,:,locs),3);
   
   %I_bw1 = bwspecial(otsu(I_mean,3));
   I_bw1 = threshold(I_mean,mode(I_mean(:))+ sd*mad(I_mean(:),1));
   I_bw2 = bwareaopen(I_bw1,20,4);   
   CC = bwconncomp(I_bw2);
   I_edge = edge(I_bw2);
   I_overlay = I_mean;
   I_overlay(I_edge) = 10*max(I_mean(:))/9;
   save('CC.mat','CC');

