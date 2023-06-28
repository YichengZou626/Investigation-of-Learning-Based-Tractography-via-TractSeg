import os

file_list = os.listdir('/Users/zyc626/Desktop/BCP')
files = []
for f in file_list:
    if f != '.DS_Store':
        files.append(f)
        
#os.chdir('/Users/zyc626/Desktop/data/cnm')
bundles = ['AcousticRadiatio_Right', 'AnteriorCommissure', 'AnteriorThalamicRadiation_Left', 'AnteriorThalamicRadiation_Right', 'ArcuateFasciculus_Left', 'ArcuateFasciculus_Right', 'Cerebellum_Left', 'Cerebellum_Right', 'CingulumBundleHippocampal_Right', 'CingulumBundle_Left', 'CingulumBundle_Right', 'CochlearNucleiFacialNerves_Left', 'CochlearNucleiOculomotorNerves_Right', 'CochlearNucleiSpinalTrigeminalTract_Left', 'CochlearNucleiSpinalTrigeminalTract_Right', 'CochlearNucleiVagusNerves_Left', 'CochlearNucleiVagusNerves_Right', 'CoronaRadiataFrontal_Left', 'CoronaRadiataFrontal_Right', 'CoronaRadiataParietal_Left', 'CorpusCallosum', 'CorpusCallosumAnteriorMidbody', 'CorpusCallosumGenu', 'CorpusCallosumIsthmus', 'CorpusCallosumPosteriorMidbody', 'CorpusCallosumRostralBody', 'CorpusCallosumRostrum', 'CorpusCallosumSplenium', 'CorticoFugalParietal_Left', 'CorticoFugalPreFrontal_Left', 'CorticoPontineTract_Left', 'CorticoPontineTract_Right', 'CorticoPontoCerebellar', 'CorticoSpinalTract_Left', 'CorticoSpinalTract_Right', 'CorticoStriatalPathway_Left', 'CorticoStriatalPathway_Right', 'CorticoThalamicPathwayMotor_Left', 'CorticoThalamicPathwaySuperior_Left', 'CorticoThalamicPathway_Left', 'CorticoThalamicPathway_Right', 'DentatoRubroThalamic_Left', 'DentatoRubroThalamic_Right', 'DorsoLateralPrefrontalCortex_Left', 'DorsoLateralPrefrontalCortex_Right', 'DorsoMedialPrefrontalCortex_Left', 'DorsoMedialPrefrontalCortex_Right', 'ExternalCapsule_Left', 'ExternalCapsule_Right', 'ExtremeCapsule_Left', 'ExtremeCapsule_Right', 'Fornix_Left', 'Fornix_Right', 'FrontalAslantTract_Left', 'FrontalAslantTract_Right', 'FrontoPontineTract_Left', 'FrontoPontineTract_Right', 'InferiorCerebellarPeduncle_Left', 'InferiorCerebellarPeduncle_Right', 'InferiorLongitudinalFasciculus_Left', 'InferiorLongitudinalFasciculus_Right', 'InferiorOccipitoFrontalFasciculus_Left', 'InferiorOccipitoFrontalFasciculus_Right', 'IntraCerebellarInputAndPurkinjeTract_Left', 'IntraCerebellarInputAndPurkinjeTract_Right', 'IntraCerebellarParallelTract_Left', 'IntraCerebellarParallelTract_Right', 'MedialLongitudinalFasciculus_Left', 'MedialLongitudinalFasciculus_Right', 'MiddleCerebellarPeduncle', 'MiddleLongitudinalFasciculus_Left', 'MiddleLongitudinalFasciculus_Right', 'OpticRadiation_Left', 'OpticTract_Left', 'OpticTract_Right', 'OrbitoFrontalCortex_Left', 'OrbitoFrontalCortex_Right', 'OrbitofrontalOrbitofrontal_Left', 'OrbitofrontalOrbitofrontal_Right', 'ParietalAslantTract_Left', 'ParietoOccipitalPontineTract_Left', 'ParietoOccipitalPontineTract_Right', 'PosteriorLimbOfInternalCapsule_Left', 'RubroSpinalTract_Right', 'SpinoThalamicTract_Left', 'StriatoFrontal_Left', 'StriatoFrontal_Right', 'StriatoFrontoOrbital_Left', 'StriatoFrontoOrbital_Right', 'StriatoOccipital_Left', 'StriatoOccipital_Right', 'StriatoParietal_Left', 'StriatoParietal_Right', 'StriatoPostcentral_Left', 'StriatoPostcentral_Right', 'StriatoPrecentral_Left', 'StriatoPrecentral_Right', 'StriatoPrefrontal_Left', 'StriatoPrefrontal_Right', 'StriatoPremotor_Left', 'StriatoPremotor_Right', 'SuperficialFrontalParietal_Left', 'SuperficialFrontalParietal_Right', 'SuperficialFrontal_Left', 'SuperficialFrontal_Right', 'SuperficialOccipitalTemporal_Left', 'SuperficialOccipitalTemporal_Right', 'SuperficialOccipital_Left', 'SuperficialOccipital_Right', 'SuperficialParietalOccipital_Left', 'SuperficialParietalOccipital_Right', 'SuperficialParietalTemporal_Left', 'SuperficialParietalTemporal_Right', 'SuperficialParietal_Left', 'SuperficialParietal_Right', 'SuperficialTemporal_Left', 'SuperficialTemporal_Right', 'SuperiorCerebellarPeduncl_Left', 'SuperiorCerebellarPeduncl_Right', 'SuperiorLongitudinalFasciculu1_Left', 'SuperiorLongitudinalFasciculu1_Right', 'SuperiorLongitudinalFasciculu2_Left', 'SuperiorLongitudinalFasciculu2_Right', 'SuperiorLongitudinalFasciculu3_Left', 'SuperiorLongitudinalFasciculu3_Right', 'SuperiorThalamicRadiation_Right', 'ThalamoFrontal_Left', 'ThalamoFrontal_Right', 'ThalamoOccipital_Left', 'ThalamoOccipital_Right', 'ThalamoParietal_Left', 'ThalamoParietal_Right', 'ThalamoPostcentral_Right', 'ThalamoPrecentral_Left', 'ThalamoPrefrontal_Left', 'ThalamoPrefrontal_Right', 'UFibers_Left', 'UFibers_Right', 'UncinateFasciculus_Left', 'UncinateFasciculus_Right', 'Vermis', 'VerticalOccipitalFasciculu_Left', 'VerticalOccipitalFasciculu_Right']

for file in files:
    dir = '/Users/zyc626/Desktop/BCP/'+file
    os.chdir(dir)
    os.mkdir('tdi')
    os.mkdir('masks')
    os.system('fslroi dwi.nii.gz b0.nii.gz 0 1 ')
    func = 'fslmerge -tr bundle_masks.nii.gz '
    
    for b in bundles:
        CMD = 'tckmap bundles/' + b + '/' + b + '.tck -contrast tdi tdi/' + b + '.nii.gz -template b0.nii.gz'
        os.system(CMD)

        CMD = 'fslmaths tdi/' + b +'.nii.gz -bin masks/' + b + '.nii.gz'
        os.system(CMD)

        mask = 'masks/'+ b +'.nii.gz '
        func += mask

    func += '1'
    os.system(func)
    os.chdir('/Users/zyc626/Desktop/BCP')
    
