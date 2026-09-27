# Regenerative Braking System

mass = float(input("Enter vehicle mass (kg): "))
initial_speed = float(input("Enter initial speed (km/h): "))
final_speed = float(input("Enter final speed (km/h): "))
efficiency = float(input("Enter regeneration efficiency (%): "))

# Convert speed from km/h to m/s
v1 = initial_speed / 3.6
v2 = final_speed / 3.6

# Kinetic energy before and after braking
energy_initial = 0.5 * mass * v1 ** 2
energy_final = 0.5 * mass * v2 ** 2

# Energy available during braking
energy_lost = energy_initial - energy_final

# Energy recovered by regenerative braking
energy_recovered = energy_lost * (efficiency / 100)

# Convert joules to Wh
energy_wh = energy_recovered / 3600

print("\n--- Regenerative Braking Results ---")
print(f"Energy available for braking: {energy_lost:.2f} J")
print(f"Energy recovered: {energy_recovered:.2f} J")
print(f"Energy recovered: {energy_wh:.2f} Wh")
