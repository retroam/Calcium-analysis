function[I_t] = imagestostacks(image_fld,save_fld)

% IMAGESTOSTACKS(image_fld,save_fld) assembles tif images in image_fld as
% a single matrix which is then saved in save_fld as a .mat file
% NOTE: tif files in image_fld have to be labelled as image01...09,10 etc.

%Example:
% I = imagestostacks(image_fld,save_fld);

 cd(image_fld);
 i_bloc = dir('*.tif*');
 I_t = [];
   
 
  for j = 1:length(i_bloc)
     info = imfinfo(i_bloc(j).name);
     fileName{j} = i_bloc(j).name;
     num_images = numel(info);
     I_cum = zeros(info(1,1).Height,info(1,1).Width,num_images-1);%pre-alloc
    disp(['Loading tif file ' num2str(j) ' of ' num2str(length(i_bloc))]);
     for k = 1:num_images
         I = imread(i_bloc(j).name, k, 'Info', info);
         I_cum(:,:,k) = I;
     end
     close all force;
     I_t = cat(3,I_cum,I_t);
     clear I_cum;
  end

     save([save_fld '\I.mat'],'I_t');
     
 end

