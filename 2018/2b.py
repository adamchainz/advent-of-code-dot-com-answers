#!/usr/bin/env python
def main():
    with open('2.txt', 'r') as fp:
        box_ids = [x.strip() for x in fp.readlines()]

    sorted_box_ids = sorted(box_ids)
    reverse_sorted_box_ids = sorted(box_ids, key=reverse_string)

    for search_box_ids in (sorted_box_ids, reverse_sorted_box_ids):
        for previous_box_id, box_id in zip(search_box_ids, search_box_ids[1:]):
            diff_count = sum((a != b for a, b in zip(previous_box_id, box_id)))
            if diff_count == 1:
                answer = ''.join((a for a, b in zip(previous_box_id, box_id) if a == b))
                print(answer)
                return


def reverse_string(string):
        return ''.join(reversed(string))


if __name__ == '__main__':
    main()
