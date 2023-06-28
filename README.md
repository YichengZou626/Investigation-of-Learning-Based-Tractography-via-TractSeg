# Investigation-of-Learning-Based-Tractography-via-TractSeg

The reconstruction of white matter fiber bundles using non-invasive diffusion-weighted magnetic resonance imaging is useful for studying brain connectivity. However, accurate fiber reconstruction remains a challenging problem. Here, we explore the use of the TractSeg model to tackle fiber reconstruction as a machine-learning problem. We use microstructure-informed fiber filtering techniques, such as COMMIT, to build our own dataset for training the model. We find that the use of a high-quality tractogram during training improves fiber reconstruction. Although our strategy yields fewer streamlines, it retains major connectivity information. Our findings support the importance of using quality controlled data for model training to improve the outcome of learning-based tractography methods such as TractSeg.

<img width="1626" alt="Screen Shot 2023-06-28 at 11 29 41 AM" src="https://github.com/YichengZou626/Investigation-of-Learning-Based-Tractography-via-TractSeg/assets/59714064/83d15361-bc7b-40de-8716-7d1dc7b254c9">

First, it takes T1-weighted MRI images as input and uses MRtrix to generate an initial tractogram. Second, it reduces the number of streamlines using the SIFT and COMMIT algorithms. It also parameterizes each streamline using a subset of the initial points to estimate its trajectory. Third, by the force of QuickBundles, nearby streamlines are clustered together based on their spatial information to represent longer tracts. Finally, the resulting clustering-based tracts are used as input for training TractSeg model, and the output will be comparatively analyzed with previous work.

TractSeg is the code for the following paper. Please cite the papers if you use it.
* Tract Segmentation:   
[TractSeg - Fast and accurate white matter tract segmentation](https://doi.org/10.1016/j.neuroimage.2018.07.070) ([free arxiv version](https://arxiv.org/abs/1805.07103))
[NeuroImage 2018]
* Tract Orientation Mapping (TOM):   
[Tract orientation mapping for bundle-specific tractography](https://arxiv.org/abs/1806.05580)
[MICCAI 2018]
* Tracking on TOMs:  
[Combined tract segmentation and orientation mapping for bundle-specific tractography](https://www.sciencedirect.com/science/article/pii/S136184151930101X)
[Medical Image Analysis 2019]
* Tractometry:  
[Multiparametric mapping of white matter microstructure in catatonia](https://www.nature.com/articles/s41386-020-0691-2) ([free preprint](resources/Wasserthal2020_Multiparametric_mapping_of_white_matter.pdf))
[Nature Neuropsychopharmacology 2020]
* Our paper://
https://docs.google.com/document/d/1C-hySU6B40irJ9qYQEmq3ZsKKJGbyQrL8rBAhQPRZSM/edit?usp=sharing
