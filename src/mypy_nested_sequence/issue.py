from __future__ import annotations

from mypy_nested_sequence import _NestedSequence

v: _NestedSequence[int]
v1: _NestedSequence[int]
v2: _NestedSequence[int]
v3: _NestedSequence[int]
v4: _NestedSequence[int]


# Fails as expected:
# Incompatible types in assignment (expression has type "int", variable has type "_NestedSequence[int]")  [assignment]mypy(error)
v = 1

# Does not fail as expected
v1 = [1]
# Does not fail as expected
v2 = [[1]]

# Does not fail, but I expected a failure
v3 = ["a"]
v4 = [["a"]]
