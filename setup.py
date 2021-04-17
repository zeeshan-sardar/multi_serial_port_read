from serial.tools import list_ports

device_ids = []
portList = list(list_ports.comports())
for port in portList:
    device_ids.append(port.hwid.split()[2][4:]+"\t")
device_ids.append('\n')

with open("arduino_data.txt", "w") as f:
    f.writelines(device_ids)
    f.close()