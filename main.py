import serial 
from serial.tools import list_ports

portList = list(list_ports.comports())

f = open("arduino_data.txt", "r")
file_header = f.readline().split('\t')[:-1]
f.close()

with open("arduino_data.txt", "a") as f:

    while True:
        portList = list(list_ports.comports())
        row_list = [',', ',', ',', ',', '\n']
#         print(len(portList))
        for port in portList:
            try:
                ser_handle = serial.Serial(port.device, 19200, timeout=2)
                data = ser_handle.readline().decode('utf-8').rstrip()

                data = data+','

#                 print(type(data))
                ser_handle.close()
                device_id = port.hwid.split()[2][4:]
                col_idx = file_header.index(device_id)
                row_list[col_idx] = data

            except:
                continue 

        empty_data_fields = row_list.count(',')
        if empty_data_fields < 4: 
            print(f'Reading from {4-empty_data_fields} devices.')
            # print(row_list)
            f.writelines(row_list)
            f.flush()


    f.close()