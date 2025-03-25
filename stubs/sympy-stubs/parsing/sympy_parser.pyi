import ast
import typing_extensions
from typing import Any, Callable

null = ...
TOKEN: typing_extensions.TypeAlias = tuple[int, str]
DICT: typing_extensions.TypeAlias = dict[str, Any]
TRANS: typing_extensions.TypeAlias = Callable[[list[TOKEN], DICT, DICT], list[TOKEN]]

class ParenthesisGroup(list[TOKEN]): ...

class AppliedFunction:
    def __init__(self, function: TOKEN, args: ParenthesisGroup, exponent=...) -> None: ...
    def expand(self) -> list[TOKEN]: ...
    def __getitem__(self, index) -> Any: ...

def function_exponentiation(tokens: list[TOKEN], local_dict: DICT, global_dict: DICT) -> list[TOKEN]: ...
def split_symbols_custom(predicate: Callable[[str], bool]) -> Callable[..., list[TOKEN]]: ...

split_symbols = ...

def implicit_multiplication(tokens: list[TOKEN], local_dict: DICT, global_dict: DICT) -> list[TOKEN]: ...
def implicit_application(tokens: list[TOKEN], local_dict: DICT, global_dict: DICT) -> list[TOKEN]: ...
def implicit_multiplication_application(result: list[TOKEN], local_dict: DICT, global_dict: DICT) -> list[TOKEN]: ...
def auto_symbol(tokens: list[TOKEN], local_dict: DICT, global_dict: DICT) -> list[TOKEN]: ...
def lambda_notation(tokens: list[TOKEN], local_dict: DICT, global_dict: DICT) -> list[TOKEN]: ...
def factorial_notation(tokens: list[TOKEN], local_dict: DICT, global_dict: DICT) -> list[TOKEN]: ...
def convert_xor(tokens: list[TOKEN], local_dict: DICT, global_dict: DICT) -> list[TOKEN]: ...
def repeated_decimals(tokens: list[TOKEN], local_dict: DICT, global_dict: DICT) -> list[TOKEN]: ...
def auto_number(tokens: list[TOKEN], local_dict: DICT, global_dict: DICT) -> list[TOKEN]: ...
def rationalize(tokens: list[TOKEN], local_dict: DICT, global_dict: DICT) -> list[TOKEN]: ...
def convert_equals_signs(tokens: list[TOKEN], local_dict: DICT, global_dict: DICT) -> list[TOKEN]: ...

standard_transformations: tuple[TRANS, ...] = ...

def stringify_expr(s: str, local_dict: DICT, global_dict: DICT, transformations: tuple[TRANS, ...]) -> str: ...
def eval_expr(code, local_dict: DICT, global_dict: DICT) -> Any: ...
def parse_expr(
    s: str,
    local_dict: DICT | None = ...,
    transformations: tuple[TRANS, ...] | str = ...,
    global_dict: DICT | None = ...,
    evaluate=...,
) -> Any: ...
def evaluateFalse(s: str) -> ast.Expression: ...

class EvaluateFalseTransformer(ast.NodeTransformer):
    operators = ...
    functions = ...
    relational_operators = ...
    def visit_Compare(self, node) -> ast.Call | ast.Compare: ...
    def flatten(self, args, func) -> list[Any]: ...
    def visit_BinOp(self, node) -> ast.Call | ast.BinOp: ...
    def visit_Call(self, node) -> ast.AST: ...

_transformation = ...
transformations = ...

class _T:
    def __init__(self) -> None: ...
    def __getitem__(self, t) -> tuple[Any, ...]: ...

T = ...
