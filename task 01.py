from time import sleep

class Trafficlight:
    __color = "Чёрный"

    def running(self):
        while True:
            print("Светоров красный")
            sleep(7)
            print("Светофор жёлтый")
            sleep(2)
            print("Светофор зелёный")
            sleep(7)
            print("Светофор жёлтый")
            sleep(2)

trafficlight = Trafficlight()
trafficlight.running()
