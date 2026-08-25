def clean_text(s: str) -> str:
    """normalize text to lowercase with sinle spaces."""
    return " ".join(s.lower().split())


text = "  This is a Sample TEXT with    irregular spacing!  "
result = clean_text(text)
print(result)


def tokenize(s: str, delimeter: str = " ") -> list:
    """split text into tokens based on the specified delimiter."""
    return s.split(delimeter)


text = "today its raining heavily"
result = tokenize(text)
print(result)


def count_chars(s: str) -> dict:
    frequency = {}  # empty dictionry to store
    for char in s:  # goes through each character in the string
        if char in frequency:  # checkks if char already exists
            frequency[char] += 1  # increase its count
        else:
            frequency[char] = 1  # new occurance ,so count 1
    return frequency
    # returns final dictiinary


print(count_chars("hellooo1AB2"))
