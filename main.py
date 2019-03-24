import keyboard
from utils import CAR


def main():
  foward_pin = 20
  backward_pin = 21
  car = CAR(foward_pin, backward_pin)

  while (True):

    if keyboard.is_pressed('w') or keyboard.is_pressed('up'):
      print("Forward")
      car.forward()
    elif keyboard.is_pressed('s') or keyboard.is_pressed('down'):
      print("Backward")
      car.backward()
    elif keyboard.is_pressed('q'):
      GPIO.cleanup()
      exit(0)
    else:
      print("Idle")


if __name__ == "__main__":
  main()
