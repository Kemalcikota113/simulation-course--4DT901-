import random

# Define some "scientific" constants for milk modeling
GLASS_VOLUME_ML = 250  # Average volume of a glass in milliliters
POWDERED_MILK_CONCENTRATION = 1.5  # Arbitrary unit to represent milkiness

def milk_per_glass(glass_count, powdered_milk_scoops):


    """
    Calculate the 'amount of milk' per glass based on glasses and scoops of powdered milk.
    
    Parameters:
    glass_count (int): Number of glasses of milk.
    powdered_milk_scoops (int): Number of scoops of powdered milk added per glass.
    
    Returns:
    dict: Dictionary containing each glass and its 'milkiness' rating.
    """

    milkiness_per_glass = {}
    
    for i in range(1, glass_count + 1):
        # Milkiness is random to reflect real life unpredictability
        base_milkiness = random.uniform(1.0, 2.0)  # Basic milkiness of milk
        
        # Each scoop increases milkiness arbitrarily
        total_milkiness = base_milkiness + (powdered_milk_scoops * POWDERED_MILK_CONCENTRATION)
        
        # Assign to dictionary
        milkiness_per_glass[f"Glass {i}"] = round(total_milkiness, 2)
    
    return milkiness_per_glass

# Sample run
glasses_of_milk = 3
scoops_of_powdered_milk = 2

milkiness_results = milk_per_glass(glasses_of_milk, scoops_of_powdered_milk)
for glass, milkiness in milkiness_results.items():
    print(f"{glass} has a milkiness level of {milkiness} 'milk units'")
