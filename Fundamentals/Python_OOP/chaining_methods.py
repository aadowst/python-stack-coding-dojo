

class User:
    def __init__ (self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        # attributes below are default 
        self.is_rewards_member = False
        self.gold_card_points = 0

    
    def display_info (self):
        import pprint
        pprint.pprint(vars(self))
        return self

    
    def enroll(self):
        if self.is_rewards_member == True:
            print("You are already enrolled")
            return self
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return self
    
    def spend_points(self, amount):
        if self.gold_card_points > amount:
            self.gold_card_points -= amount
            return self
        else:
            print("User already a member")
            return self

# Adrian = User("Adrian", "Awesome", "a@a.com", 40)
# Adrian.enroll()
# Adrian.spend_points(300)
# Adrian.display_info()

Brian = User("Brian", "Bossy", "b@b.com", 30)
Brian.display_info().enroll().enroll()
