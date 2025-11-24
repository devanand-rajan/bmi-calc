def calculate_bmi(weight_kg, height_m):

    if weight_kg <= 0 or height_m <= 0:
        return None  # Return None for invalid input

    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

def interpret_bmi(bmi):

    if bmi is None:
        return "Invalid input. Weight and height must be positive values."

    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else: # bmi >= 30
        return "Obesity"

def get_user_input(prompt, unit):

    while True:
        try:
            value = float(input(f"{prompt} ({unit}): "))
            if value <= 0:
                print("Error: Input must be a positive number.")
                continue
            return value
        except ValueError:
            print("Error: Invalid input. Please enter a numerical value.")

def main():

    print("--- BMI Calculator ---")

    # Get valid weight input
    weight = get_user_input("Enter your weight", "kg")


    height = get_user_input("Enter your height", "meters")

    # Calculate and interpret BMI
    bmi_value = calculate_bmi(weight, height)
    category = interpret_bmi(bmi_value)

    print("\n--- Results ---")

    if bmi_value is not None:
        print(f"Your Weight: {weight:.2f} kg")
        print(f"Your Height: {height:.2f} meters")
        print(f"Calculated BMI: {bmi_value}")
        print(f"BMI Category: {category}")
    else:
        print(f"Calculation failed: {category}")

# Check if the script is being run directly
if __name__ == "__main__":
    main()