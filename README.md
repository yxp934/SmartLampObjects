# Lab: SmartLamp Objects (Using @dataclass)

## Overview
This project demonstrates how to design Python classes using the @dataclass decorator through a smart lamp example. It is organized into two versions:
- **basic/**: The basic implementation with required features only.
- **stretched/**: The advanced implementation with additional stretch challenge features.

## Directory Structure
```
SmartLampObjects/
├── basic/
│   ├── main.py
│   ├── smart_lamp.py
│   └── README.md (deprecated, see parent README)
├── stretched/
│   ├── main.py
│   ├── smart_lamp.py
│   └── README.md (deprecated, see parent README)
└── README.md  (this file)
```

---

## 1. Basic Version (`basic/`)
### Features
- `SmartLamp` dataclass with fields: `name`, `color`, `brightness`, `is_on`
- Methods: `turn_on()`, `turn_off()`, `set_brightness(percent)`, `set_color(new_color)`, `status()`
- Demonstrates two lamps with different properties and independent state changes

### How to Run
```bash
cd basic
uv run main.py
```

### Sample Output
```
Desk Lamp [ON]: 80% brightness, warm white
Night-Stand [ON]: 30% brightness, red
```

---

## 2. Stretched Version (`stretched/`)
### Additional Features
- All basic features, plus:
  - `toggle()` method to switch the lamp on/off
  - Restricts brightness to 0–100 range
  - `power_outage()` class method to turn all lamps off at once
- Demonstrates advanced features in the script

### How to Run
```bash
cd stretched
uv run main.py
```

### Sample Output
```
Desk Lamp [ON]: 80% brightness, warm white
Night-Stand [ON]: 30% brightness, red
Desk Lamp [OFF]: 80% brightness, warm white
Desk Lamp [OFF]: 80% brightness, warm white
Night-Stand [OFF]: 30% brightness, red
```

---

## Notes
- Both versions require Python 3.7+ and the `dataclasses` module (built-in for 3.7+).
- Install `uv` if not already installed: `pip install uv`
- The README files in `basic/` and `stretched/` are now deprecated; refer to this file for all documentation.
