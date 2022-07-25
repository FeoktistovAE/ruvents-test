#! usr/bin/python/env python

import argparse
from test_task.logic import task_logic
def main():
    parser = argparse.ArgumentParser(description='Select the task you want to complete')
    parser.add_argument('path_to_xlsx', help='put path to your file here')
    parser.add_argument('task', choices=['num1', 'num2', 'num3', 'date1', 'date2', 'date3'], help='choose column here')
    args = parser.parse_args()
    if args.task == 'num1':
        print(task_logic.count_even_numbers(args.path_to_xlsx))
    elif args.task == 'num2':
        print(task_logic.count_prime_numbers(args.path_to_xlsx))
    elif args.task == 'num3':
        print(task_logic.count_less_point_five(args.path_to_xlsx))
    elif args.task == 'date1':
        print(task_logic.count_tuesdays(args.path_to_xlsx))
    elif args.task == 'date2':
        print(task_logic.count_tuesdays2(args.path_to_xlsx))
    elif args.task == 'date3':
        print(task_logic.count_last_tuesdays(args.path_to_xlsx))


if __name__ == '__main__':
    main()