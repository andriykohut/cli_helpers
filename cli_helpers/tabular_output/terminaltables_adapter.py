# -*- coding: utf-8 -*-
"""Format adapter for the terminaltables module."""

import terminaltables

from .preprocessors import (bytes_to_string, align_decimals,
                            override_missing_value)

supported_formats = ('ascii', 'double', 'github')
preprocessors = (bytes_to_string, override_missing_value, align_decimals)


def adapter(data, headers, table_format=None, **_):
    """Wrap terminaltables inside a function for TabularOutputFormatter."""

    table_format_handler = {
        'ascii': terminaltables.AsciiTable,
        'double': terminaltables.DoubleTable,
        'github': terminaltables.GithubFlavoredMarkdownTable,
    }

    try:
        table = table_format_handler[table_format]
    except KeyError:
        raise ValueError('unrecognized table format: {}'.format(table_format))

    t = table([headers] + data)
    return t.table
