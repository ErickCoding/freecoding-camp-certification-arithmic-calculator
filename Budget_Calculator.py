class Category:
    def __init__(self, Purchase_category='', Purchase_Description="", Amount_Purchased=0):
        self.Purchase_category = Purchase_category
        self.Purchase_Description = Purchase_Description
        self.Amount_purchased = Amount_Purchased

    def Add_Ledger(self):
        self.Purchase_category.append([self.Purchase_Description, self.Amount_purchased])
Food=[]
Clothes=[]
Utility=[]
Name_Of_Categories=["Food", "Clothes", "Utility"]
Master_List_Categories=[Food, Clothes, Utility]
while True:
    Multiple_choice_opt = 1
    Category_question = "Which Budget Category are we working with today? Enter The Number Corresponding with the Category \n1) New Category \n"
    Transfer_question= ''
    for Key in Name_Of_Categories:
        Multiple_choice_opt = Multiple_choice_opt + 1
        Category_question = Category_question + str(Multiple_choice_opt) + ") " + Key + "\n"
        Transfer_question= Transfer_question + str(Multiple_choice_opt - 1) + ") " + Key + "\n"
    User_inp_Action=int(input("What will you be doing Today? Enter The Number Corresponding with the action. \n1) Spend \n2) Withdraw \n3) Deposit \n4) Transfer\n"))
    if User_inp_Action==4:
        Transfer_from=int(input("What account would you like to transfer from? Enter The Number Corresponding with the action. \n" + Transfer_question))
        Transfer_amount=float(input("Amount you want to transfer.\n"))
        Transfer_positive="${:.2f}".format(Transfer_amount)
        Transfer_negative="${:.2f}".format(Transfer_amount*-1)
        Transfer_to=int(input("What account would you like to transfer to? Enter The Number Corresponding with the action. \n" + Transfer_question + str(Multiple_choice_opt) + ") New Category\n"))
        Transfer_description_to = "Transfer from " + Name_Of_Categories[Transfer_from - 1]
        if Transfer_to==Multiple_choice_opt:
            User_inp_Category = input("Please type the new Category name.\n")
            Name_Of_Categories.append(User_inp_Category)
            User_inp_Category = []
            Master_List_Categories.append(User_inp_Category)
            Transfer_description_from = "Transfer to "+User_inp_Category
        else:
            User_inp_Category=Master_List_Categories[Transfer_to-1]
            Transfer_description_from = "Transfer to " + Name_Of_Categories[Transfer_to-1]
        Transfer_Entry_from = Category(Master_List_Categories[Transfer_from-1], Transfer_description_from, Transfer_negative)
        Transfer_Entry_from.Add_Ledger()
        Transfer_Entry_to= Category(User_inp_Category,Transfer_description_to,Transfer_positive)
        Transfer_Entry_to.Add_Ledger()
        print(Master_List_Categories)
        continue
    User_inp_Category = int(input(Category_question))
    if User_inp_Category != 1:
        User_inp_Category = Master_List_Categories[User_inp_Category - 2]
    if User_inp_Category == 1 and User_inp_Action!=3:
        print("This is a new Category with no budget in it. If you want to make Withdraw or Spend you must first make an initial deposit")
        continue
    if User_inp_Category == 1:
        User_inp_Category = input("Please type the new Category name.\n")
        Name_Of_Categories.append(User_inp_Category)
        User_inp_Category = []
        Master_List_Categories.append(User_inp_Category)
    if User_inp_Action==3:
        User_inp_Desc = "Deposit"
        User_inp_amt = "${:.2f}".format(float(input("Amount of Transaction.\n")))
    elif User_inp_Action==2:
        User_inp_Desc = "Withdraw"
        User_inp_amt = "${:.2f}".format(float(input("Amount of Transaction.\n")) * -1)
    else:#option 1
        User_inp_Desc = input("Description of transaction.\n")
        User_inp_amt = "${:.2f}".format(float(input("Amount of Transaction.\n"))*-1)
    # DT_User_Desc = User_inp_Desc+"bought on "+str(datetime.now())
    def Add_Ledger(self):
        self.Purchase_category.append([self.Purchase_Description, self.Amount_purchased])
    Budget_Entry = Category(User_inp_Category, User_inp_Desc, User_inp_amt)
    Budget_Entry.Add_Ledger()
    print(Name_Of_Categories)
    print(Master_List_Categories)