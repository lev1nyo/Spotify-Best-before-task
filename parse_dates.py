import sys
import datetime

import itertools


def main():

    def parse_date(year, month, day):
        try:
            year = int(year) + 2000 if int(year) < 1000 else int(year)
            return datetime.date(int(year), int(month), int(day))
        except ValueError:
            return False

    try:
        filename = sys.argv[1]
    except IndexError:
        print("Missing file name!")
        exit()

    with open(filename) as f:
        for line in [l.rstrip('\n') for l in f]:
            parts = line.split('/')

            dates = []

            for (year, month, day) in itertools.permutations(parts, 3):
                date = parse_date(year, month, day)
                if date and 2000 <= date.year < 3000:
                    dates.append(date)

            if len(dates) > 0:
                print(min(dates))
                    
            else:
                print(line + ' is illegal')


if __name__ == '__main__':
    main()
