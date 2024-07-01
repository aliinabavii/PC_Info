import platform
import psutil
import cpuinfo
import gpuinfo
import sensors

# Get system information
system_info = platform.uname()

# Display the system information
print("System Information:")
print(f"System: {system_info.system}")
print(f"Node Name: {system_info.node}")
print(f"Release: {system_info.release}")
print(f"Version: {system_info.version}")
print(f"Machine: {system_info.machine}")
print(f"Processor: {system_info.processor}")

# Get CPU information
cpu_info = cpuinfo.get_cpu_info()
print("\nCPU Information:")
print(f"Brand: {cpu_info['brand_raw']}")
print(f"Frequency: {cpu_info['hz_actual_raw']}")

# Get GPU information
gpu_info = gpuinfo.get_gpu_info()
print("\nGPU Information:")
print(f"Name: {gpu_info['name']}")
print(f"Memory: {gpu_info['memory']}")

# Get temperature sensor information
temperature_info = sensors.get_temperature()
print("\nTemperature Information:")
for key, value in temperature_info.items():
    print(f"{key}: {value} °C")

# Get network connections information
network_connections = psutil.net_connections(kind='inet')
print("\nNetwork Connections:")
for connection in network_connections:
    print(f"Local Address: {connection.laddr.ip}:{connection.laddr.port} --> Remote Address: {connection.raddr.ip}:{connection.raddr.port} ({connection.status})")

# Wait for a key press before exiting
input("Press any key to exit...")