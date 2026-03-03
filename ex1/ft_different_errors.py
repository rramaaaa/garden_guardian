def garden_operations() -> None:
    try:
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    try:
        _ = 10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    try:
        fd = open("missing.txt")
        fd.close()
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError:  {e}")

    try:
        plants = {"rose": 1, "lily": 5}
        _ = plants["missing_plant"]
    except KeyError as e:
        print(f"Caught KeyError: {e}")

    try:
        int("abc")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")


def test_error_types() -> None:
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    print()
    print("Testing ZeroDivisionError...")
    try:
        _ = 10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    print()
    print("Testing FileNotFoundError...")
    try:
        fd = open("missing.txt")
        fd.close()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file ’missing.txt’")

    print()
    print("Testing KeyError...")
    try:
        plants = {"rose": 1, "lily": 5}
        _ = plants["missing_plant"]
    except KeyError as e:
        print(f"Caught KeyError: {e}")

    print()
    print("\nTesting multiple errors together...")
    try:
        int("abc")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")

    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
