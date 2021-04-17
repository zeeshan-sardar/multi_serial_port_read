from serial.tools import list_ports

# get available ports
device_ids = []
portList = list(list_ports.grep('ACM'))

# get device IDs of the available ports
for port in portList:
    device_ids.append(port.hwid.split()[2][4:]+"\t")
device_ids.append('\n')

# writing the IDs as column names of the log data file
with open("data_log.txt", "w") as f:
    f.writelines(device_ids)
    f.close()


