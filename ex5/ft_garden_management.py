class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self) -> None:
        self.plants = {}

    def add_plant(self, plant_name: str, water_level: int, sunlight_hours: int) -> None:
        if not plant_name or plant_name == "":
            raise PlantError("Plant name cannot be empty!")
        if water_level < 1:
            raise PlantError(f"Water level {water_level} is too low (min 2)")
        if water_level > 10:
            raise PlantError(f"Water level {water_level} is too high (max 10)")
        if sunlight_hours < 2:
            raise PlantError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
        if sunlight_hours > 12:
            raise PlantError(
                f"Sunlight hours {sunlight_hours} is too high (max 12)"
            )
        self.plants[plant_name] = {"water_level": water_level, "sunlight_hours": sunlight_hours}
        print(f"Plant {plant_name} is healthy!")

    def water_plants(self, tank_level: int) -> None:
        print("Opening watering system")
        try:
            if tank_level < len(self.plants):
                raise WaterError("Not enough water in tank")
            for plant in self.plants:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name: str) -> None:
        if plant_name not in self.plants:
            raise PlantError(f"Plant {plant_name} not found in garden!")
        plant = self.plants[plant_name]
        water = plant["sunlight_hours"]
        if water < 3:
            raise WaterError(f"Water level {water} is too low (min 3)")
        print(f"{plant_name}: healthy (water: {water}, sun: {sun})")


def test_garden_management() -> None:
    print("=== Garden Management System ===")
    manager = GardenManager()
    print()
    print("Adding plants to garden...")
    for name, water, sun in [("tomato", 5, 8), ("lettuce", 4, 6), ("", 5, 8)]:
        try:
            manager.add_plant(name, water, sun)
        except PlantError as e:
            print(f"Error adding plant: {e}")
    print()
    print("Watering plants...")
    try:
        manager.water_plants(tank_level=10)
    except WaterError as e:
        print(f"Watering error: {e}")
    print()
    print("Checking plant health...")
    for name, water, sun in [("tomato", 5, 8), ("lettuce", 15, 6)]:
        try:
            manager.check_plant_health(name)
        except (PlantError, WaterError) as e:
            print(f"Error checking {name}: {e}")
    print()
    print("Testing error recovery...")
    try:
        manager.water_plants(tank_level=0)
    except WaterError as e:
        print(f"Caught GardenError: {e}")
    print("System recovered and continuing...")
    print()
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
