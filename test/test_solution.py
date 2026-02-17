"""
Unit tests for the solution module.
"""

from app.solution import main


def test_main():
    """Test that main function exists and can be called."""
    # Basic test to ensure the main function exists
    assert callable(main)
    # Call main - should not raise any exceptions
    main()
