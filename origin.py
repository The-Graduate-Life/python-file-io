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

    
def find_matches_in_file(input_path, pattern):
    """
    Find all matches of a regex pattern in a file.

    Args:
        input_path (str): Path to the input text file.
        pattern (re.Pattern): Compiled regex pattern.

    Yields:
        tuple: (line_number, matched_word)
    """
    with open(input_path, 'r') as in_file:
        for line_number, line in enumerate(in_file, start=1):
            matches = pattern.findall(line)
            for match in matches:
                yield line_number, match


def write_matches(output_path, matches):
    """
    Write matches to an output file.

    Args:
        output_path (str): Path to the output file.
        matches (iterable): Iterable of (line_number, word) tuples.
    """
    with open(output_path, 'w') as out_file:
        for line_number, word in matches:
            out_file.write(f"{line_number}\t{word}\n")


def main():
    """
    Main execution function.

    Defines the pattern for heritability-related words,
    processes the input file, and writes results to output file.
    """
    input_file = "origin.txt"
    output_file = "heritability_related.txt"

    # Flexible regex patterns
    pattern_str = r'\b(inherit\w*|heritable\w*)\b'

    pattern = compile_pattern(pattern_str)
    matches = find_matches_in_file(input_file, pattern)
    write_matches(output_file, matches)
