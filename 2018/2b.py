#!/usr/bin/env python
def main():
    with open('2.txt', 'r') as fp:
        box_ids = [x.strip() for x in fp.readlines()]

    sorted_box_ids = sorted(box_ids)
    sorted_reverse_box_ids = sorted([''.join(reversed(b)) for b in box_ids])

    searches = [
        (sorted_box_ids, False),
        (sorted_reverse_box_ids, True),
    ]

    for search_box_ids, reverse_answer in searches:
        previous = None
        for box_id in search_box_ids:
            if previous is not None:
                diff_count = sum([a != b for a, b in zip(previous, box_id)])
                if diff_count == 1:
                    answer = ''.join([a for a, b in zip(previous, box_id) if a == b])
                    if reverse_answer:
                        answer = ''.join(reversed(answer))
                    print(answer)
                    return
            previous = box_id


if __name__ == '__main__':
    main()
