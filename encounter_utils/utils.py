import typing

from numpy import random

__all__ = [
    "generate_code",
]

RU_ALPHABET = list("укенгшхварясмт")
EN_ALPAHBET = list("wertyupasdfghjkzxcvbn")
NUMBERS = list("12456789")


def generate_code(mask: str, n: int = 1, seed: int = None) -> typing.List[str]:
    if seed:
        random.seed(seed)
    codes = []
    for sym in mask:
        alphabet = {
            sym in x: x
            for x in [RU_ALPHABET, EN_ALPAHBET, NUMBERS]
        }[True]
        let = random.choice(alphabet, n, True)
        codes.append(let)
    codes = ["".join(seq) for seq in zip(*codes)]
    return codes


if __name__ == '__main__':
    res = generate_code("ффф11", 10)
    print(res)
