import pydirectinput as pd
import pyautogui as pg
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# switch to the last windos
def switchWindows() -> None:
    pd.keyDown("alt")
    pd.press("tab")
    pd.keyUp("alt")

# Detect de number in the image
def detectNumber(coord: tuple) -> str:
    # screenshot
    x, y, height, width = coord
    ss = pg.screenshot(region=(x, y, height, width))

    # detection
    num = pytesseract.image_to_string(ss, config='--psm 6 digits')
    num = num.strip()

    return num

def poblarLevels() -> list:
    minLevel = int(input("Enter the minimum level: "))

    while minLevel < 75 or 100 < minLevel:
        print("Minimun level must be between 75 and 100")
        minLevel = int(input("Enter the minimum level: "))

    levels = [str(i) for i in range(minLevel, 100)]
    levels.append("00")

    return levels

def deleteFrom(value: str, levels: list) -> None:
    index = levels.index(value)
    del levels[:index + 1]


coordFullScreen = (820, 730, 40, 30)
coordReRoll = (900, 810)
coordRemember = (570, 810)

levels = poblarLevels()
switchWindows()

pg.moveTo(coordReRoll[0], coordReRoll[1])
while levels:
    try:
        pg.click()
        number = detectNumber(coordFullScreen)

        if number in levels:
            deleteFrom(number, levels)
            pg.moveTo(coordRemember[0], coordRemember[1])
            pg.click()
            pg.moveTo(coordReRoll[0], coordReRoll[1])

            print(f"A new level has been reached: {number}")
            print(f"The list of levels is: {levels}\n")
    except KeyboardInterrupt:
        print("The program has been interrupted")
        break
