# -*- coding: utf-8 -*-

__all__ = ["tabulate"]


"""
Extend `tabulate` module with prime print format.
"""

import tabulate as tabulate_module

from tabulate import tabulate, DataRow, Line, TableFormat

prime_format = TableFormat(
    lineabove=None,
    linebelowheader=Line("", "-", "+", ""),
    linebetweenrows=None,
    linebelow=None,
    headerrow=DataRow("", "|", ""),
    datarow=DataRow("", "|", ""),
    padding=1, with_header_hide=None
)

tabulate_module._table_formats["prime"] = prime_format

_pad_row = tabulate_module._pad_row
_build_row = tabulate_module._build_row
_build_line = tabulate_module._build_line
