import time
import re
import pyperclip

FULL_DECK_SIZE = 208

def main():
    running_count = 0
    seen_cards = set()
    while len(seen_cards) < FULL_DECK_SIZE:
        clipboard = pyperclip.paste()

        card_emojis = re.findall(r':(([1-9ajqk]0?)[SDHC]):', clipboard)
        for full, value in card_emojis:
            if full in seen_cards:
                continue
            seen_cards.add(full)
            if value in "23456":
                running_count += 1
            elif value in "10JQKA":
                running_count -= 1
            print(f'True Count: {running_count/((FULL_DECK_SIZE-len(seen_cards))/52)}')
        time.sleep(0.25)


if __name__ == '__main__':
    main()
