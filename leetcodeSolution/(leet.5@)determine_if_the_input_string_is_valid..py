class LoadedIcecream:
    s_vanilla_price = 5
    l_vanilla_price = 10

    def __init__(self):
        self.s_vanilla = 0
        self.l_vanilla = 0

    def input_quantity_of_s_vanilla_loaded(self):
        self.l_vanilla = int(input("enter the no of small cup loaded on vehicle:-"))
        # print('your small cup loaded on vehicle:-', self.s_cup, 'register successfully')

    def input_quantity_of_l_vanilla_loaded(self):
        self.l_vanilla = int(input("enter the no of big cup loaded on vehicle:-"))
        # print('your big cup loaded on vehicle:-', self.b_cup, 'register successfully')

    @property
    def total_amount_of_s_vanilla_icecream_loaded(self):
        return f'Total amount of small cup loaded:-{self.s_vanilla}*{self.s_vanilla_price} = ₹{self.s_vanilla*self.s_vanilla_price}'

    @property
    def total_amount_of_l_vanilla_icecream_loaded(self):
        return f'Total amount of small cup loaded:-{self.l_vanilla}*{self.l_vanilla_price} = ₹{self.l_vanilla*self.l_vanilla_price}'

    @property
    def total_amount_of_all_the_icecream_loaded(self):
        return f'Total amount of all the icecream loaded :-₹{self.s_vanilla*self.s_vanilla_price + self.l_vanilla*self.l_vanilla_price}'


l1 = LoadedIcecream()

l1.input_quantity_of_s_vanilla_loaded()
l1.input_quantity_of_l_vanilla_loaded()
print(l1.total_amount_of_s_vanilla_icecream_loaded)
print(l1.total_amount_of_l_vanilla_icecream_loaded)
print(l1.total_amount_of_all_the_icecream_loaded)

