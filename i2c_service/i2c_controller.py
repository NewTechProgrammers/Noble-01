import smbus2
import time

BUS_ID = 1
bus = smbus2.SMBus(BUS_ID)

def send_i2c_command(address: int, command: bytes):
    try:
        length = len(command)
        bus.write_i2c_block_data(address, 0x00, [length] + list(command))
        print(f"[I2C]: Sent to 0x{address:02X}: {command}")
    except Exception as e:
        print(f"[ERROR]: I2C send failed: {e}")