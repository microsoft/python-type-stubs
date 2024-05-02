from array import array
from typing import Any, Literal, LiteralString

from sympy.core.numbers import Integer, Rational
from sympy.matrices import Matrix
from sympy.utilities.decorator import doctest_depends_on

class NonInvertibleCipherWarning(RuntimeWarning):
    def __init__(self, msg) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def warn(self, stacklevel=...) -> None:
        ...
    


def AZ(s=...) -> LiteralString | str | list[Any | str]:
    ...

bifid5 = ...
bifid6 = ...
bifid10 = ...
def padded_key(key, symbols) -> str:
    ...

def check_and_join(phrase, symbols=..., filter=...) -> str:
    ...

def cycle_list(k, n) -> list[int]:
    ...

def encipher_shift(msg, key, symbols=...) -> str:
    ...

def decipher_shift(msg, key, symbols=...) -> str:
    ...

def encipher_rot13(msg, symbols=...) -> str:
    ...

def decipher_rot13(msg, symbols=...) -> str:
    ...

def encipher_affine(msg, key, symbols=..., _inverse=...) -> str:
    ...

def decipher_affine(msg, key, symbols=...) -> str:
    ...

def encipher_atbash(msg, symbols=...) -> str:
    ...

def decipher_atbash(msg, symbols=...) -> str:
    ...

def encipher_substitution(msg, old, new=...) -> str:
    ...

def encipher_vigenere(msg, key, symbols=...) -> LiteralString:
    ...

def decipher_vigenere(msg, key, symbols=...) -> str:
    ...

def encipher_hill(msg, key, symbols=..., pad=...) -> str:
    ...

def decipher_hill(msg, key, symbols=...) -> str:
    ...

def encipher_bifid(msg, key, symbols=...) -> str:
    ...

def decipher_bifid(msg, key, symbols=...) -> str:
    ...

def bifid_square(key) -> Matrix:
    ...

def encipher_bifid5(msg, key) -> str:
    ...

def decipher_bifid5(msg, key) -> str:
    ...

def bifid5_square(key=...) -> Matrix:
    ...

def encipher_bifid6(msg, key) -> str:
    ...

def decipher_bifid6(msg, key) -> str:
    ...

def bifid6_square(key=...) -> Matrix:
    ...

def rsa_public_key(*args, **kwargs) -> tuple[Any, Any] | tuple[Any, Any | int] | Literal[False]:
    ...

def rsa_private_key(*args, **kwargs) -> tuple[Any, Any] | tuple[Any, Any | int] | Literal[False]:
    ...

def encipher_rsa(i, key, factors=...):
    ...

def decipher_rsa(i, key, factors=...):
    ...

def kid_rsa_public_key(a, b, A, B) -> tuple[Any, Any]:
    ...

def kid_rsa_private_key(a, b, A, B) -> tuple[Any, Any]:
    ...

def encipher_kid_rsa(msg, key):
    ...

def decipher_kid_rsa(msg, key):
    ...

morse_char = ...
char_morse = ...
def encode_morse(msg, sep=..., mapping=...) -> str:
    ...

def decode_morse(msg, sep=..., mapping=...) -> LiteralString:
    ...

def lfsr_sequence(key, fill, n) -> list[Any]:
    ...

def lfsr_autocorrelation(L, P, k) -> Rational | Integer:
    ...

def lfsr_connection_polynomial(s) -> int:
    ...

def elgamal_private_key(digit=..., seed=...) -> tuple[Any | int | array[int] | None, int | Any | None, int | Any]:
    ...

def elgamal_public_key(key) -> tuple[Any, Any, Any]:
    ...

def encipher_elgamal(i, key, seed=...) -> tuple[Any, Any]:
    ...

def decipher_elgamal(msg, key):
    ...

def dh_private_key(digit=..., seed=...) -> tuple[Any | int | array[int] | None, int | Any | None, int | Any]:
    ...

def dh_public_key(key) -> tuple[Any, Any, Any]:
    ...

def dh_shared_key(key, b):
    ...

def gm_private_key(p, q, a=...) -> tuple[Any, Any]:
    ...

def gm_public_key(p, q, a=..., seed=...) -> tuple[int | Any, Any] | Literal[False]:
    ...

def encipher_gm(i, key, seed=...) -> list[Any]:
    ...

def decipher_gm(message, key) -> int:
    ...

def encipher_railfence(message, rails) -> LiteralString:
    ...

def decipher_railfence(ciphertext, rails) -> str:
    ...

def bg_private_key(p, q) -> tuple[Any, Any]:
    ...

def bg_public_key(p, q):
    ...

def encipher_bg(i, key, seed=...) -> tuple[list[Any], int]:
    ...

def decipher_bg(message, key) -> Literal[0]:
    ...

