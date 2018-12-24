#!/usr/bin/env python
import re
from collections import defaultdict, namedtuple

Claim = namedtuple('Claim', ['id', 'x', 'y', 'width', 'height'])
claim_re = re.compile(
    r'^#(?P<id>\d+) @ (?P<x>\d+),(?P<y>\d+): (?P<width>\d+)x(?P<height>\d+)$'
)


def main():
    claims = load_claims()

    non_overlapped_claim_ids = set()
    squares_by_claims = defaultdict(lambda: defaultdict(set))
    for claim in claims:
        non_overlapped_claim_ids.add(claim.id)
        for i in range(claim.width):
            for j in range(claim.height):
                square_claims = squares_by_claims[claim.x + i][claim.y + j]
                if square_claims:
                    non_overlapped_claim_ids.discard(claim.id)
                    non_overlapped_claim_ids.difference_update(square_claims)
                square_claims.add(claim.id)

    print(list(non_overlapped_claim_ids)[0])


def load_claims():
    claims = []
    with open('3.txt', 'r') as fp:
        for line in fp.readlines():
            groups = claim_re.match(line)
            if not groups:
                raise ValueError(f"Didn't match {repr(line)}")
            claims.append(Claim(
                id=int(groups['id']),
                x=int(groups['x']),
                y=int(groups['y']),
                width=int(groups['width']),
                height=int(groups['height']),
            ))
    return claims


if __name__ == '__main__':
    main()
