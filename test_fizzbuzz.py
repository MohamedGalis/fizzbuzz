from fizzbuzz import fizzbuzz

def test_no_criteria():
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(2) == "2"

def test_even_multiples_of_3():
    assert fizzbuzz(12) == "Fizz"
    assert fizzbuzz(6) == "Fizz"


def test_divisble_by_5():
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(10) == "Buzz"

def test_divisble_by_3_5():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"

def test_odd_mutiples_3():
    assert fizzbuzz(3) == "FizzOdd"
    assert fizzbuzz(9) == "FizzOdd"
