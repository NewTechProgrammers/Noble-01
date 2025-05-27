import socket
import cbor2
import uuid
from datetime import datetime
from inputs import get_gamepad

# Server data
SERVER_IP = "192.168.4.1"
SERVER_PORT = 9155
DEVICE_ID = f"OCU-{uuid.uuid4()}"[:12]

# Packet sending function
def send_udp_packet(sock, action):
    payload = {
        "device_id": DEVICE_ID,
        "timestamp": datetime.utcnow().isoformat(),
        "action": action
    }
    encoded = cbor2.dumps(payload)
    sock.sendto(encoded, (SERVER_IP, SERVER_PORT))

# Main loop
def gamepad_loop():
    print(f"[OCU]: OCU active as {DEVICE_ID}")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        events = get_gamepad()
        for e in events:
            if e.ev_type in ["Key", "Absolute"]:
                action = {
                    "type": "BUTTON" if e.ev_type == "Key" else "AXIS",
                    "code": e.code,
                    "state": e.state
                }
                send_udp_packet(sock, action)

if __name__ == "__main__":
    gamepad_loop()