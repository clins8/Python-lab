class InvalidAgeException(Exception):
    "Raised when the input value is less than 18"
    pass
a = [10, 20, 30]
def test_value_error():
    try:
        no = int(input("Enter non numeric value:"))
        print("ENtered:",no)
    except ValueError as e:
        print("Invalid inpu:",e)
    finally:
        print("Final blocl executed")
def test_zero_division_error():
    try:
        numerator = int(input("Enter numerator:"))
        denominator = int(input("Enter denomerator:"))
        rsult = numerator/denominator
        print("result:",rsult)
    except ZeroDivisionError as e:
        print("cannot divivde by zero:",e)
    finally:
        print("Final blocl executed")
        
def test_index_error():
    try:
        number = int(input("Enter index (0-2) to test IndexError: "))
        print("Value at index:", a[number])
    except IndexError:
        print("Index is out of range.")
    finally:
        print("Finally block executed")

def test_invalid_age_exception():
    try:
        age = int(input("ENeter age less then 18"))
        if age < 18:
            raise InvalidAgeException("MInor UH")
        else:
            print("Eligible to vote")
    except InvalidAgeException as e:
        print("error")
    finally:
        print("exec")
def test_general_exception():
    try:
        number = int(input("Enter a number to test general exception: "))
        print("You entered:", number)
    except Exception as e:
        print("An error occurred:", e)
    finally:
        print("Finally block executed")
def main():
    print("Testing ValueError")
    test_value_error()

    print("\nTesting ZeroDivisionError")
    test_zero_division_error()

    print("\nTesting IndexError")
    test_index_error()

    print("\nTesting Custom InvalidAgeException")
    test_invalid_age_exception()

    print("\nTesting General Exception")
    test_general_exception()
main()
print("\nAll tested")
