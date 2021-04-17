# import packages
import serial 
from serial.tools import list_ports

# list the plugged devices
portList = list(list_ports.grep('ACM'))

# open file to read header (column names)
print('Reading column names..')
f = open("data_log.txt", "r")
file_header = f.readline().split('\t')[:-1]
f.close()

# open file to append data
print('Opening file to append data..')
with open("data_log.txt", "a") as f:
# main loop
    print('Entering into main loop..')
    while True:
        portList = list(list_ports.grep('ACM'))
        row_list = [',', ',', ',', ',', '\n']
        # loop over the available ports
        for port in portList:
            try:
                # open serial port
                ser_handle = serial.Serial(port.device, 19200, timeout=2)
                # read serial data
                data = ser_handle.readline().decode('utf-8').rstrip()+','
                # close the port
                ser_handle.close()
                # get the corresponding device ID
                device_id = port.hwid.split()[2][4:]
                # match the column name
                col_idx = file_header.index(device_id)
                # put data into list
                row_list[col_idx] = data

            except:
                continue 
        # count empty data fields out of four ports
        empty_data_fields = row_list.count(',')
        # check if the there is data available from at least one port
        if empty_data_fields < 4: 
            print(f'Reading from {4-empty_data_fields} devices.')
            # write into file
            f.writelines(row_list)
            f.flush()
    f.close()