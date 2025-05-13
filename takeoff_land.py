from dronekit import connect, VehicleMode, LocationGlobalRelative
import dronekit_sitl
import time

# Start the simulator
sitl = dronekit_sitl.start_default()
sitl.launch(['--model', 'quad', '--home=38.1452,-76.2479,10,0'])

connection_string = sitl.connection_string()

# Connect to the vehicle
print("Connecting to simulated drone...")
vehicle = connect(connection_string, wait_ready=True)

# Function to arm and take off
def arm_and_takeoff(target_altitude):
    print("Arming motors...")

    # Set mode to GUIDED and arm
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True
    
    # Wait until the vehicle is armed
    while not vehicle.armed:
        print("Waiting for arming...")
        time.sleep(1)
        
    print(f"Taking off to {target_altitude} meters...")
    vehicle.simple_takeoff(target_altitude)
    
    # Wait until the drone reaches target altitude
    while True:
        alt = vehicle.location.global_relative_frame.alt
        print(f" Current altitude: {alt:.2f} meters")
        if alt >= target_altitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(1)

# Takeoff and land sequence
arm_and_takeoff(10)  # Take off to 10 meters

print("Hovering for 5 seconds...")
time.sleep(5)

print("Landing...")
vehicle.mode = VehicleMode("LAND")

# Wait until landed
while vehicle.armed:
    print(" Waiting for landing...")
    time.sleep(1)
    
# Clean up
vehicle.close()
sitl.stop()
print("Simulation complete.")
