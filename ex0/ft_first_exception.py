def check_temperature(temp_str: str) -> None:
    try:
        temperature = int(temp_str)
        if 0 <= temperature <= 40:
            print(f"Temperature {temperature}°C is perfect for plants!\n")
        elif temperature < 0:
            print(f"Error: {temperature}°C is too cold for plants (min 0°C)\n")
        else:
            print(f"Error: {temperature}°C is too hot for plants (max 40°C)\n")
    except ValueError:
        print(f"Error: {temp_str} is not a valid number\n")


def test_temperature_input() -> None:
    print("Testing temperature: 25")
    check_temperature("25")
    print("Testing temperature: abc")
    check_temperature("abc")
    print("Testing temperature: 100")
    check_temperature("100")
    print("Testing temperature: -50")
    check_temperature("-50")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature_input()
    print("All tests completed - program didn’t crash!")
