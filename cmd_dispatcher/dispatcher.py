from i2c_controller import send_i2c_command

ACTION_MAP = {
    "ABS_Y+":    (0x20, b"MOTOR_FWD"),
    "ABS_Y-":    (0x20, b"MOTOR_BACK"),
}

def dispatch_action(action: dict):
    try:
        code = action.get("code")
        state = action.get("state")
        
        if code in ACTION_MAP:
            addr, command = ACTION_MAP[code]
            send_i2c_command(addr, command)
        else:
            print(f"[WARN]: Unmapped action: {code}")
    except Exception as e:
        print(f"[ERROR]: Dispatch failed: {e}")