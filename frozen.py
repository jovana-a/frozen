import tkinter as tk
from tkinter import messagebox

class FrozenYogurtApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Frozen Yogurt Selector")
        
        self.flavors = ["Vanilla", "Chocolate", "Strawberry"]
        self.sauces = ["Chocolate", "Caramel", "Strawberry"]
        self.toppings = ["Fruits", "Nuts", "Candies", "Cookies", "Sprinkles"]
        
        self.selected_flavor = tk.StringVar()
        self.selected_sauce = tk.StringVar()
        self.selected_toppings = []
        
        self.create_widgets()
    
    def create_widgets(self):
        tk.Label(self.root, text="Choose your yogurt flavor:").pack()
        for flavor in self.flavors:
            tk.Radiobutton(self.root, text=flavor, variable=self.selected_flavor, value=flavor).pack()
        
        tk.Label(self.root, text="Choose your sauce:").pack()
        for sauce in self.sauces:
            tk.Radiobutton(self.root, text=sauce, variable=self.selected_sauce, value=sauce).pack()
        
        tk.Label(self.root, text="Choose up to 3 toppings:").pack()
        for topping in self.toppings:
            tk.Checkbutton(self.root, text=topping, command=lambda t=topping: self.select_topping(t)).pack()
        
        tk.Button(self.root, text="Submit", command=self.show_summary).pack()
    
    def select_topping(self, topping):
        if topping in self.selected_toppings:
            self.selected_toppings.remove(topping)
        elif len(self.selected_toppings) < 3:
            self.selected_toppings.append(topping)
        else:
            messagebox.showwarning("Warning", "You can only select up to 3 toppings.")
    
    def show_summary(self):
        summary = f"Flavor: {self.selected_flavor.get()}\nSauce: {self.selected_sauce.get()}\nToppings: {', '.join(self.selected_toppings)}"
        messagebox.showinfo("Your Frozen Yogurt", summary)

if __name__ == "__main__":
    root = tk.Tk()
    app = FrozenYogurtApp(root)
    root.mainloop()