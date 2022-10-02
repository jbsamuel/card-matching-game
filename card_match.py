# cards_ace = ["Ace"]
# cards_queen = ["Queen"]
# cards_king =["King"]
cards = [["Ace"], ["King"], ["Queen"]]
user_card_choice = str(input("Choose a card: King. Queen, or Ace\n"))
user_card_choice = user_card_choice.lower()
pick_card_number = int(input("Pick a card: 0-2\n"))
match pick_card_number:
    case 0 | 1 | 2:
        print("it works")
        print(pick_card_number)
    case _:
        print("not working")
