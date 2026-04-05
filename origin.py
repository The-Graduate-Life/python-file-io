#!/usr/bin/env python3
"""
text_pattern_finder.py

This module reads a text file, searches for words matching a given
regular expression pattern, and writes the results to an output file.

Each match is written as:
<line_number>\t<matched_word>

The module is reusable and allows different input files and patterns.
"""

import re


def compile_pattern(pattern_str, ignore_case=True):
    """
    Compile a regular expression pattern.

    Args:
        pattern_str (str): The regex pattern as a string.
        ignore_case (bool): Whether to ignore case when matching.

    Returns:
        re.Pattern: Compiled regex pattern.
    """
    flags = re.IGNORECASE if ignore_case else 0
    return re.compile(pattern_str, flags)
