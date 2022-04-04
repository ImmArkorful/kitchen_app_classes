class KitchenUser():
    firstName = ''
    lastName = ''
    emailAddress = ''
    phoneNumber = ''
    allergies = []
    preferences = []

    def getEmailAddress(self):
        return self.emailAddress

class MealItem():
    name = ''
    description = ''
    serving_size = ''
    allergens = []

    def getMealItemName(self):
        return self.name
    

class Order(KitchenUser, MealItem):
    orderDate = ''
    eitEmail = KitchenUser.getEmailAddress()
    meal = Meal.getMealItemName()
    takeAway = False

class Menu():
    menu_items = []
    special_items = []