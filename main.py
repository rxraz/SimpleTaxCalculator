def persAllow(salary):
    if salary > 100000:
        persAllowExtra = (salary - 100000) / 2
        persAllow = 12570 - persAllowExtra
    else:
        persAllow = 12570
    return persAllow


def taxCalc(salary):
    if salary <= 50270 and salary >= 12571:
        lowerBracket = 37699 * 0.2
        AfterTax = salary - lowerBracket - persAllow(salary)
    elif salary >= 50270 and salary <= 125140:
        lowerBracket = 37699 * 0.2
        higherBracket = salary - 50271
        higherBracket = higherBracket * 0.4
        AfterTax = salary - lowerBracket - higherBracket - persAllow(salary)
    elif salary > 125140:
        lowerBracket = 37699 * 0.2
        higherBracket = 74869 * 0.4
        veryHighBracket = salary - 125140
        veryHighBracket = veryHighBracket * 0.45
        AfterTax = salary - veryHighBracket - higherBracket - lowerBracket - persAllow(salary)
    return AfterTax


Salary = int(input("Input Your Salary To The Nearest Pound : "))
persAllow(Salary)
print(round(taxCalc(Salary), 2))
