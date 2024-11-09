from .french_numbers import digits, units, tens


def process_unit(num: int) -> str:
    return units[num]


def process_tens(num: int) -> str:
    ten_idx = num // 10
    reminder = num % 10

    if num < 20:
        return process_unit(num)

    if ten_idx in (1, 2, 3, 4, 5, 6):
        return tens[ten_idx] + (
            ("-et-" if reminder == 1 else "-") + process_unit(reminder)
            if reminder
            else ""
        )
    if ten_idx == 7:
        return tens[ten_idx] + (
            ("-et-" if reminder == 1 else "-") + process_unit(10 + reminder)
            if reminder
            else ""
        )
    if ten_idx == 8:
        return tens[ten_idx] + ("-" + process_unit(reminder) if reminder else "s")
    if ten_idx == 9:
        return tens[ten_idx] + ("-" + process_unit(10 + reminder) if reminder else "")


def process_hundreds(num: int) -> str:
    hundred = num // 100
    reminder = num % 100

    if num < 100:
        return process_tens(num)

    ret = f"{digits[hundred-1]}-cent" if hundred > 1 else "cent"
    ret += "s" if hundred > 1 and not reminder else ""
    ret += f"-{process_tens(reminder)}" if reminder else ""

    return ret


def process_thousands(num: int) -> str:
    num_str: str = str(num)
    s_thousands = slice(0, -3)
    s_hunders = slice(-3, None)
    thousands = int(num_str[s_thousands])
    hundreds = int(num_str[s_hunders])

    ret = f"{process_hundreds(thousands)}-mille" if thousands > 1 else "mille"
    ret += f"-{process_hundreds(hundreds)}" if hundreds > 0 else ""
    return ret


def process_millions(num: int) -> str:
    num_str: str = str(num)
    s_millions = slice(0, -6)
    s_thousands = slice(-6, None)
    millions = int(num_str[s_millions])
    thousands = int(num_str[s_thousands])

    ret = f"{process_hundreds(millions)}-million"
    ret += "s" if millions > 1 else ""
    ret += f"-{process_thousands(thousands)}" if thousands > 0 else ""
    return ret


def process(num: int) -> str:
    ret: str = ""

    # Boundaries conditions
    if num < 0:
        raise ValueError("Negative values are not authorized.")
    if num >= 1_000_000_000:
        raise ValueError("Number must be less than a billion.")

    # Base cases
    if num == 0:
        return "zéro"

    if num < 20:
        ret = process_unit(num)
    elif num < 100:
        ret = process_tens(num)
    elif num < 1_000:
        ret = process_hundreds(num)
    elif num < 1_000_000:
        ret = process_thousands(num)
    elif num < 1_000_000_000:
        ret = process_millions(num)

    return ret
