
import time

userData = {} #creating an open dict to store user input

#Dictionary of pizza names and different combinations of Bread, Meat, toppings, and Sauce Combinations and Costs
pizzas = {"314": ["Big Red",14], #Thick Crusts
          "312": ["Bacon Boom",15],
          "311": ["Pepperoni Explosion",15],
          "313": ["Red Ham",15],
          "324": ["Big Green",13],
          "322": ["Greeny Bacon Delight",14],
          "321": ["Thick Pepperoni Pesteroni",14],
          "323": ["Ham and Pesto Explosion",14],
          "214": ["Classic",14], #Medium Crusts
          "212": ["Canadian",14],
          "211": ["Toni Pepperoni",14],
          "213": ["Americana",14],
          "224": ["Pesto Franki",12],
          "222": ["Summer Sun",12],
          "221": ["The Grandmother",12],
          "223": ["Soprano",12],
          "114": ["Fratello",13], #Thin Crusts
          "112": ["Mama's Pizza",14],
          "111": ["Capone",14],
          "113": ["Salumi",14],
          "124": ["Piccola Pesto",12],
          "122": ["Brando",12],
          "121": ["Capri",12],
          "123": ["Primavera",12],
          }

toppings = {"Olives":1.00,
            "Broccoli":1.25,
            "Zucchini":1.00,
            "Tobasco Sauce":1.10,
            "Pineapple": 0.70,
            "BBQ Sauce": 1.10,
            "No": 0
            }

# The main function that drives the system
def TakeOrder():
  print("********* Welcome To Sydney's Pizza *********")
  userName = input("Greetings!! \nWhat is your name?_")
  userData.update({"Name":userName}) #updating the user data dict with the input
  userPNum = input("What is your phone number?_")
  userData.update({"Phone":userPNum})
  userAdrs = input("What is your address._")
  userData.update({"address":userAdrs})
  # using a try except to avoid user errors
  try:
    # Choosing bread for pizza
    bread = int(input("What dough do you want? Type 1 for thin, 2 for regular, and 3 for thick\n"))
    userData.update({"bread":bread})#updating the user data dict with the input

    #Choosing sauce for pizza
    sauce = int(input("What sauce do you want? Type 1 for marinara, and 2 for pesto.\n"))
    userData.update({"sauce":sauce})

    # Choosing meat for pizza
    meat = int(input("Choose your meat: Type 1 for pepperoni, type 2 for bacon, type 3 for ham, type 4 for none.\n"))
    userData.update({"meat":meat})

    # Choosing vegetables for pizza 
    vegetables = int(input("What vegetables do you want? Type 1 for mushroom, type 2 for pepper, type 3 for tomato, type 4 for none.\n"))
    userData.update({"veg":vegetables})

    # choosing extra toppings
    print("Alright. There are also a selection of toppings you can choose from. We have:")
    n = 1
    for x,y in toppings.items():
      print("Type "+str(n)+f" for {x}: ${str(y)}")
      n = n + 1
    print("Type 7 to have none.")
    toppingChoice = int(input(""))
    userData.update({"toppings":toppingChoice})

  except:
    print("Input Error, please try again!")
    TakeOrder()
  
  proceed = input("Do you want us to create your order now? y/n_ ")
  if proceed == "y":
    createOrder() # Calling the create order function
  else:
    TakeOrder()


def createOrder():
  finalPizza = str(userData.get("bread")) + str(userData.get("sauce")) + str(userData.get("meat"))
  #updating the user data dict with values
  if userData.get("veg") == 1:
      userData.update({"veg":"mushroom"})
  if userData.get("veg") == 2:
    userData.update({"veg":"pepper"})
  if userData.get("veg") == 3:
    userData.update({"veg":"tomato"})
  if userData.get("veg") == 4:
    userData.update({"veg":"No"})

  if userData.get("toppings") == 1:
    userData.update({"toppings":"Olives"})
  if userData.get("toppings") == 2:
    userData.update({"toppings":"Broccoli"})
  if userData.get("toppings") == 3:
    userData.update({"toppings":"Zucchini"})
  if userData.get("toppings") == 4:
    userData.update({"toppings":"Tobasco Sauce"})
  if userData.get("toppings") == 5:
    userData.update({"toppings":"Pineapple"})
  if userData.get("toppings") == 6:
    userData.update({"toppings":"BBQ Sauce"})
  if userData.get("toppings") == 7:
    userData.update({"toppings":"None"})

#Giving the user a chance to revisit her/his order
  print("Hey,",userData.get("Name"),"!","\nPlease check your order details again!")
  for i in pizzas.keys():
    if i == finalPizza: 
      print("You've ordered for :\n" , pizzas[i][0] ,"pizza with", userData["veg"],"as veggies and",userData["toppings"], "as toppings .")
  proceed = input("Do you want us to proceed y/n ? _ ")
  if proceed == "y":
    time.sleep(1)
    print("Creating your order\t.")
    time.sleep(1)
    checkOut(finalPizza)
  else:
    TakeOrder()

#Printing the final order and check-out
def checkOut(code):
  print("\n\n******* Your Order Summary *******")
  print("_______________________________________________")
# Calculating cost and taxed cost
  totalCost = toppings[userData['toppings']] + pizzas[code][1]
  tax = totalCost % 12
# Printing the Summary
  print("Pizza ->",pizzas[code][0],"$",pizzas[code][1])
  print("Toppings ->",userData['toppings'],"$",toppings[userData['toppings']])
  print("Veggies ->",userData['veg'],"-> 0$")
  print("Sub Total :$", totalCost)
  print("_______________________________________________")
  print("With a 12% service charge\n\tYou'll be paying $",totalCost+tax)
  print("_______________________________________________")
  #print("Grand Total with 12% Taxes :$",totalCost+tax)
  print("You order will be delivered shortly at :\n",userData["address"])
  print("Thanks for visiting Keon's Pizza today!\nPlease visit us again...\nHave a great day ahead!")
  proceed = input("Do you want to order another pizza y/n ? _ ")
  if proceed == "y":
    TakeOrder()
  else:
    print("Bye Bye!")




#Driver Code
TakeOrder()

