
def compute_daily_averages(rows, ts_col, value_col):
    daily_values = {}
    for row in rows:                              #get only the date part: YYYY-MM-DD
        date = row[ts_col][:10]

        value =float(row[value_col])              #covert the value from string to numbers

        if date not in daily_values:
            daily_values[date] = []

        daily_values[date].append(value)

    averages = {}
    for date, values in daily_values.items():
        averages[date] = sum(values) / len(values)

    return averages


def find_spikes(rows, values_col, top):
    sorted_rows = sorted( rows, key=lambda row: float(row[value_col]),reverse=True)

    return sorted_rows[:top]