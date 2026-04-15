import random

MOODS = {
    "happy": {
        "emoji": "😄",
        "quotes": [
            "Keep smiling — your vibe is contagious! ✨",
            "Happiness looks good on you. Ride this wave! 🌊",
            "You're on fire today. Don't let anyone dim your light. 🔥",
            "Good vibes only — and you're the source. 🌟",
            "Today is a great day to have a great day. 🌈",
        ],
    },
    "neutral": {
        "emoji": "😐",
        "quotes": [
            "Not every day has to be amazing. Steady is underrated. 🌿",
            "A calm sea makes a skilled sailor. You're learning. ⚓",
            "Even a gray sky has its own quiet beauty. 🌫️",
            "Neutral is just energy waiting to find its direction. 🧭",
            "Sometimes 'meh' is just your brain taking a breather. 🧠",
        ],
    },
    "sad": {
        "emoji": "😢",
        "quotes": [
            "It's okay not to be okay. You won't feel this way forever. 💙",
            "Even the darkest night will end, and the sun will rise. 🌅",
            "You are allowed to be both a masterpiece and a work in progress. 🎨",
            "Crying is just your soul taking a shower. You'll feel cleaner soon. 🌧️",
            "Every storm runs out of rain. Hang in there. ☂️",
        ],
    },
}


def print_banner():
    print("\n" + "=" * 40)
    print("       ✨  VIBE CONSOLE APP  ✨")
    print("=" * 40 + "\n")


def ask_mood():
    print("How are you feeling right now?\n")
    print("  1. 😄  Happy")
    print("  2. 😐  Neutral")
    print("  3. 😢  Sad")
    print()

    while True:
        choice = input("Enter 1, 2, or 3: ").strip()
        if choice == "1":
            return "happy"
        elif choice == "2":
            return "neutral"
        elif choice == "3":
            return "sad"
        else:
            print("Hmm, that doesn't match. Please enter 1, 2, or 3.")


def deliver_vibe(mood):
    data = MOODS[mood]
    quote = random.choice(data["quotes"])
    emoji = data["emoji"]

    print("\n" + "-" * 40)
    print(f"  Mood detected: {emoji}  ({mood.capitalize()})")
    print("-" * 40)
    print(f'\n  "{quote}"\n')
    print("-" * 40 + "\n")


def main():
    print_banner()
    mood = ask_mood()
    deliver_vibe(mood)

    while True:
        again = input("Want to check your vibe again? (y/n): ").strip().lower()
        if again == "y":
            print()
            mood = ask_mood()
            deliver_vibe(mood)
        elif again == "n":
            print("\nStay true to your vibe. See you next time! 👋\n")
            break
        else:
            print("Just type 'y' or 'n'.")


if __name__ == "__main__":
    main()
