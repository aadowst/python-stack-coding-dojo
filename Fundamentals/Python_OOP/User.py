class User:
    user_list = []
    def __init__ (self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        # attributes below are default 
        self.is_rewards_member = False
        self.gold_card_points = 0
        User.user_list.append(self)
    
    def display_info (self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        # Is there a way to print all of the attributes??
    
    def enroll(self):
        if self.is_rewards_member == True:
            print("You are already enrolled")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
    
    def spend_points(self, amount):
        if self.gold_card_points > amount:
            self.gold_card_points -= amount
            return True
        else:
            print("User already a member")
            return False

Adrian = User("Adrian", "Awesome", "a@a.com", 40)
Adrian.enroll()
Adrian.spend_points(300)
Adrian.display_info()

Brian = User("Brian", "Bossy", "b@b.com", 30)
Brian.display_info()
Brian.enroll()


