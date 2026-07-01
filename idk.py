import random
import time
import pyautogui


def main():
    print("Start. Co minutę wciśnięty zostanie losowo: d lub s.")

    # Opcjonalnie: mały bufor czasu, żeby zdążyć przełączyć się na właściwe okno
    time.sleep(2)

    while True:
        key = random.choice(["d", "s"])
        pyautogui.press(key)  # symuluje naciśnięcie klawisza
        print(f"Wciśnięto: {key}")
        time.sleep(60)  # 60 sekund


if __name__ == "__main__":
    main()
