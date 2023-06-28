#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from tractseg.experiments.peak_reg import Config as TractSegConfig
#change tract_seg to endings_seg or peak_reg

class Config(TractSegConfig):
    EXP_NAME = os.path.basename(__file__).split(".")[0]

    DATASET_FOLDER = "/nas/longleaf/home/zyc626/TractSeg/tractseg/tom"      # name of folder that contains all the preprocessed subjects (each subject has its own folder with the name of the subjectID)
    FEATURES_FILENAME = "mrtrix_peaks"  # filename of nifti file (*.nii.gz) without file ending; mrtrix CSD peaks; shape: [x,y,z,9]; one file for each subject
    LABELS_FILENAME = "bundle_masks"
