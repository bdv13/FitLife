import time

WATER_PER_KG_ML = 30
ML_IN_LITER = 1000
DELAY_SECONDS = 0.2


def calc_bmi(user_weight, user_height):
    """Calculate body mass index (BMI)."""
    return user_weight / (user_height**2)


def calc_water_needed(user_weight):
    """Calculate recommended daily water intake (in liters)."""
    return user_weight * WATER_PER_KG_ML / ML_IN_LITER


def display_results(user_name, user_age, bmi, water_needed):
    """Display the results to the user"""
    print(
        f"{user_name}, thank you for waiting!\n"
        f"Your age: {user_age} years\n"
        f"Your body mass index (BMI): {bmi:.1f}\n"
        f"Recommended daily water intake: {water_needed:.2f} l\n"
        "Calculation complete. Stay healthy!",
    )


def main():
    """Main function to run the FitLife application."""
    print("Welcome to FitLife!", end="\n\n")

    user_name = input("Hi, what is your name? ")

    try:
        user_age = int(input("Please enter your age: "))
    except ValueError:
        print("Please enter a valid age (number).")
        return

    try:
        user_weight = float(input("Please enter your weight in kg: "))
    except ValueError:
        print("Please enter a valid weight (e.g., 70.5).")
        return

    try:
        user_height = float(input("Please enter your height in meters: "))
    except ValueError:
        print("Please enter a valid height (e.g., 1.75).")
        return

    bmi = calc_bmi(user_weight, user_height)
    water_needed = calc_water_needed(user_weight)

    print(
        "Thank you! Calculating BMI and water intake...",
        end="\n\n",
    )
    time.sleep(DELAY_SECONDS)
    display_results(user_name, user_age, bmi, water_needed)


if __name__ == "__main__":
    main()
