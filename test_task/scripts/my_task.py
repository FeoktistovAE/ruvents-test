#! usr/bin/python/env python

import argparse
from test_task.logic.task_logic import count_even_numbers, count_prime_numbers, count_less_point_five, count_tuesdays, count_tuesdays2, count_last_tuesdays


def main():
    parser = argparse.ArgumentParser(description='Select the task you want to complete')
    parser.add_argument('path_to_xlsx', help='put path to your file here')
    parser.add_argument('task', choices=['num1', 'num2', 'num3', 'date1', 'date2', 'date3'])
    args = parser.parse_args()
    if args.task == 'num1':
        print(count_even_numbers(args.path_to_xlsx))
    elif args.task == 'num2':
        print(count_prime_numbers(args.path_to_xlsx))
    elif args.task == 'num3':
        print(count_less_point_five(args.path_to_xlsx))
    elif args.task == 'date1':
        print(count_tuesdays(args.path_to_xlsx))
    elif args.task == 'date2':
        print(count_tuesdays2(args.path_to_xlsx))
    elif args.task == 'date3':
        print(count_last_tuesdays(args.path_to_xlsx))


if __name__ == '__main__':
    main()