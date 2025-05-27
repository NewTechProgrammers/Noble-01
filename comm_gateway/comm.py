import socket
import cbor2
from dispatcher import dispatch_action

MAX_PACKET_SIZE = 1024

def is_valid_packet(data: dict) -> bool:
    return (
        isinstance(data, dict) and
        "device_id" in data and
        "timestamp" in data and
        "action" in data and
        isinstance(data["action"], dict)
    )

# Main loop
def run_udp_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", 9999))
    print("[UDP SERVER]: CBOR UDP server listening on 0.0.0.0:9999")

    while True:
        try:
            packet, addr = sock.recvfrom(MAX_PACKET_SIZE)
            data = cbor2.loads(packet)

            if not is_valid_packet(data):
                print(f"[WARN]: Invalid packet from {addr}")
                continue

            print(f"[RECV]: From {addr}: {data['action']}")
            dispatch_action(data["action"])

        except Exception as e:
            print(f"[ERROR]: Exception: {e}")

if __name__ == "__main__":
    run_udp_server()