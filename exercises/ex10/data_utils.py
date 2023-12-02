"""Dictionary related utility functions."""

from csv import DictReader

__author__ = "730659395"

# Define your functions below

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read CSV file and return as a list of dicts with headers as keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader: DictReader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Return a list of all values under a specific header."""
    result: list[str] = []
    # loop through each element (dictionary) in list
    for dictionary in table:
        # for each dictionary, get the value whose key corresponds to header and add that to result
        result.append(dictionary[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformats data so it's a dictionary with column heads as keys."""
    result: dict[str, list[str]] = {}
    # loop through keys of one row of the table to get the headers
    first_row: dict[str, str] = table[0]
    for key in first_row:
        # for each key (header), amke a dictionary entry with all the column calues
        result[key] = column_values(table, key)
    return result

def head(table: dict[str, list[str]], num_rows: int) -> dict[str, list[str]]:
    result: dict[str, list[str]]
    for column in table:
        pass