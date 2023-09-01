"""
Test goes here

"""
from main import positive_real_number


def test_positive_real_number():
    # Test with a positive number
    result = positive_real_number(5)
    assert result is True, "Test failed for the positive number"

    # Test with zero (non-positive number)
    result = positive_real_number(0)
    assert result is False, "Test failed for zero (non-positive number)"

    # Test with a negative number
    result = positive_real_number(-5)
    assert result is False, "Test failed for the negative number"


if __name__ == "__main__":
    test_positive_real_number()
