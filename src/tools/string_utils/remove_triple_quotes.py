"""
This module provides a function to process text between delimiters.

The main function in this module is `process_between_delimiters`, which can either remove or return the text between the first and second occurrence of a specified delimiter in a given text.
"""

import re

def process_between_delimiters(text, delimiter, return_inside=False):
    """
    Process text between the first and second occurrence of a specified delimiter.

    This function either removes or returns the text between the first and second occurrence of a specified delimiter in a given text, depending on the value of `return_inside`.

    Args:
        text (str): The text to process.
        delimiter (str): The delimiter to use for processing the text.
        return_inside (bool, optional): Whether to return the text inside the delimiters. Defaults to False.

    Returns:
        str: The processed text.
    """
    pattern = re.escape(delimiter) + r'(.*?)' + re.escape(delimiter)
    matches = re.findall(pattern, text, flags=re.DOTALL)

    if return_inside:
        # Return the text inside the first pair of delimiters
        return matches[0] if matches else ''
    else:
        # Remove the text between the first pair of delimiters
        return re.sub(pattern, '', text, flags=re.DOTALL, count=1)