class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant(name: str, is_wilting: bool) -> None:
    if is_wilting:
        raise PlantError(f"The {name} plant is wilting!")


def check_water(water_level: int) -> None:
    if water_level < 10:
        raise WaterError("Not enough water in the tank!")


def catch_error() -> None:
    print("Testing PlantError...")
    try:
        check_plant("tomato", True)
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print()
    print("Testing WaterError...")
    try:
        check_water(1)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print()
    print("Testing catching all garden errors...")
    try:
        check_plant("tomato", True)
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        check_water(4)
    except GardenError as e:
        print(f"Caught a garden error: {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    catch_error()
    print("\nAll custom error types work correctly!")
