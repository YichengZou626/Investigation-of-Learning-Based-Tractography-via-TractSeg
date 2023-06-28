
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from os.path import join

from tractseg.libs.system_config import SystemConfig as C


# HCP_105
# (bad subjects removed: 994273, 937160, 885975, 788876, 713239)
# (no CA: 885975, 788876, 713239)
all_subjects = ["100610", "102311", "102816", "104416", "105923", "108323","109123", "111514", "111312","115017","115825","116726","118225","125525","126426","128935","130518","132188","134627","135124","137128","144226","145834","146432","146735","146937","148133","155938","156334","158136"]

def get_all_subjects(dataset="HCP"):
    return all_subjects
