from model.user import User

class HighEloManager():
    def high_enough_elo(self, user: User):
        print("\nChecking if elo greater than 1500...")
        user_elo = user.get_userelo()
        if user_elo >= 1500:
            print("User elo = " + str(user_elo))
            print("Confirmed.")
            return True
        return False