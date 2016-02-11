# -*- coding: utf-8 -*-

__all__ = ["tabulate_prime"]


"""
Extend `tabulate` module with prime print format.
"""

import tabulate as tabulate_module
from tabulate import DataRow, Line, TableFormat

prime_format = TableFormat(
    lineabove=None,
    linebelowheader=Line("", "-", "-", ""),
    linebetweenrows=None,
    linebelow=None,
    headerrow=DataRow("", " ", ""),
    datarow=DataRow("", " ", ""),
    padding=0, with_header_hide=None
)

tabulate_module._table_formats["prime"] = prime_format
orig_tabulate = tabulate_module.tabulate


def tabulate_prime(tabular_data):
    """
    This `tabulate` function only support prime table requirement, just as ETL stuffs.
    """
    # treat the second column as normal values.
    tabular_data = [([row[0]] + ["|"] + row[1:]) for row in tabular_data]

    # print table as customized format.
    output = orig_tabulate(tabular_data, headers="firstrow",
                           tablefmt="prime", stralign="right",)
    lines = output.split("\n")

    # add "+" sign to horizontal line row.
    first_line = lines[0]
    second_line = lines[1]
    sign_idx = first_line.index("|")
    chars_in_line_2 = list(second_line)
    chars_in_line_2[sign_idx] = "+"
    lines[1] = "".join(chars_in_line_2)

    # align the second horizontal line row.
    last_line = lines[-1]
    max_width = len(last_line)
    lines[1] = lines[1][0:max_width]

    # remote the column after "+" sign
    lines = [line[0:sign_idx - 2] + line[sign_idx] + line[sign_idx + 2:] for line in lines]

    output = "\n".join(lines)
    return output
