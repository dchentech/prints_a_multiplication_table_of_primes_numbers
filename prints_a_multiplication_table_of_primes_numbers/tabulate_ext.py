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
    headerrow=DataRow("", "", ""),
    datarow=DataRow("", "", ""),
    padding=0, with_header_hide=None
)

tabulate_module._table_formats["prime"] = prime_format

_pad_row = tabulate_module._pad_row
_build_row = tabulate_module._build_row
_build_line = tabulate_module._build_line

orig_tabulate = tabulate_module.tabulate


def tabulate_prime(tabular_data):
    """
    This `tabulate` function only support prime table requirement.
    """
    # treat the second column as normal values.
    tabular_data = [([row[0]] + ["|"] + row[1:]) for row in tabular_data]

    # print table as customized format.
    output = orig_tabulate(tabular_data, headers="firstrow",
                           tablefmt="prime", stralign="center",)

    # add "+" sign to horizontal line row.
    lines = output.split("\n")
    sign_idx = lines[0].index("|")
    chars_in_line_2 = list(lines[1])
    chars_in_line_2[sign_idx] = "+"
    lines[1] = "".join(chars_in_line_2)
    output = "\n".join(lines)

    return output
