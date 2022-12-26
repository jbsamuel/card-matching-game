cards = ["Ace", "King", "Queen"]

user_card_choice = str(input("Choose a card: King. Queen, or Ace\n"))
user_card_choice = user_card_choice.lower()
match user_card_choice:
    case "ace" | "queen" | "king":
        print("it works")
        print(user_card_choice)
    case "Ace" | "ace":
        user_card_choice = cards[0]
    case "King" | "king":
        user_card_choice = cards[1]
    case "Queen" | "queen":
        user_card_choice = cards[2]
    case _:
        print("not working")
        user_card_choice = str(input("Choose a card: King. Queen, or Ace\n"))
        print("Not a valid card choice")
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
        print("Not a valid number choice")
        quit()

if user_card_choice == pick_card_number:
    print(f"Good match! Your card was a(n) {user_card_choice} and you picked a(n) {pick_card_number}.")
else:
    print(f"Bad match! Your card was a(n) {user_card_choice} and you picked a(n) {pick_card_number}.")