# cards = None
# cards_ace = ["Ace"]
# cards_queen = ["Queen"]
# cards_king =["King"]
user_card_choice = str(input("Choose a card: King. Queen, or Ace\n"))
user_card_choice = user_card_choice.lower()
match user_card_choice:
    case "ace" | "queen" | "king":
        print("it works")
        print(user_card_choice)
    case _:
        print("not working")
        user_card_choice = str(input("Choose a card: King. Queen, or Ace\n"))
