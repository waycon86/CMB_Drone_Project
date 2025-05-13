from dronekit import connect, VehicleMode, LocationGlobalRelative
import dronekit_sitl
import time

# Start the simulator with quad model and valid GPS
sitl = dronekit_sitl.start_default()
sitl.launch(['--model', 'quad', '--home=38.1452,-76.4279,10,0'])

connection_string = sitl.connection_string()
print("Connecting to simulated drone...")
vehicle = connect(connection_string, wait_ready=True)

def arm_and_takeoff(target_altitude):
    print("Arming motors...")
    
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True
    
    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)
        
    print(f"Taking off to {target_altitude} meters...")
    vehicle.simple_takeoff(target_altitude)
    
    #Wait until the vehicle reaches a safe height or timeout
    start_time = time.time()
    timeout = 20 # seconds
    
    while True:
        alt = vehicle.location.global_relative_frame.alt
        print(f" Altitude: {alt:.2f} meters")
        
        if alt >= target_altitude * 0.95:
            print("Reached target altitude.")
            break
        
        if time.time() - start_time > timeout:
            print("Timeout: altitude not reached.")
            break
        
        time.sleep(1)