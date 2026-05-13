import time


WATER_PER_KG_ML = 30
ML_IN_LITER = 1000


def calc_bmi(user_weight, user_height):
    """Calculate body mass index (BMI)."""
    return user_weight / (user_height ** 2)


def calc_water_needed(user_weight):
    """Calculate recommended daily water intake (in liters)."""
    return user_weight * WATER_PER_KG_ML / ML_IN_LITER


def display_results(user_name, user_age, bmi, water_needed):
    """Display the results to the user"""
    print(
        f'{user_name}, thank you for waiting!\n'
        f'Your age: {user_age} years\n'
        f'Your body mass index (BMI): {bmi:.1f}\n'
        f'Recommended daily water intake: {water_needed:.2f} l\n'
        f'Calculation complete. Stay healthy!'
    )


def main():
    """Main function to run the FitLife application."""
    print('Welcome to FitLife!', end='\n\n')

    user_name = input(
        'Hi, what is your name? ')

    while True:
        try:
            user_age = int(input('Please enter your age: '))
            break
        except ValueError:
            print('Please enter a valid age (number).')

    while True:
        try:
            user_weight = float(input('Please enter your weight in kg: '))
            break
        except ValueError:
            print('Please enter a valid weight (e.g., 70.5).')

    while True:
        try:
            user_height = float(input('Please enter your height in meters: '))
            break
        except ValueError:
            print('Please enter a valid height (e.g., 1.75).')

    bmi = calc_bmi(user_weight, user_height)
    water_needed = calc_water_needed(user_weight)

    print()
    print('Thank you, your data has been saved. '
          'Calculating BMI and water intake...', end='\n\n')
    time.sleep(0.2)
    display_results(user_name, user_age, bmi, water_needed)


if __name__ == '__main__':
    main()
