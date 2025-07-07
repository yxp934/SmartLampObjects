from dataclasses import dataclass, field

@dataclass
class SmartLamp:
    name: str
    color: str = "white"
    brightness: int = 100
    is_on: bool = field(default=False, init=False)

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_brightness(self, percent):
        if 0 <= percent <= 100:
            self.brightness = percent
        else:
            print(f"Brightness {percent} is invalid, must be between 0 and 100.")

    def set_color(self, new_color):
        self.color = new_color

    def status(self):
        state = "ON" if self.is_on else "OFF"
        return f"{self.name} [{state}]: {self.brightness}% brightness, {self.color}"

    # Stretch: toggle method
    def toggle(self):
        self.is_on = not self.is_on

    # Stretch: simulate power outage
    _all_lamps = []

    def __post_init__(self):
        SmartLamp._all_lamps.append(self)

    @classmethod
    def power_outage(cls):
        for lamp in cls._all_lamps:
            lamp.turn_off()

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