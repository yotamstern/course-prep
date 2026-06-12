

def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    return " ".join(words[word] for word in sentence.split())


def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def prime_generator(start):
    num = start
    while True:
        if is_prime(num):
            yield num
        num += 1


def first_prime_over(n):
    primes = prime_generator(n+1)
    return next(primes)


def parse_ranges(ranges_string):
    pairs_generator = ((int(start), int(end)) for pair in ranges_string.split(',') for start, end in [pair.strip().split("-")])
    range_generator = (num for (start, end) in pairs_generator for num in range(start, end+1))
    return range_generator

def gen_secs():
    secs_gen = (seconds for seconds in range(60))
    return secs_gen

def gen_minutes():
    mins_gen = (minutes for minutes in range(60))
    return mins_gen

def gen_hours():
    hours_gen = (hours for hours in range(24))
    return hours_gen

def gen_time():
    for h in gen_hours():
        for m in gen_minutes():
            for s in gen_secs():
                yield "%02d:%02d:%02d" % (h, m, s)

def gen_years(start=2026):
    current_year = start
    while True:
        yield current_year
        current_year += 1

def gen_months():
    months_gen = (hours for hours in range(1, 13))
    return months_gen

def gen_days(month, leap_year=True):
    months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    total_days = 29 if (leap_year and month == 2) else months[month]
    return (day for day in range(1, total_days + 1))


def gen_date():
        for y in gen_years():
            is_leap = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
            for m in gen_months():
                for d in gen_days(m, is_leap):
                    for time in gen_time():
                        yield f"{d:02d}/{m:02d}/{y:04d} {time}"
def main():
    #print(translate("el gato esta en la casa"))
    #print(first_prime_over(1000000))
    #print(list(parse_ranges("1-2,4-4,8-10")))
    #print(list(parse_ranges("0-0,4-8,20-21,43-45")))
    timeline = gen_date()
    print(next(timeline))


if __name__ == '__main__':
    main()

