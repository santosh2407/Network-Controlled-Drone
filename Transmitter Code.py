import socket,keyboard
serverAddressPort = ("192.168.72.140", 9999)
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
thr = 70
kp = 175
ki = 15
kd = 121
data = "100 100 100 100 175 125 122\n"
prevdata = ""
DATA = ""
type1 = "a"
type2 = "1"
while True:
        roll = 50
        pitch = 50
        yaw = 50
        prevDATA = DATA
        prevdata = data
        key = keyboard.get_hotkey_name()
        if key == "7":
            print("7 is pressed")
            roll = 20
        if key == "9":
            print("9 is pressed")
            roll = 70
        if key == "/":
            print("/ is pressed")
            pitch = 70
        if key == "8":
            print("8 is pressed")
            pitch = 20
        if key == "q":
              if thr < 70:
                thr = thr + 0.001
        if key == "a":
            print("a is pressed")
            if thr > 0:
                thr = thr - 0.001

        if key == "4":
            if kp < 600:
                kp += 0.001
        if key == "1":
            if kp > 0:
                kp -= 0.001

        if key == "5":
            if ki < 600:
                ki += 0.001
        if key == "2":
            if ki > 0:
                ki -= 0.001

        if key == "6":
            if kd < 600:
                kd += 0.001
        if key == "3":
            if kd > 0:
                kd -= 0.001

        if key == "enter":
            kp = 175
            ki = 15
            kd = 121
        data = str(roll) + str(pitch) + str(round(thr)) + str(yaw)
        datachar = chr(roll) + chr(pitch) + chr(int(round(thr))) + chr(yaw)
        if data != prevdata:
                UDPClientSocket.sendto(datachar.encode(),serverAddressPort)
                print("trans: ", data)
                print("trans_c: ", datachar)

        recvdata = UDPClientSocket.recv(10)
        print("recv: ", recvdata)
