import pytest
from datetime import datetime
from app.dto import Student


class TestStudent:
    """Test cases for the Student DTO class."""
    
    @pytest.mark.unit
    def test_student_creation(self):
        """Test creating a Student object with valid data."""
        name = "John Doe"
        seat_number = "A1"
        topic = "Code bug/error"
        time_of_request = "2024-01-01 10:00:00"
        
        student = Student(name, seat_number, topic, time_of_request)
        
        assert student.name == name
        assert student.seat_number == seat_number
        assert student.topic == topic
        assert student.time_of_request == time_of_request
    
    def test_student_creation_with_different_data_types(self):
        """Test creating Student objects with different data types."""
        # Test with integer seat number (should work as it's converted to string)
        student1 = Student("Alice", 1, "HTML/CSS/Bootstrap issue", "2024-01-01 10:00:00")
        assert student1.seat_number == 1
        
        # Test with different topics
        student2 = Student("Bob", "B2", "Understanding the lab exercises", "2024-01-01 10:00:00")
        assert student2.topic == "Understanding the lab exercises"
        
        # Test with "Other" topic
        student3 = Student("Charlie", "C3", "Other", "2024-01-01 10:00:00")
        assert student3.topic == "Other"
    
    def test_student_string_representation(self):
        """Test the string representation of Student objects."""
        student = Student("John Doe", "A1", "Code bug/error", "2024-01-01 10:00:00")
        expected_str = "Student(name=John Doe, seat_number=A1, topic=Code bug/error, time_of_request = 2024-01-01 10:00:00)"
        
        assert str(student) == expected_str
    
    def test_student_with_empty_strings(self):
        """Test Student creation with empty strings (edge case)."""
        student = Student("", "", "", "")
        
        assert student.name == ""
        assert student.seat_number == ""
        assert student.topic == ""
        assert student.time_of_request == ""
    
    def test_student_with_special_characters(self):
        """Test Student creation with special characters in name."""
        student = Student("José María", "A1", "Code bug/error", "2024-01-01 10:00:00")
        
        assert student.name == "José María"
        assert student.seat_number == "A1"
    
    def test_student_with_long_strings(self):
        """Test Student creation with long strings."""
        long_name = "A" * 1000
        long_topic = "B" * 1000
        
        student = Student(long_name, "A1", long_topic, "2024-01-01 10:00:00")
        
        assert student.name == long_name
        assert student.topic == long_topic
        assert len(student.name) == 1000
        assert len(student.topic) == 1000
