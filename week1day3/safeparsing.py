def safe_parse_int(value):
    try:
        number = int(value)
        return number
    except ValueError:
        return None

# Examples
print(safe_parse_int("123"))     # 123
print(safe_parse_int("hello"))   # None
print(safe_parse_int("45"))      # 45