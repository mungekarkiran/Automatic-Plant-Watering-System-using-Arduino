# lib's
import serial.tools.list_ports
import sqlite3
import time
from datetime import datetime

# Create a SQL connection to our SQLite database
connect = sqlite3.connect('sensor_data_test.db') # portal_mammals.sqlite
cursor = connect.cursor()

# Create table
cursor.execute("""CREATE TABLE IF NOT EXISTS soil_moisture_sensor_data (data_date TEXT, soil_moisture REAL);""")

arduino =  serial.Serial()
arduino.baudrate = 9600
arduino.port = 'COM3'
arduino.open()

while 1:
    time.sleep(2)
    current_dateTime = str(datetime.now()).split('.')[0]
    if arduino.in_waiting:
        packet = arduino.readline()
        print(packet.decode('utf').rstrip('\n'))
        sens_data = float(packet.decode('utf').rstrip('\n'))
        cursor.execute(f"""INSERT INTO soil_moisture_sensor_data VALUES ('{current_dateTime}', {sens_data});""")
        connect.commit()

# to close db connection
connect.close()