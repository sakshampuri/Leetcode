'''

Explanation:

Problem category -> Sliding window

We start withempty window and keep on adding each character to the window
while adding the characters, we keep track of the most frequently occured characters in the current window size
This allows us to check for the minority occuring character length against the threshold replacement value: k

If the minority characters - represented by length of the window - majority characters - are greater than threshold k,
we decrease the size of the window from the front

Keeping track of max window size is the solution

why is mac_char_in_cur_window not updated when window_start index is changed?
Because we're only concerned about the max window size size and to consider that, we only need to keep track and look forward
to a value which is greater than what is occured. A smaller value will not affect the max window size that is possible.

'''
from typing import Dict


def characterReplacement(s: str, k: int) -> int:
    letter_count: Dict[str, int] = {}
    window_start = max_chars_in_cur_window = max_window_size = 0

    for window_end, current_char in enumerate(s):
        letter_count[current_char] = letter_count.get(current_char, 0) + 1
        max_chars_in_cur_window = max(
            max_chars_in_cur_window, letter_count[current_char])

        if window_end - window_start + 1 - max_chars_in_cur_window > k:
            letter_count[s[window_start]] -= 1
            window_start += 1

        max_window_size = max(max_window_size, window_end - window_start + 1)

    return max_window_size


print(characterReplacement("AABABBA", 1))
