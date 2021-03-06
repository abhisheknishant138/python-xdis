# (C) Copyright 2017, 2019 by Rocky Bernstein
"""
CPython 2.3 bytecode opcodes

This is a like Python 2.3's opcode.py with some additional classification
of stack usage, and opererand formatting functions.
"""

import xdis.opcodes.opcode_2x as opcode_2x
from xdis.opcodes.base import (
    finalize_opcodes,
    format_CALL_FUNCTION_pos_name_encoded,
    format_MAKE_FUNCTION_arg,
    format_extended_arg,
    init_opdata,
    update_pj2,
)

version = 2.3
python_implementation = "CPython"

l = locals()
init_opdata(l, opcode_2x, version)

update_pj2(globals(), l)

opcode_arg_fmt = {
    "CALL_FUNCTION": format_CALL_FUNCTION_pos_name_encoded,
    "CALL_FUNCTION_KW": format_CALL_FUNCTION_pos_name_encoded,
    "CALL_FUNCTION_VAR_KW": format_CALL_FUNCTION_pos_name_encoded,
    "EXTENDED_ARG": format_extended_arg,
    "MAKE_FUNCTION": format_MAKE_FUNCTION_arg,
}

finalize_opcodes(l)
