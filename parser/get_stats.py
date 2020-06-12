#!/usr/bin/env python3
import sys
import string

default_input_file = 'sample_log.txt'



def main(*args):
    arg_count = len(args)

    if arg_count == 0:
        input_file = default_input_file
    elif arg_count == 1:
        input_file = args[0]
    else:
        print('Invalid arguments.')
        return None

    input_fh = open(input_file, 'r')
    input_data = input_fh.readlines()
    parsed_data_set = []
    data_set = []

    for data_line in input_data:
        line_date_time = data_line.split(None, 1)
        if len(line_date_time) != 2: continue

        date_time = line_date_time[0]

        line_snapshot =  line_date_time[1].split('  :', 1)
        if len(line_snapshot) != 2: continue

        line_values = line_snapshot[1].split('Old=', 1)
        if len(line_values) != 2: continue

        line_new = line_values[1].split('New=', 1)
        old = line_new[0]
        new = line_new[1]

        old = old[:-7]
        new = new[:-7]

        data = [date_time, old, new]
        parsed_data_set.append(data)

    for data in parsed_data_set:
        data_set.append([(data[0]), (data[1])])
        data_set.append([(data[0]), (data[2])])

    average = calculate_average_rate(data_set)
    print('Average Rate: {:0.3f}(MBps)'.format(average))

    max = find_maximum_value(data_set)
    print('Maximum Rate: {:0.3f}(MBps) at {}'.format(float(max[1]), max [0] ))

    min = find_minimum_value(data_set)
    print('Minimum Rate: {:0.3f}(MBps) at {}'.format(float(min[1]), min[0]))

    mid = find_middle_value(data_set)
    print('Middle Rate: {:0.3f}(MBps) at {}'.format(float(mid[1]), mid[0]))


def calculate_average_rate(data_set):
    count = 0
    sum = 0

    for data in data_set:
        sum = sum + float(data[1])
        count = count + 1

    return sum / count


def find_maximum_value(data_set):
    result = sorted(data_set, key=lambda x: float(x[1]))

    return result[len(result)-1]


def find_minimum_value(data_set):
    result = sorted(data_set, key=lambda x: float(x[1]))

    return result[0]


def find_middle_value(data_set):
    result = sorted(data_set, key=lambda x: float(x[1]))
    return result[int(len(result)/2)]


if __name__ == '__main__': main()