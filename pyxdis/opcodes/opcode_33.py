"""
CPython 3.3 bytecode opcodes

This is used in disassembly

This is a superset of Python 3.3's opcode.py with some opcodes that simplify
parsing and semantic interpretation.
"""

from copy import deepcopy

import pyxdis.opcodes.opcode_3x as opcode_3x
from pyxdis.opcodes.opcode_3x import fields2copy, rm_op

# FIXME: can we DRY this even more?

opmap = {}
opname = [''] * 256
hasconst = []
hasjrel = []
hasjabs = []

def def_op(name, op):
    opname[op] = name
    opmap[name] = op

for object in fields2copy:
    globals()[object] =  deepcopy(getattr(opcode_3x, object))

# Below are opcodes since Python 3.2

rm_op(opname, opmap, 'STOP_CODE', 0)

def_op('YIELD_FROM', 72)

def updateGlobal():
    # JUMP_OPs are used in verification are set in the scanner
    # and used in the parser grammar
    globals().update({'PJIF': opmap['POP_JUMP_IF_FALSE']})
    globals().update({'PJIT': opmap['POP_JUMP_IF_TRUE']})
    globals().update({'JA': opmap['JUMP_ABSOLUTE']})
    globals().update({'JF': opmap['JUMP_FORWARD']})
    globals().update(dict([(k.replace('+', '_'), v) for (k, v) in opmap.items()]))
    globals().update({'JUMP_OPs': map(lambda op: opname[op], hasjrel + hasjabs)})

updateGlobal()

# FIXME: turn into pytest test
from pyxdis import PYTHON_VERSION
if PYTHON_VERSION == 3.3:
    import dis
    # for item in dis.opmap.items():
    #     if item not in opmap.items():
    #         print(item)
    assert all(item in opmap.items() for item in dis.opmap.items())

# opcode3x.dump_opcodes(opmap)
