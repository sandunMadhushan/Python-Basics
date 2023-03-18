#Qusetion 01

name = "A.M.S.H. Madhushan"
birth_year = 2000
height = 5.5
s_number = "s22010304"
likes_to_exercise = False

print("Hello All! I am " + name + " and I was born in " + str(birth_year))
print("\nMy height is " + str(height) + " feet")
print("\nStudent number: " + s_number)
print("\nLike to exercise: " + str(likes_to_exercise))

print("\n")

#Qusetion 02

def multiply(x,y):
    return x*y
    
def divide(x,y):
    if x<y:
        x,y = y,x
    return x/y

num1 = float(input("Enter number one: "))
num2 = float(input("Enter number two: "))

product = multiply(num1, num2)
quotient = divide(num1, num2)

print("\nMultiplication: ", product)
print("Division: ", quotient)

print("\n")

#Question 03

#s22010304
#last digit: 4

Objects = ["Fish","Bicycle","Guitar","Microwave Oven","Debit Card"]
print(Objects[4])

print("\n")

class DebitCard:
    def __init__(self, card_number, expiration_date, cardholder_name, cvv_code):
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.cardholder_name = cardholder_name
        self.cvv_code = cvv_code
    
    def make_purchase(self, amount):
        print(f"Making a purchase of {amount} dollars with card ending in {self.card_number[-4:]}")
    
my_card = DebitCard("1122 3344 5566 7788", "03/24", "Sandun Madhushan", "666")
    
my_card.make_purchase(50)