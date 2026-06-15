import time
import random
from src.sensor import WaterLevelSensor
from src.config import ThresholdConfig
from src.dashboard import Dashboard

def run_simulation():

    print("\033[95m[SYSTEM] Initializing EDODS Core Monitoring System...\033[0m")

    config = ThresholdConfig(warningLevel=12.0, criticalLevel=22.0)

    sensor = WaterLevelSensor(sensorID="Dam-Sensor-01", status="OK", initialLevel=10.0)
 
    dashboard = Dashboard(sensors=[sensor], config=config)
    
    print("\033[94m[CONFIG] Thresholds Configured -> Warning: 12.0m | Critical: 22.0m\033[0m")
    print("\033[92m[SENSOR] WaterLevelSensor 'Dam-Sensor-01' online.\033[0m")
    print("-" * 60)
    
    try:
        while True:
            change = random.uniform(-1.5, 2.5)
            new_level = max(0.0, sensor.getWaterLevel() + change)
            
            sensor.transmitData(forcedValue=new_level)

            dashboard.updateChart(new_level)
            
            status = dashboard.checkThreshold(new_level)
            
            if status.name == "CRITICAL":
                color_code = "\033[91m"
            elif status.name == "WARNING":
                color_code = "\033[93m"
            else:
                color_code = "\033[92m"
                
            print(f"[{time.strftime('%H:%M:%S')}] Sensor Level: {dashboard.displayStatus:5.2f}m | Status: {color_code}{status.name:<8}\033[0m")
            
            time.sleep(1.0)
            
    except KeyboardInterrupt:
        print("\n\033[95m[SYSTEM] Simulation terminated by user.\033[0m")

if __name__ == "__main__":
    run_simulation()
