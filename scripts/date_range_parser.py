# date_range_parser.py

import re
from datetime import datetime, timedelta

def parse_date_range(date_range_str: str) -> tuple[str, str]:
    """
    Parses a US English style date range string and returns a tuple of
    (start_date_iso, end_date_iso) in ISO standard format (YYYY-MM-DD).

    Handles:
    - Single dates: "October 26, 2025" -> ("2025-10-26", "2025-10-26")
    - Ranges within the same month: "October 26–31, 2025" -> ("2025-10-26", "2025-10-31")
    - Ranges spanning different months: "April 26–May 1, 2025" -> ("2025-04-26", "2025-05-01")
    - Ranges spanning different years: "December 25, 2025–January 5, 2026" -> ("2025-12-25", "2026-01-05")
    - Uses both en-dash (–) and hyphen (-) as separators.

    Args:
        date_range_str: The input date range string.

    Returns:
        A tuple of two strings (start_date_iso, end_date_iso).

    Raises:
        ValueError: If the input string format is invalid or the end date
                    is before the start date.
    """

    # Normalize separator (en-dash to hyphen for simpler regex)
    date_range_str = date_range_str.replace('–', '-')

    # Regex for single date or date range
    # Group 1: Month name (e.g., "October")
    # Group 2: Start day (e.g., "26")
    # Group 3 (optional): End day (e.g., "31") for same-month range
    # Group 4 (optional): Month name for end date (e.g., "May")
    # Group 5 (optional): End day for different-month range
    # Group 6: Year for start date (e.g., "2025")
    # Group 7 (optional): Year for end date (e.g., "2026")

    # Pattern for "Month Day-Day, Year" or "Month Day, Year"
    pattern_same_month_or_single = re.compile(
        r'([A-Za-z]+)\s*(\d{1,2})(?:-(\d{1,2}))?,\s*(\d{4})'
    )
    # Pattern for "Month Day-Month Day, Year"
    pattern_diff_month_same_year = re.compile(
        r'([A-Za-z]+)\s*(\d{1,2})-(\s*[A-Za-z]+\s*\d{1,2}),\s*(\d{4})'
    )
    # Pattern for "Month Day, Year-Month Day, Year"
    pattern_diff_year = re.compile(
        r'([A-Za-z]+)\s*(\d{1,2}),\s*(\d{4})-(\s*[A-Za-z]+\s*\d{1,2},\s*\d{4})'
    )

    month_to_num = {
        'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5,
        'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10,
        'November': 11, 'December': 12
    }

    start_date = None
    end_date = None

    # Try to match patterns
    match_same_month = pattern_same_month_or_single.match(date_range_str)
    match_diff_month = pattern_diff_month_same_year.match(date_range_str)
    match_diff_year = pattern_diff_year.match(date_range_str)

    if match_diff_year:
        # Example: "December 25, 2025-January 5, 2026"
        start_month_str, start_day_str, start_year_str, end_part_str = match_diff_year.groups()

        start_month = month_to_num.get(start_month_str, None)
        if start_month is None:
            raise ValueError(f"Invalid month name in start date: {start_month_str}")
        start_day = int(start_day_str)
        start_year = int(start_year_str)
        start_date = datetime(start_year, start_month, start_day)

        # Parse the end part (e.g., "January 5, 2026")
        end_part_match = re.match(r'([A-Za-z]+)\s*(\d{1,2}),\s*(\d{4})', end_part_str.strip())
        if not end_part_match:
            raise ValueError(f"Invalid format for end date in multi-year range: {end_part_str}")
        end_month_str, end_day_str, end_year_str = end_part_match.groups()

        end_month = month_to_num.get(end_month_str, None)
        if end_month is None:
            raise ValueError(f"Invalid month name in end date: {end_month_str}")
        end_day = int(end_day_str)
        end_year = int(end_year_str)
        end_date = datetime(end_year, end_month, end_day)

    elif match_diff_month:
        # Example: "April 26-May 1, 2025"
        start_month_str, start_day_str, end_part_str, year_str = match_diff_month.groups()

        year = int(year_str)
        start_month = month_to_num.get(start_month_str, None)
        if start_month is None:
            raise ValueError(f"Invalid month name in start date: {start_month_str}")
        start_day = int(start_day_str)
        start_date = datetime(year, start_month, start_day)

        # Parse the end part (e.g., "May 1")
        end_part_match = re.match(r'([A-Za-z]+)\s*(\d{1,2})', end_part_str.strip())
        if not end_part_match:
            raise ValueError(f"Invalid format for end date in cross-month range: {end_part_str}")
        end_month_str, end_day_str = end_part_match.groups()

        end_month = month_to_num.get(end_month_str, None)
        if end_month is None:
            raise ValueError(f"Invalid month name in end date: {end_month_str}")
        end_day = int(end_day_str)
        end_date = datetime(year, end_month, end_day)

    elif match_same_month:
        # Example: "October 26-31, 2025" or "October 26, 2025"
        month_str, start_day_str, end_day_str, year_str = match_same_month.groups()

        year = int(year_str)
        month = month_to_num.get(month_str, None)
        if month is None:
            raise ValueError(f"Invalid month name: {month_str}")
        start_day = int(start_day_str)
        start_date = datetime(year, month, start_day)

        if end_day_str:
            end_day = int(end_day_str)
            end_date = datetime(year, month, end_day)
        else:
            # Single date
            end_date = start_date
    else:
        raise ValueError(f"Could not parse date range format: '{date_range_str}'")

    if start_date is None or end_date is None:
        raise ValueError("Failed to extract both start and end dates.")

    if start_date > end_date:
        raise ValueError(f"Start date ({start_date.strftime('%Y-%m-%d')}) cannot be after end date ({end_date.strftime('%Y-%m-%d')}).")

    return start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')

# Example Usage (for demonstration, include this in your test script or interactive session)
if __name__ == "__main__":
    test_cases = [
        ("October 26–31, 2025", ("2025-10-26", "2025-10-31")),
        ("October 26-31, 2025", ("2025-10-26", "2025-10-31")), # with hyphen
        ("October 26, 2025", ("2025-10-26", "2025-10-26")),
        ("April 26–May 1, 2025", ("2025-04-26", "2025-05-01")),
        ("December 25, 2025–January 5, 2026", ("2025-12-25", "2026-01-05")),
        ("January 1-5, 2025", ("2025-01-01", "2025-01-05")),
        ("March 8, 2024 - April 1, 2025", ("2024-03-08", "2025-04-01")),
        # Error cases
        ("Invalid Date String", ValueError),
        ("October 31–26, 2025", ValueError), # end date before start date
        ("Oct 26, 2025", ValueError), # abbreviated month
    ]

    print("--- Running Test Cases ---")
    for input_str, expected in test_cases:
        try:
            result = parse_date_range(input_str)
            print(f"Input: '{input_str}' -> Output: {result}")
            assert result == expected or expected == ValueError, f"Test failed for '{input_str}'. Expected {expected}, got {result}"
        except ValueError as e:
            print(f"Input: '{input_str}' -> Error: {e}")
            assert expected == ValueError, f"Expected no error for '{input_str}', but got: {e}"
        except Exception as e:
            print(f"Input: '{input_str}' -> Unexpected Error: {e}")
            assert False, f"Unexpected error for '{input_str}': {e}"
    print("--- Test Cases Finished ---")
