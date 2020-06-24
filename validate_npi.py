def validate_npi(npi):
    valid = False  # assume in the beginning that number hasn't been validated
    data_type = type(npi)
    # check what datatype npi is
    if data_type is str:
        # parameter is a string
        # check if it has 10 characters
        if len(npi) == 10:
            # number has the valid number of characters
            try:
                npi = int(npi)
                data_type = type(npi)  # update the datatype after successful conversion
            except ValueError:
                print('[Wrong input]: Could not convert to integer')
        else:
            print('[Wrong input]: Number should have 10 digits')
    if data_type is int:
        # parameter is an integer
        # check if number has 10 digits
        if count_digits(npi) == 10:
            last_digit = npi % 10  # store the check digit (last digit from ltr)
            npi = npi // 10  # discard the last digit
            sum_digits = calculate_sum(npi)
            check_digit = checksum(sum_digits)
            valid = check_digit == last_digit
        else:
            print('[Wrong input]: Number should have 10 digits')
    if not (data_type is int or data_type is str):
        print('[Wrong input]: Input is not of the required type')

    return valid


CONST = 24


def count_digits(num: int) -> int:
    """
    Counts how many digits are present in a number
    :param num:
    :return: returns the number of digits in an integer
    :rtype: int
    """
    num_digits = 0
    # so far as the number is greater than zero
    while num > 0:
        num_digits += 1
        num = num // 10  # integer divide to get rid of the last digit
    return num_digits


def calculate_sum(npi: int) -> int:
    sum_digits = 0
    while npi > 0:
        even_digit = npi % 10  # gets every second digit going from rtl
        npi = npi // 10  # discard stored digit
        even_digit *= 2  # double the digit
        # check if product greater than 9
        if even_digit > 9:
            # doubling a single digit would always result in at most a two digit number.
            # Using modulo and integer division to get the unit's and ten's value respectively
            even_digit = even_digit % 10 + even_digit // 10
        odd_digit = npi % 10
        npi = npi // 10  # discard the stored number
        sum_digits = sum_digits + even_digit + odd_digit  # calculate the sum
    return sum_digits


def checksum(num: int) -> int:
    """
    Calculates what the check digit is given
    the sum of digits using Luhn's algorithm
    :param num:
    :return: returns the check digit
    :rtype: int
    """
    num += CONST  # for 10 digits add constant
    unit = num % 10  # get the units value
    check_digit = 0
    if unit > 0:
        check_digit = 10 - unit
    return check_digit


def test_suite(tests):
    result = ('FAILED :(', 'PASSED :)',)
    passes = 0
    fails = 0
    num_tests = len(tests)
    for count, test in enumerate(tests):
        print(f'Running test {count + 1} {40 * "."}')
        outcome = validate_npi(test[0])
        passed = outcome == test[1]
        if passed:
            passes += 1
        else:
            fails += 1
        print(f'{test[2]} -> {test[0]}')
        print(f'[{result[passed]}]: Expected - {test[1]} | Outcome - {outcome}')
        print(f'{70 * "+"}')

    print('\nTest Summary')
    print(70 * '-')
    print(f'Run {num_tests} test cases')
    print(f'{passes}/{num_tests} cases passed' * (passes > 0))
    print(f'{fails}/{num_tests} cases failed' * (fails > 0))


if __name__ == '__main__':
    test_cases = [(1245319599, True, 'Testing valid npi integer'),
                  ('1234567893', True, 'Testing valid npi string'),
                  (1245319594, False, 'Testing npi integer with invalid check digit'),
                  ('1234567890', False, 'Testing npi string with invalid check digit'),
                  (1212343, False, 'Testing integer with less than 10 digits'),
                  ('23577986', False, 'Testing string with less than 10 digits'),
                  (75435678744567, False, 'Testing integer with more than 10 digits'),
                  ('965435445654', False, 'Testing string with more than 10 digits'),
                  (1003864190, True, 'Testing valid npi integer with 0 check digit'),
                  ('1376104430', True, 'Testing valid npi string with 0 check digit'),
                  (1453.446565, False, 'Testing invalid input; type float'),
                  (True, False, 'Testing invalid input; type bool'),
                  ('13463r6807', False, 'Testing valid string length containing invalid character(s)')]
    test_suite(test_cases)
