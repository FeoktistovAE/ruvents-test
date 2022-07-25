import pandas as pd


def get_items_from_xlsx(path_to_file, column):
    with pd.ExcelFile(path_to_file) as xlsx:
        df = pd.read_excel(xlsx, 'Tasks', skiprows=2, header=None)
        items = df[column].values
        return items


def count_even_numbers(path_to_file):
    items = get_items_from_xlsx(path_to_file, 1)
    number_of_evens = len([i for i in items if i % 2 == 0])
    return f'В столбце num1 {number_of_evens} четных чисел'


def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True


def count_prime_numbers(path_to_file):
    items = get_items_from_xlsx(path_to_file, 2)
    number_of_primes = len([i for i in items if is_prime(i)])
    return f'В столбце num2 {number_of_primes} простых чисел'


def count_less_point_five(path_to_file):
    items = get_items_from_xlsx(path_to_file, 3)
    float_items = (float(i.replace(',', '.').replace(' ', '')) for i in items)
    number_of_values = len([i for i in float_items if i < 0.5])
    return f'В столбце num3 {number_of_values} чисел, меньших 0.5.'


def count_tuesdays(path_to_file):
    items = get_items_from_xlsx(path_to_file, 4)
    tuesdays = []
    for i in items:
        try:
            if pd.Timestamp(i).day_name() == 'Tuesday':
                tuesdays.append(i)
        except ValueError:
            print(f'Unparsed: {i}')
    return f'В столбце date1 {len(tuesdays)} вторников.'


def count_tuesdays2(path_to_file):
    items = get_items_from_xlsx(path_to_file, 5)
    number_of_teusedays = len([i for i in items if pd.Timestamp(i).day_name() == 'Tuesday'])
    return f'В столбце date2 {number_of_teusedays} вторников.'


def is_last_tuesday(date):
    parsed_date = pd.Timestamp(date)
    last_tuesday = (parsed_date - pd.offsets.Day()) + pd.offsets.LastWeekOfMonth(n=1, weekday=1)
    if parsed_date == last_tuesday:
        return True
    return False


def count_last_tuesdays(path_to_file):
    items = get_items_from_xlsx(path_to_file, 6)
    number_of_last_tuesdays = len([i for i in items if is_last_tuesday(i)])
    return f'В столбце date3 {number_of_last_tuesdays} полследних вторников месяца.'
