def calculate_bmi(weight, height, metric='metric'):
    """Calculate the Body Mass Index (BMI) of a person."""
    if metric == 'english':
        # Convert pounds to kilograms
        weight_kg = weight * 0.453592
        # Convert feet and inches to meters
        height_inches = height[0] * 12 + height[1]
        height_m = height_inches * 0.0254
    else:
        weight_kg = weight
        height_m = height

    return weight_kg / (height_m ** 2)

def get_input(metric):
    if metric == 'english':
        weight = float(input("Enter weight in pounds: "))
        feet = int(input("Enter height in feet: "))
        inches = int(input("Enter height in inches: "))
        height = (feet, inches)
    else:
        weight = float(input("Enter weight in kilograms: "))
        height = float(input("Enter height in meters: "))
    
    return weight, height

metric_choice = input("Choose metric system (english/metric): ").lower()
if metric_choice not in ['english', 'metric']:
    print("Invalid choice. Using metric system by default.")
    metric_choice = 'metric'

weight, height = get_input(metric_choice)
bmi = calculate_bmi(weight, height, metric_choice)
print(f"Your BMI is: {bmi:.2f}")
