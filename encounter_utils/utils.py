import typing

from numpy.random import choice

__all__ = [
    "generate_code",
]

RU_ALPHABET = list("укенгшзхфвапрожячсмитбю")
EN_ALPAHBET = list("wertyuopasdfghjkzxcvbn")
NUMBERS = list("0123456789")


def generate_code(mask: str, n: int = 1) -> typing.List[str]:
    codes = []
    for sym in mask:
        alphabet = {
            sym in x: x
            for x in [RU_ALPHABET, EN_ALPAHBET, NUMBERS]
        }[True]
        let = choice(alphabet, n, True)
        codes.append(let)
    codes = ["".join(seq) for seq in zip(*codes)]
    return codes


if __name__ == '__main__':
    res = generate_code("ффф11", 10)
    print(res)
