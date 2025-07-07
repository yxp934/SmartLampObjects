from smart_lamp import SmartLamp

if __name__ == "__main__":
    lamp1 = SmartLamp(name="Desk Lamp", color="warm white", brightness=80)
    lamp2 = SmartLamp(name="Night-Stand", color="red", brightness=30)

    lamp1.turn_on()
    lamp2.turn_on()

    print(lamp1.status())
    print(lamp2.status())

    # Stretch: test toggle and power outage
    lamp1.toggle()
    print(lamp1.status())
    SmartLamp.power_outage()
    print(lamp1.status())
    print(lamp2.status()) 