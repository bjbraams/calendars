# date_range_formatter.py

from datetime import date

def format_date_range(start_date: date, end_date: date) -> str:
    """
    Converts a pair of date objects into a standardized ISO-style date range string.

    Args:
        start_date: The starting date object.
        end_date: The ending date object.

    Returns:
        A string representing the date range in the specified ISO-style format.

    Raises:
        ValueError: If start_date is after end_date.
        TypeError: If inputs are not datetime.date objects.
    """
    if not isinstance(start_date, date) or not isinstance(end_date, date):
        raise TypeError("Both start_date and end_date must be datetime.date objects.")

    if start_date > end_date:
        raise ValueError("Start date cannot be after end date.")

    # Case 1: Single date
    if start_date == end_date:
        return start_date.strftime("%Y-%m-%d")

    # Case 2: Same year
    if start_date.year == end_date.year:
        # Case 2a: Same month
        if start_date.month == end_date.month:
            return f"{start_date.strftime('%Y-%m-%d')} to {end_date.day}"
        # Case 2b: Different months
        else:
            return f"{start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%m-%d')}"
    # Case 3: Different years
    else:
        return f"{start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}"

# Example Usage (for demonstration purposes, not part of the module itself)
if __name__ == "__main__":
    from datetime import date

    test_cases = [
        # Same month, same year
        (date(2025, 10, 26), date(2025, 10, 31), "2025-10-26 to 31"),
        # Different months, same year
        (date(2025, 4, 26), date(2025, 5, 1), "2025-04-26 to 05-01"),
        # Different years
        (date(2025, 12, 25), date(2026, 1, 5), "2025-12-25 to 2026-01-05"),
        # Single date
        (date(2025, 10, 26), date(2025, 10, 26), "2025-10-26"),
        # Another single date
        (date(2024, 3, 15), date(2024, 3, 15), "2024-03-15"),
        # Range spanning multiple years
        (date(2023, 11, 1), date(2025, 2, 28), "2023-11-01 to 2025-02-28"),
    ]

    print("--- Running Test Cases (Successful) ---")
    for start, end, expected in test_cases:
        result = format_date_range(start, end)
        print(f"Input: ({start}, {end}) -> Output: '{result}' (Expected: '{expected}')")
        assert result == expected, f"Test failed for ({start}, {end}). Expected '{expected}', got '{result}'"
    print("--- Successful Test Cases Finished ---\n")

    print("--- Running Test Cases (Error Handling) ---")
    error_cases = [
        (date(2025, 10, 31), date(2025, 10, 26), "Start date cannot be after end date."), # End date before start date
        ("not a date", date(2025,1,1), "Both start_date and end_date must be datetime.date objects."), # Invalid input type
        (date(2025,1,1), "not a date", "Both start_date and end_date must be datetime.date objects."), # Invalid input type
    ]

    for start, end, expected_error_message in error_cases:
        try:
            format_date_range(start, end)
            print(f"Test failed: Expected error for ({start}, {end}), but no error was raised.")
        except (ValueError, TypeError) as e:
            print(f"Input: ({start}, {end}) -> Error: '{e}' (Expected: '{expected_error_message}')")
            assert str(e) == expected_error_message, f"Test failed for ({start}, {end}). Expected error '{expected_error_message}', got '{e}'"
    print("--- Error Handling Test Cases Finished ---")
