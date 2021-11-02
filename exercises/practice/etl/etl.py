from typing import Dict, List


# The first step in writing this function was having a look at etl_test.py to find out
# what format the legacy data was in, and what the expected output was supposed to be.
# I decided to add type hints to the function signature to serve as a reminder of what
# how exactly the data was stored and how it is transformed.
def transform(legacy_data: Dict[int, List[str]]) -> Dict[str, int]:
    """
    Take Scrabble scores stored in a legacy format and return it in the new format
    """
    # Initialise what we're going to return
    new_score_map = {}

    # Iterating over dict.items() returns a (key, value) tuple, which we can unpack
    for score, letter_list in legacy_data.items():
        for letter in letter_list:
            new_score_map[letter.lower()] = score

    return new_score_map
