from datetime import datetime, timedelta

def generate_date_range(start_date, end_date):
    """
    Generates a list of dates between the given start_date and end_date (inclusive).
    
    Args:
        start_date (str): Start date in the format "YYYY-MM-DD".
        end_date (str): End date in the format "YYYY-MM-DD".
    
    Returns:
        list: List of dates between start_date and end_date (inclusive).
    """
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        
        date_range = []
        current_date = start
        while current_date <= end:
            date_range.append(current_date.strftime("%Y-%m-%d"))
            current_date += timedelta(days=1)
        
        return date_range
    except ValueError:
        return "Invalid date format. Please provide dates in the format 'YYYY-MM-DD'."

# Example usage:
start_date = "2020-06-03"
end_date = "2020-06-05"
result = generate_date_range(start_date, end_date)
print(result)  # Output: ['2020-06-03', '2020-06-04', '2020-06-05']