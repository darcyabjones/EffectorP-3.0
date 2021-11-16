try:
    from importlib.resources import path
except ImportError:
    from importlib_resources import path


def resource_filename(module, resource):
    """ Emulates the behaviour of the old setuptools resource_filename command.

    Basically it just gets rid of the context manager thing, because it's not needed.
    None of the files are zip files or create any temporary files that need to be
    cleaned up.

    This function would be unsafe to use with anything that will be extracted.
    """

    with path(module, resource) as handler:
        filename = str(handler)

    return filename


WEKA_PATH = resource_filename(__name__ + ".weka384", 'weka.jar')
FASTA_PATH = resource_filename(__name__, "Effectors.fasta")

models_bayes_cytoplasmic_fungionly = [
    resource_filename(__name__ + '.TrainingData_CytoplasmicFungiOnly_Mycorrhizal_Bayes', 'trainingdata_iteration85_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_CytoplasmicFungiOnly_Mycorrhizal_Bayes', 'trainingdata_iteration75_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_CytoplasmicFungiOnly_Mycorrhizal_Bayes', 'trainingdata_iteration100_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_CytoplasmicFungiOnly_Mycorrhizal_Bayes', 'trainingdata_iteration41_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_CytoplasmicFungiOnly_Mycorrhizal_Bayes', 'trainingdata_iteration31_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_CytoplasmicFungiOnly_Pathogens_Bayes', 'trainingdata_iteration92_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_CytoplasmicFungiOnly_Pathogens_Bayes', 'trainingdata_iteration16_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_CytoplasmicFungiOnly_Pathogens_Bayes', 'trainingdata_iteration84_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_CytoplasmicFungiOnly_Pathogens_Bayes', 'trainingdata_iteration2_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_CytoplasmicFungiOnly_Pathogens_Bayes', 'trainingdata_iteration96_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_CytoplasmicFungiOnly_Saprophytes_Bayes', 'trainingdata_iteration34_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_CytoplasmicFungiOnly_Saprophytes_Bayes', 'trainingdata_iteration64_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_CytoplasmicFungiOnly_Saprophytes_Bayes', 'trainingdata_iteration88_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_CytoplasmicFungiOnly_Saprophytes_Bayes', 'trainingdata_iteration23_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_CytoplasmicFungiOnly_Saprophytes_Bayes', 'trainingdata_iteration32_ratio3.model')
]

models_J48_cytoplasmic_fungionly = [
    resource_filename(__name__ + '.TrainingData_CytoplasmicFungiOnly_Mycorrhizal_J48', 'trainingdata_iteration77_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_CytoplasmicFungiOnly_Mycorrhizal_J48', 'trainingdata_iteration61_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_CytoplasmicFungiOnly_Mycorrhizal_J48', 'trainingdata_iteration95_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_CytoplasmicFungiOnly_Mycorrhizal_J48', 'trainingdata_iteration46_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_CytoplasmicFungiOnly_Mycorrhizal_J48', 'trainingdata_iteration56_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_CytoplasmicFungiOnly_Pathogens_J48', 'trainingdata_iteration85_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_CytoplasmicFungiOnly_Pathogens_J48', 'trainingdata_iteration58_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_CytoplasmicFungiOnly_Pathogens_J48', 'trainingdata_iteration87_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_CytoplasmicFungiOnly_Pathogens_J48', 'trainingdata_iteration25_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_CytoplasmicFungiOnly_Pathogens_J48', 'trainingdata_iteration97_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_CytoplasmicFungiOnly_Saprophytes_J48', 'trainingdata_iteration85_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_CytoplasmicFungiOnly_Saprophytes_J48', 'trainingdata_iteration13_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_CytoplasmicFungiOnly_Saprophytes_J48', 'trainingdata_iteration22_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_CytoplasmicFungiOnly_Saprophytes_J48', 'trainingdata_iteration91_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_CytoplasmicFungiOnly_Saprophytes_J48', 'trainingdata_iteration21_ratio3.model')
]

models_bayes_cytoplasmic = [
    resource_filename(__name__ + '.TrainingData_Cytoplasmic_Mycorrhizal_Bayes', 'trainingdata_iteration39_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Cytoplasmic_Mycorrhizal_Bayes', 'trainingdata_iteration17_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Cytoplasmic_Mycorrhizal_Bayes', 'trainingdata_iteration76_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Cytoplasmic_Mycorrhizal_Bayes', 'trainingdata_iteration74_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Cytoplasmic_Mycorrhizal_Bayes', 'trainingdata_iteration78_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Cytoplasmic_Pathogens_Bayes', 'trainingdata_iteration79_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Cytoplasmic_Pathogens_Bayes', 'trainingdata_iteration1_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Cytoplasmic_Pathogens_Bayes', 'trainingdata_iteration32_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Cytoplasmic_Pathogens_Bayes', 'trainingdata_iteration70_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Cytoplasmic_Pathogens_Bayes', 'trainingdata_iteration77_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Cytoplasmic_Saprophytes_Bayes', 'trainingdata_iteration14_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Cytoplasmic_Saprophytes_Bayes', 'trainingdata_iteration71_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Cytoplasmic_Saprophytes_Bayes', 'trainingdata_iteration44_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Cytoplasmic_Saprophytes_Bayes', 'trainingdata_iteration62_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Cytoplasmic_Saprophytes_Bayes', 'trainingdata_iteration64_ratio3.model')
]

models_J48_cytoplasmic = [
    resource_filename(__name__ + '.TrainingData_Cytoplasmic_Mycorrhizal_J48', 'trainingdata_iteration36_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Cytoplasmic_Mycorrhizal_J48', 'trainingdata_iteration14_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Cytoplasmic_Mycorrhizal_J48', 'trainingdata_iteration63_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Cytoplasmic_Mycorrhizal_J48', 'trainingdata_iteration60_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Cytoplasmic_Mycorrhizal_J48', 'trainingdata_iteration29_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Cytoplasmic_Pathogens_J48', 'trainingdata_iteration67_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Cytoplasmic_Pathogens_J48', 'trainingdata_iteration92_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Cytoplasmic_Pathogens_J48', 'trainingdata_iteration78_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Cytoplasmic_Pathogens_J48', 'trainingdata_iteration1_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Cytoplasmic_Pathogens_J48', 'trainingdata_iteration34_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Cytoplasmic_Saprophytes_J48', 'trainingdata_iteration36_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Cytoplasmic_Saprophytes_J48', 'trainingdata_iteration71_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Cytoplasmic_Saprophytes_J48', 'trainingdata_iteration67_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Cytoplasmic_Saprophytes_J48', 'trainingdata_iteration91_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Cytoplasmic_Saprophytes_J48', 'trainingdata_iteration70_ratio3.model')
]

models_bayes_apoplastic = [
    resource_filename(__name__ + '.TrainingData_Apoplastic_Animal_Bayes', 'trainingdata_iteration19_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Apoplastic_Animal_Bayes', 'trainingdata_iteration70_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Apoplastic_Animal_Bayes', 'trainingdata_iteration78_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Apoplastic_Animal_Bayes', 'trainingdata_iteration80_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Apoplastic_Animal_Bayes', 'trainingdata_iteration92_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Apoplastic_Pathogens_Bayes', 'trainingdata_iteration40_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Apoplastic_Pathogens_Bayes', 'trainingdata_iteration31_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Apoplastic_Pathogens_Bayes', 'trainingdata_iteration98_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Apoplastic_Pathogens_Bayes', 'trainingdata_iteration76_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Apoplastic_Pathogens_Bayes', 'trainingdata_iteration53_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Apoplastic_Saprophytes_Bayes', 'trainingdata_iteration61_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Apoplastic_Saprophytes_Bayes', 'trainingdata_iteration79_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Apoplastic_Saprophytes_Bayes', 'trainingdata_iteration29_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Apoplastic_Saprophytes_Bayes', 'trainingdata_iteration91_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Apoplastic_Saprophytes_Bayes', 'trainingdata_iteration32_ratio3.model')
]

models_J48_apoplastic = [
    resource_filename(__name__ + '.TrainingData_Apoplastic_Animal_J48', 'trainingdata_iteration82_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Apoplastic_Animal_J48', 'trainingdata_iteration19_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Apoplastic_Animal_J48', 'trainingdata_iteration46_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Apoplastic_Animal_J48', 'trainingdata_iteration47_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Apoplastic_Animal_J48', 'trainingdata_iteration100_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Apoplastic_Pathogens_J48', 'trainingdata_iteration26_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Apoplastic_Pathogens_J48', 'trainingdata_iteration98_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Apoplastic_Pathogens_J48', 'trainingdata_iteration49_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Apoplastic_Pathogens_J48', 'trainingdata_iteration9_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Apoplastic_Pathogens_J48', 'trainingdata_iteration78_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Apoplastic_Saprophytes_J48', 'trainingdata_iteration25_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Apoplastic_Saprophytes_J48', 'trainingdata_iteration95_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Apoplastic_Saprophytes_J48', 'trainingdata_iteration46_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Apoplastic_Saprophytes_J48', 'trainingdata_iteration92_ratio3.model'),
    resource_filename(__name__ + '.TrainingData_Apoplastic_Saprophytes_J48', 'trainingdata_iteration77_ratio3.model')
]
