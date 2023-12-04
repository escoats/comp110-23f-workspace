"""EX10 - Dictionary related utility functions."""

from csv import DictReader

__author__ = "730659395"


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read CSV file and return as a list of dicts with headers as keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
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
        # for each key (header), make a dictionary entry with all the column calues
        result[key] = column_values(table, key)
    return result


def head(table: dict[str, list[str]], num_rows: int) -> dict[str, list[str]]:
    """Returns a table with the first (num_rows) rows of data for each column."""
    result: dict[str, list[str]] = {}
    if len(table.keys()) <= num_rows:
        return table
    for column in table.keys():
        row: list[str] = []
        for i in range(0, num_rows):
            row.append(table[column][i])
        result[column] = row
    return result


def select(table: dict[str, list[str]], col_names: list[str]) -> dict[str, list[str]]:
    """Creates a new table with a subset of the original columns."""
    result: dict[str, list[str]] = {}
    for column in table.keys():
        if column in col_names:
            result[column] = table[column]
    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two tables."""
    result: dict[str, list[str]] = {}
    for column in table1.keys():
        result[column] = table1[column]
    for column in table2.keys():
        if column in table1.keys():
            for elem in table2[column]:
                result[column].append(elem)
        else:
            result[column] = table2[column]
    return result


def count(vals_list: list[str]) -> dict[str, int]:
    """Counts how many times each value appears in a list."""
    result: dict[str, int] = {}
    for elem in vals_list:
        if elem in result:
            result[elem] += 1
        else:
            result[elem] = 1
    return result