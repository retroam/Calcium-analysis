function[data,bkg] = roitodata(save_fld)
 
% ROITODATA(save_fld) loads CC from save_fld for data extraction from I.mat

%Example:
% [data,bkg] = roitodata(save_fld)

cd(save_fld);load('CC.mat');
m_bloc = dir('*I*.mat' );
data = [];background = [];avg=[];bkg=[];
for j = 1:length(m_bloc)
     I_cum = importdata(m_bloc(j).name);
   for k = 1:length(I_cum)%looping through files
      I =  I_cum(:,:,k);
      for l = 1:size(CC.PixelIdxList,2)
         avg(k,l) =  mean(I(CC.PixelIdxList{:,l})); 
         I(CC.PixelIdxList{:,l}) = NaN; 
      end
      bkg(k) = nanmean(I(:));
     
    end
  data = [data ; avg];
  background = [background bkg];
end
save('data.mat','data');save('bkg.mat','background');


