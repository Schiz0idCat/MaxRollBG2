import pydirectinput as pd
import pyautogui as pg
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def switchWindows() -> None:
    pd.keyDown("alt")
    pd.press("tab")
    pd.keyUp("alt")

def detectNumber(coord: tuple) -> str:
    x, y, height, width = coord
    SS = pg.screenshot(region=(x, y, height, width))

    num = pytesseract.image_to_string(SS, config='--psm 6 digits')
    num = num.strip()

    return num

def populateLevels() -> list:
    minLevel = int(input("Enter the minimum level: "))

    levels = [str(i) for i in range(minLevel, 100)]
    levels.append("00")

    return levels

def deleteUpTo(level: str, levels: list) -> None:
    indice = levels.index(level)
    del levels[:indice + 1]

coordFullScreen = (820, 730, 40, 30)
coordReRoll = (900, 820)
coordRemember = (570, 820)

levels = populateLevels()
switchWindows()

pg.moveTo(coordReRoll[0], coordReRoll[1])
while levels:
    try:
        pg.click()
        number = detectNumber(coordFullScreen)

        if number not in levels: continue

        print(f"New level found: {number}")
        deleteUpTo(number, levels)
        print(f"list of levels: {levels}\n")

        pg.moveTo(coordRemember[0], coordRemember[1])
        pg.click()
        pg.moveTo(coordReRoll[0], coordReRoll[1])

    except KeyboardInterrupt:
        print("The program has been interrupted")
        break