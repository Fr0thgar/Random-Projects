import time

import pyscreenshot as ImageGrab
import schedule


from datetime import datetime

def take_screenshot():
    print("takeing screenshot...")
    
    image_name = f"screenshot-{str(datetime.now())}"
    screenshot = ImageGrab.grab()
    
    filepath = f"./screenshots{image_name}.png"
    
    screenshot.save(filepath)
    
    print("screenshot taken...")
    
    return filepath

def main():
    schedule.every(5).seconds.do(take_screenshot)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ ==  "__main__":
    main()