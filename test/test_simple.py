import pytest
from datetime import datetime
from app.dto import Student
from app.views import generate_seat_numbers, append_to_que, check_student_in_que, current_que


class TestSimpleUnitTests:
    """Simple unit tests that don't require Flask context."""
    
    def test_student_creation(self):
        """Test creating a Student object."""
        student = Student("John Doe", "A1", "Code bug/error", "2024-01-01 10:00:00")
        assert student.name == "John Doe"
        assert student.seat_number == "A1"
        assert student.topic == "Code bug/error"
        assert student.time_of_request == "2024-01-01 10:00:00"
    
    def test_student_string_representation(self):
        """Test student string representation."""
        student = Student("John Doe", "A1", "Code bug/error", "2024-01-01 10:00:00")
        expected = "Student(name=John Doe, seat_number=A1, topic=Code bug/error, time_of_request = 2024-01-01 10:00:00)"
        assert str(student) == expected
    
    def test_generate_seat_numbers(self):
        """Test seat number generation."""
        seats = generate_seat_numbers()
        assert len(seats) == 105  # 15 letters * 7 numbers
        assert "A1" in seats
        assert "B2" in seats
        assert "P7" in seats
        assert "G1" not in seats  # G is missing from alphabet
    
    def test_append_to_que(self):
        """Test adding students to queue."""
        # Clear queue first
        current_que.clear()
        
        student = Student("John Doe", "A1", "Code bug/error", "2024-01-01 10:00:00")
        append_to_que(student)
        
        assert len(current_que) == 1
        assert current_que[0].name == "John Doe"
    
    def test_check_student_in_que(self):
        """Test checking if student exists in queue."""
        # Clear queue first
        current_que.clear()
        
        # Add a student
        student1 = Student("John Doe", "A1", "Code bug/error", "2024-01-01 10:00:00")
        append_to_que(student1)
        
        # Check for same seat number
        student2 = Student("Jane Smith", "A1", "HTML/CSS/Bootstrap issue", "2024-01-01 10:01:00")
        assert check_student_in_que(student2) == True
        
        # Check for different seat number
        student3 = Student("Bob Johnson", "B2", "Code bug/error", "2024-01-01 10:02:00")
        assert check_student_in_que(student3) == False
    
    def test_multiple_students_in_queue(self):
        """Test multiple students in queue."""
        # Clear queue first
        current_que.clear()
        
        students = [
            Student("Alice", "A1", "Code bug/error", "2024-01-01 10:00:00"),
            Student("Bob", "B2", "HTML/CSS/Bootstrap issue", "2024-01-01 10:01:00"),
            Student("Charlie", "C3", "Understanding the lab exercises", "2024-01-01 10:02:00")
        ]
        
        for student in students:
            append_to_que(student)
        
        assert len(current_que) == 3
        assert current_que[0].name == "Alice"
        assert current_que[1].name == "Bob"
        assert current_que[2].name == "Charlie"
    
    def test_student_with_different_data_types(self):
        """Test student with different data types."""
        # Test with integer seat number
        student = Student("John Doe", 1, "Code bug/error", "2024-01-01 10:00:00")
        assert student.seat_number == 1
        
        # Test with different topics
        topics = [
            "PyCharm/Conda/Flask issue",
            "HTML/CSS/Bootstrap issue",
            "Code bug/error",
            "Understanding the lab exercises",
            "Other"
        ]
        
        for topic in topics:
            student = Student("John Doe", "A1", topic, "2024-01-01 10:00:00")
            assert student.topic == topic
    
    def test_empty_queue_operations(self):
        """Test operations on empty queue."""
        # Clear queue first
        current_que.clear()
        
        assert len(current_que) == 0
        
        # Check student in empty queue
        student = Student("John Doe", "A1", "Code bug/error", "2024-01-01 10:00:00")
        assert check_student_in_que(student) == False
    
    def test_seat_number_validation(self):
        """Test seat number validation logic."""
        seats = generate_seat_numbers()
        
        # Valid seats
        assert "A1" in seats
        assert "B2" in seats
        assert "C3" in seats
        assert "P7" in seats
        
        # Invalid seats
        assert "G1" not in seats  # G is missing
        assert "A8" not in seats  # Numbers only go to 7
        assert "Z1" not in seats  # Z is not in alphabet
        assert "AA1" not in seats  # Double letters
        assert "A10" not in seats  # Double digits
    
    def test_student_edge_cases(self):
        """Test student creation with edge cases."""
        # Empty strings
        student = Student("", "", "", "")
        assert student.name == ""
        assert student.seat_number == ""
        assert student.topic == ""
        assert student.time_of_request == ""
        
        # Special characters
        student = Student("José María", "A-1", "Code bug/error", "2024-01-01 10:00:00")
        assert student.name == "José María"
        assert student.seat_number == "A-1"
        
        # Long strings
        long_name = "A" * 1000
        student = Student(long_name, "A1", "Code bug/error", "2024-01-01 10:00:00")
        assert len(student.name) == 1000 