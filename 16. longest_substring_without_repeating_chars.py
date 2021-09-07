def lengthOfLongestSubstring(s: str) -> int:
    max_len = 0
    current_window = ""

    for _, current_char in enumerate(s):
        if current_char not in current_window:
            current_window += current_char
        else:
            current_window = ""
        max_len = max(max_len, len(current_window))

    return max_len


print(lengthOfLongestSubstring("pwwkew"))
