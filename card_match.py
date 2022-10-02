cards = ["Ace", "King", "Queen"]

user_card_choice = str(input("Choose a card: King. Queen, or Ace\n"))
user_card_choice = user_card_choice.lower()
while user_card_choice == "":
    print("Please enter a choice\n")
    user_card_choice = str(input("Choose a card: King. Queen, or Ace\n"))
    user_card_choice = user_card_choice.lower()

match user_card_choice:
    case "Ace" | "ace":
        user_card_choice = cards[0]
    case "King" | "king":
        user_card_choice = cards[1]
    case "Queen" | "queen":
        user_card_choice = cards[2]
    case _:
        print("Please enter a valid card choice\n")
        quit()

pick_card_number = int(input("Pick a card: 1-3\n"))
match pick_card_number:
    case 1:
        pick_card_number = cards[0]
    case 2:
        pick_card_number = cards[1]
    case 3:
        pick_card_number = cards[2]
    case _:
        print("Please enter a valid number")
        quit()

if user_card_choice == pick_card_number:
    print(f"Good match! Your card was a(n) {user_card_choice} and you picked a(n) {pick_card_number}.")
else:
    print(f"Bad match! Your card was a(n) {user_card_choice} and you picked a(n) {pick_card_number}.")
