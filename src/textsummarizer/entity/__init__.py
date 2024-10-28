from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=False)
class DataIngestionConfig:
    def __init__(self, root_dir, source_URL, local_data_file, unzip_dir):
        self.root_dir = root_dir
        self.source_URL = source_URL
        self.local_data_file = local_data_file
        self.unzip_dir = unzip_dir
        
        
        
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=False)
class DataValidationConfig:
    def __init__(self, root_dir, STATUS_FILE, ALL_REQUIRED_FILES):
        self.root_dir = root_dir
        self.STATUS_FILE = STATUS_FILE
        self.ALL_REQUIRED_FILES = ALL_REQUIRED_FILES        
        