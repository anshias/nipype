4. Read the tutorial on nipype interfaces and do the following:

For each subject, create a brain mask using FSL's BET through nipype interfaces.
Create images for each brain mask overlaid on the original anatomica image using nilearn's plotting tools (Hint: use plot_roi ) in this notebook

# ROI Plots

%pylab inline
from nilearn.plotting import plot_roi
from nipype.interfaces.fsl import BET
from nilearn import plotting

# Subject 50008
plotting.plot_roi('~/mprage_brain_mask.nii.gz', bg_img = '~/mprage.nii.gz',
                  title="Plot_Roi_Subject50008")
# Subject 50009
plotting.plot_roi('~/mprage2_brain_mask.nii.gz', bg_img = '~/mprage2.nii',
                  title="Plot_Roi_Subject50009")

# Subject 50010
plotting.plot_roi('~/mprage3_brain_mask.nii.gz', bg_img = '~/mprage3.nii',
                  title="Plot_Roi_Subject50010")

# Subject 50011
plotting.plot_roi('~/mprage4_brain_mask.nii.gz', bg_img = '~/mprage4.nii',
                  title="Plot_Roi_Subject50011")

# Subject 50012
plotting.plot_roi('~/mprage5_brain_mask.nii.gz', bg_img = '~/mprage5.nii',
                  title="Plot_Roi_Subject50012")




