import pytest
import os
from config import Config


class TestConfigSimple:
    """Simple unit tests for configuration."""
    
    def test_config_creation(self):
        """Test that Config can be created."""
        config = Config()
        assert config is not None
    
    def test_secret_key_exists(self):
        """Test that SECRET_KEY exists."""
        config = Config()
        assert hasattr(config, 'SECRET_KEY')
        assert config.SECRET_KEY is not None
        assert len(config.SECRET_KEY) > 0
    
    def test_upload_folder_exists(self):
        """Test that UPLOAD_FOLDER exists."""
        config = Config()
        assert hasattr(config, 'UPLOAD_FOLDER')
        assert config.UPLOAD_FOLDER is not None
        assert os.path.isabs(config.UPLOAD_FOLDER)
    
    def test_max_content_length_exists(self):
        """Test that MAX_CONTENT_LENGTH exists."""
        config = Config()
        assert hasattr(config, 'MAX_CONTENT_LENGTH')
        assert config.MAX_CONTENT_LENGTH is not None
        assert config.MAX_CONTENT_LENGTH > 0
    
    def test_max_content_length_value(self):
        """Test that MAX_CONTENT_LENGTH is 1MB."""
        config = Config()
        expected_size = 1 * 1024 * 1024  # 1MB
        assert config.MAX_CONTENT_LENGTH == expected_size
    
    def test_config_attributes(self):
        """Test that all expected attributes exist."""
        config = Config()
        expected_attributes = ['SECRET_KEY', 'UPLOAD_FOLDER', 'MAX_CONTENT_LENGTH']
        
        for attr in expected_attributes:
            assert hasattr(config, attr)
    
    def test_multiple_config_instances(self):
        """Test that multiple config instances work."""
        config1 = Config()
        config2 = Config()
        
        # Both should have the same values
        assert config1.SECRET_KEY == config2.SECRET_KEY
        assert config1.UPLOAD_FOLDER == config2.UPLOAD_FOLDER
        assert config1.MAX_CONTENT_LENGTH == config2.MAX_CONTENT_LENGTH
    
    def test_upload_folder_path_structure(self):
        """Test that upload folder path has expected structure."""
        config = Config()
        path = config.UPLOAD_FOLDER
        
        # Should contain 'app', 'data', 'uploads'
        assert 'app' in path
        assert 'data' in path
        assert 'uploads' in path 