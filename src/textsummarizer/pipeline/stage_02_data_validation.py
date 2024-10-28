from textsummarizer.config.configuration import ConfigurationManager
from textsummarizer.components.data_validation import DataValidation
from textsummarizer.logging import logger


class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()  # Corrected method name
        data_validation = DataValidation(config=data_validation_config)  # Corrected variable name
        data_validation.validate_all_files_exist()