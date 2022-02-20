from tkinter import *
import time
import datetime
import random
import tkinter.messagebox

#================================ Main Frame ===============================
root = Tk()
root.geometry("800x690+0+0")
root.maxsize(width=800, height=690)
root.title("Pizza-Burger Management System")
root.configure(background='black')

#=============================== Base Frames ===============================
Base1 = Frame(root, width=500, height=690, bg="green")
Base1.grid_propagate(0)
Base1.pack(side=LEFT)

Base2 = Frame(root, width=300, height=690, bg="red")
Base2.grid_propagate(0)
Base2.pack(side=RIGHT)

#============================ Left Frame / Base1 ===========================
Title = Frame(Base1, width=500, height=100, bd=8, bg="gold")
Title.grid_propagate(0)
Title.pack(side=TOP)

Appmenu = Frame(Base1, width=500,height=590, bd=8, bg="gold")
Appmenu.grid_propagate(0)
Appmenu.pack(side=BOTTOM)

#============================ Right Frame / Base2 ==========================
Subbase1 = Frame(Base2, width=300, height=200, bd=8, bg="orange")
Subbase1.pack(side=TOP)

Appinfo = Frame(Subbase1, width=300, height=200, bd=8)
Appinfo.grid_propagate(0)
Appinfo.pack(side=TOP)

Subbase2 = Frame(Base2, width=300,height=490, bd=8, bg="orange")
Subbase2.pack(side=BOTTOM)

Appreceipt = Frame(Subbase2, width=300, height=340, bd=8, bg="beige")
Appreceipt.grid_propagate(0)
Appreceipt.pack(side=TOP)

Appbuttons = Frame(Subbase2, width=300,height=150, bd=1, bg="grey")
Appbuttons.grid_propagate(0)
Appbuttons.pack(side=RIGHT)

#=================================== Time ==================================
localtime=time.asctime(time.localtime(time.time()))

#=============================== Title and time ============================
lbl_info = Label(Title, font=('arial', 30, 'bold'), text="Pizza-Burger", bd=10, bg="gold")
lbl_info.grid(row=0, column=0)

lbl_date_time=Label(Title, font=('arial', 8, 'bold'), text=localtime, fg="Steel Blue", bd=10, bg="gold", anchor="n")
lbl_date_time.grid(row=1, column=0)

#================================== Menu info ==============================
lbl_menu_0 = Label(Appmenu, font=('arial', 10, 'bold'), text="Price", bd=10, bg="gold", justify=CENTER)
lbl_menu_0.grid(row=0, column=2)


#================================== Functions ==============================
#===========================================================================
def exit():
    exit = tkinter.messagebox.askyesno("Quit System", "Do you want to exit?")
    if exit > 0:
        root.destroy()
        return


def empty_field():
    alert = tkinter.messagebox.showwarning("Alert", "The entry field is empty!")
    return alert


def reset():
    paid_tax.set(""), sub_total.set(""), total_cost.set(""), foods_price.set(""),
    drinks_price.set(""), service_charge.set(""), txt_receipt.delete("1.0", END)

    e_margherita.set("0"), e_cheesepizza.set("0"), e_pepperoni.set("0"),
    e_veggie.set("0"), e_hamburger.set("0"), e_cheeseburger.set("0"),
    e_chickenburger.set("0"), e_veganburger.set("0"), e_lemonade.set("0"),
    e_juice.set("0"), e_soda.set("0"), e_coffee.set("0"), e_tea.set("0")

    var1.set(0), var2.set(0), var3.set(0), var4.set(0), var5.set(0)
    var6.set(0), var7.set(0), var8.set(0), var9.set(0), var10.set(0),
    var11.set(0), var12.set(0), var13.set(0)

    entry_margherita.configure(state="disabled")
    entry_cheesepizza.configure(state="disabled")
    entry_pepperoni.configure(state="disabled")
    entry_veggie.configure(state="disabled")
    entry_hamburger.configure(state="disabled")
    entry_cheeseburger.configure(state="disabled")
    entry_chickenburger.configure(state="disabled")
    entry_veganburger.configure(state="disabled")
    entry_lemonade.configure(state="disabled")
    entry_juice.configure(state="disabled")
    entry_soda.configure(state="disabled")
    entry_coffee.configure(state="disabled")
    entry_tea.configure(state="disabled")


#============================== Check Function ============================
def chk_button():
    if var1.get() == 1:
        entry_margherita.configure(state="normal")
    elif var1.get() == 0:
        entry_margherita.configure(state="disabled")
        e_margherita.set("0")

    if var2.get() == 1:
        entry_cheesepizza.configure(state="normal")
    elif var2.get() == 0:
        entry_cheesepizza.configure(state="disabled")
        e_cheesepizza.set("0")

    if var3.get() == 1:
        entry_pepperoni.configure(state="normal")
    elif var3.get() == 0:
        entry_pepperoni.configure(state="disabled")
        e_pepperoni.set("0")

    if var4.get() == 1:
        entry_veggie.configure(state="normal")
    elif var4.get() == 0:
        entry_veggie.configure(state="disabled")
        e_veggie.set("0")

    if var5.get() == 1:
        entry_hamburger.configure(state="normal")
    elif var5.get() == 0:
        entry_hamburger.configure(state="disabled")
        e_hamburger.set("0")
    
    if var6.get() == 1:
        entry_cheeseburger.configure(state="normal")
    elif var6.get() == 0:
        entry_cheeseburger.configure(state="disabled")
        e_cheeseburger.set("0")

    if var7.get() == 1:
        entry_chickenburger.configure(state="normal")
    elif var7.get() == 0:
        entry_chickenburger.configure(state="disabled")
        e_chickenburger.set("0")

    if var8.get() == 1:
        entry_veganburger.configure(state="normal")
    elif var8.get() == 0:
        entry_veganburger.configure(state="disabled")
        e_veganburger.set("0")

    if var9.get() == 1:
        entry_lemonade.configure(state="normal")
    elif var9.get() == 0:
        entry_lemonade.configure(state="disabled")
        e_lemonade.set("0")

    if var10.get() == 1:
        entry_juice.configure(state="normal")
    elif var10.get() == 0:
        entry_juice.configure(state="disabled")
        e_juice.set("0")

    if var11.get() == 1:
        entry_soda.configure(state="normal")
    elif var11.get() == 0:
        entry_soda.configure(state="disabled")
        e_soda.set("0")

    if var12.get() == 1:
        entry_coffee.configure(state="normal")
    elif var12.get() == 0:
        entry_coffee.configure(state="disabled")
        e_coffee.set("0")

    if var13.get() == 1:
        entry_tea.configure(state="normal")
    elif var13.get() == 0:
        entry_tea.configure(state="disabled")
        e_tea.set("0")


def cost_of_item():
    item1 = float(e_margherita.get())
    item2 = float(e_cheesepizza.get())
    item3 = float(e_pepperoni.get())
    item4 = float(e_veggie.get())
    item5 = float(e_hamburger.get())
    item6 = float(e_cheeseburger.get())
    item7 = float(e_chickenburger.get())
    item8 = float(e_veganburger.get())
    item9 = float(e_lemonade.get())
    item10 = float(e_juice.get())
    item11 = float(e_soda.get())
    item12 = float(e_coffee.get())
    item13 = float(e_tea.get())

    price_of_foods = (item1*13.34) + (item2*14.99) + (item3*11.54) + (item4*15.35) + (item5*2.46) + (item6*3.46) + (item7*3.99) + (item8*2.85)
    price_of_beverages = (item9*1.25) + (item10*2.54) + (item11*0.99) + (item12*2.70) + (item13*1.70)

    result_foods_price = "$" + str('%.2f'%(price_of_foods))
    result_beverages_price = "$" + str('%.2f' % (price_of_beverages))

    foods_price.set(result_foods_price)
    drinks_price.set(result_beverages_price)

    #=== Service Charge ===
    sc_percentage = (price_of_foods + price_of_beverages)*.10
    sc = "$" + str('%.2f'%(sc_percentage))
    service_charge.set(sc)

    #=== Taxes ===
    tax = "$" + str('%.2f' % ((price_of_beverages + price_of_foods + sc_percentage) * 0.15))
    paid_tax.set(tax)

    tt = ((price_of_beverages + price_of_foods + sc_percentage) * 0.15)
    
    #=== Sub Total ===
    sub_total1 = "$" + str('%.2f' % (price_of_beverages + price_of_foods + sc_percentage))
    sub_total.set(sub_total1)
    
    #=== Total ===
    tc = "$" + str('%.2f' % (price_of_beverages + price_of_foods + sc_percentage + tt))
    total_cost.set(tc)


def receipt():
    txt_receipt.delete("1.0", END)
    date_time = datetime.datetime.now()
    x = random.randint(100898, 6812789)
    random_ref = str(x)
    txt_receipt.insert(END, 'Bill ' + random_ref + "\t\t" + str(date_time) + "\n\n")
    txt_receipt.insert(END, 'Margherita\t\t' + "$13.34 x " + str(e_margherita.get()) + "\t\t" + " $" + str((e_margherita.get())* 13.34) + "\n")
    txt_receipt.insert(END, 'Cheesepizza\t\t' +  "$14.99 x " + str(e_cheesepizza.get()) + "\t\t" + " $" +str((e_cheesepizza.get())* 14.99) + "\n")
    txt_receipt.insert(END, 'Pepperoni\t\t' + "$11.54 x " + str(e_pepperoni.get()) + "\t\t" + " $" +str((e_pepperoni.get())* 11.54) + "\n")
    txt_receipt.insert(END, 'Veggie\t\t' + "$15.35 x " + str(e_veggie.get()) + "\t\t" + " $" +str((e_veggie.get())* 15.35) + "\n")
    txt_receipt.insert(END, 'Hamburger\t\t' + "$  2.46 x " + str(e_hamburger.get()) + "\t\t" + " $" +str((e_hamburger.get())* 2.46) + "\n")
    txt_receipt.insert(END, 'Cheeseburger\t\t' + "$  3.46 x " + str(e_cheeseburger.get()) + "\t\t" + " $" +str((e_cheeseburger.get())* 3.46) + "\n")
    txt_receipt.insert(END, 'Chickenburger\t\t' + "$  3.99 x " + str(e_chickenburger.get()) + "\t\t" +" $" + str((e_chickenburger.get())* 3.99) + "\n")
    txt_receipt.insert(END, 'Veganburger\t\t' + "$  2.85 x " + str(e_veganburger.get()) + "\t\t" + " $" +str((e_veganburger.get())* 2.85) + "\n")
    txt_receipt.insert(END, 'Lemonade\t\t' + "$  1.25 x " + str(e_lemonade.get()) + "\t\t" + " $" +str((e_lemonade.get())* 1.25) + "\n")
    txt_receipt.insert(END, 'Juice\t\t' + "$  2.54 x " + str(e_juice.get()) + "\t\t" + " $" +str((e_juice.get())* 2.54) + "\n")
    txt_receipt.insert(END, 'Soda\t\t' + "$  0.99 x " + str(e_soda.get()) + "\t\t" + " $" +str((e_soda.get())* 0.99) + "\n")
    txt_receipt.insert(END, 'Coffee\t\t' + "$  2.70 x " + str(e_coffee.get()) + "\t\t" + " $" +str((e_coffee.get())* 2.70) + "\n")
    txt_receipt.insert(END, 'Tea\t\t' + "$  1.70 x " + str(e_tea.get()) + "\t\t" + " $" +str((e_tea.get())* 1.70) + "\n\n")
    txt_receipt.insert(END, 'Cost of foods \t\t\t\t ' + str(foods_price.get()) + "\n")
    txt_receipt.insert(END, 'Cost of beverages \t\t\t\t ' + str(drinks_price.get()) + "\n")
    txt_receipt.insert(END, 'Tax paid \t\t\t\t ' + paid_tax.get() + "\n")
    txt_receipt.insert(END, 'Service charge \t\t\t\t ' + service_charge.get() + "\n\n")
    txt_receipt.insert(END, 'Total cost: \t\t\t\t ' + total_cost.get() + "\n")


def total():
    try:
        cost_of_item()
    except:
        empty_field()


#=============================== Variables ================================
#==========================================================================
#=== Food ===
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()

#=== Drinks ===
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()

#=== Others ===
paid_tax = StringVar()
sub_total = StringVar()
total_cost = StringVar()
foods_price = StringVar()
drinks_price = StringVar()
service_charge = StringVar()


#===============================Products Entry Field==================================
#=== Pizzas ===
e_margherita = IntVar()
e_cheesepizza = IntVar()
e_pepperoni = IntVar()
e_veggie = IntVar()

#=== Hamburgers ===
e_hamburger = IntVar()
e_cheeseburger = IntVar()
e_chickenburger = IntVar()
e_veganburger = IntVar()

#=== Drinks ===
e_lemonade = IntVar()
e_juice = IntVar()
e_soda = IntVar()
e_coffee = IntVar()
e_tea = IntVar()

#===================================== Menu Products ======================================
#================================= App Menu / Check Button ================================
margherita = Checkbutton(Appmenu, text="Margherita Pizza \t", variable=var1, onvalue=1, offvalue=0, font=('arial', 14, 'bold'), command=chk_button, bg='gold').grid(row=1, sticky=W)
cheesepizza = Checkbutton(Appmenu, text="Cheese Pizza \t", variable=var2, onvalue=1, offvalue=0, font=('arial', 14, 'bold'), command=chk_button, bg='gold').grid(row=2, sticky=W)
pepperoni = Checkbutton(Appmenu, text="Pepperoni Pizza \t", variable=var3, onvalue=1, offvalue=0, font=('arial', 14, 'bold'), command=chk_button, bg='gold').grid(row=3, sticky=W)
veggie = Checkbutton(Appmenu, text="Veggie Pizza \t", variable=var4, onvalue=1, offvalue=0, font=('arial', 14, 'bold'), command=chk_button, bg='gold').grid(row=4, sticky=W)

hamburger = Checkbutton(Appmenu, text="Hamburger \t", variable=var5, onvalue=1, offvalue=0, font=('arial', 14, 'bold'), command=chk_button, bg='gold').grid(row=5, sticky=W)
cheeseburger = Checkbutton(Appmenu, text="Cheeseburger \t", variable=var6, onvalue=1, offvalue=0, font=('arial', 14, 'bold'), command=chk_button, bg='gold').grid(row=6, sticky=W)
chickenburger = Checkbutton(Appmenu, text="Chicken Burger \t", variable=var7, onvalue=1, offvalue=0, font=('arial', 14, 'bold'), command=chk_button, bg='gold').grid(row=7, sticky=W)
veganburger = Checkbutton(Appmenu, text="Vegan Burger \t", variable=var8, onvalue=1, offvalue=0, font=('arial', 14, 'bold'), command=chk_button, bg='gold').grid(row=8, sticky=W)

lemonade = Checkbutton(Appmenu, text="Lemonade \t", variable=var9, onvalue=1, offvalue=0, font=('arial', 14, 'bold'), command=chk_button, bg='gold').grid(row=9, sticky=W)
juice = Checkbutton(Appmenu, text="Juice \t", variable=var10, onvalue=1, offvalue=0, font=('arial', 14, 'bold'), command=chk_button, bg='gold').grid(row=10, sticky=W)
soda = Checkbutton(Appmenu, text="Soda \t", variable=var11, onvalue=1, offvalue=0, font=('arial', 14, 'bold'), command=chk_button, bg='gold').grid(row=11, sticky=W)
coffee = Checkbutton(Appmenu, text="Coffee \t", variable=var12, onvalue=1, offvalue=0, font=('arial', 14, 'bold'), command=chk_button, bg='gold').grid(row=12, sticky=W)
tea = Checkbutton(Appmenu, text="Tea \t", variable=var13, onvalue=1, offvalue=0, font=('arial', 14, 'bold'), command=chk_button, bg='gold').grid(row=13, sticky=W)

#==================================== App Menu / Entry field ==============================
entry_margherita = Entry(Appmenu, font=('arial', 12, 'bold'), bd=6, width=15, textvariable=e_margherita, justify='center', state='disabled')
entry_margherita.grid(row=1, column=1)
entry_cheesepizza = Entry(Appmenu, font=('arial', 12, 'bold'), bd=6, width=15, textvariable=e_cheesepizza, justify='center', state='disabled')
entry_cheesepizza.grid(row=2, column=1)
entry_pepperoni = Entry(Appmenu, font=('arial', 12, 'bold'), bd=6, width=15, textvariable=e_pepperoni, justify='center', state='disabled')
entry_pepperoni.grid(row=3, column=1)
entry_veggie = Entry(Appmenu, font=('arial', 12, 'bold'), bd=6, width=15, textvariable=e_veggie, justify='center', state='disabled')
entry_veggie.grid(row=4, column=1)

entry_hamburger = Entry(Appmenu, font=('arial', 12, 'bold'), bd=6, width=15, textvariable=e_hamburger, justify='center', state='disabled')
entry_hamburger.grid(row=5, column=1)
entry_cheeseburger = Entry(Appmenu, font=('arial', 12, 'bold'), bd=6, width=15, textvariable=e_cheeseburger, justify='center', state='disabled')
entry_cheeseburger.grid(row=6, column=1)
entry_chickenburger = Entry(Appmenu, font=('arial', 12, 'bold'), bd=6, width=15, textvariable=e_chickenburger, justify='center', state='disabled')
entry_chickenburger.grid(row=7, column=1)
entry_veganburger = Entry(Appmenu, font=('arial', 12, 'bold'), bd=6, width=15, textvariable=e_veganburger, justify='center', state='disabled')
entry_veganburger.grid(row=8, column=1)

entry_lemonade = Entry(Appmenu, font=('arial', 12, 'bold'), bd=6, width=15, textvariable=e_lemonade, justify='center', state='disabled')
entry_lemonade.grid(row=9, column=1)
entry_juice = Entry(Appmenu, font=('arial', 12, 'bold'), bd=6, width=15, textvariable=e_juice, justify='center', state='disabled')
entry_juice.grid(row=10, column=1)
entry_soda = Entry(Appmenu, font=('arial', 12, 'bold'), bd=6, width=15, textvariable=e_soda, justify='center', state='disabled')
entry_soda.grid(row=11, column=1)
entry_coffee = Entry(Appmenu, font=('arial', 12, 'bold'), bd=6, width=15, textvariable=e_coffee, justify='center', state='disabled')
entry_coffee.grid(row=12, column=1)
entry_tea = Entry(Appmenu, font=('arial', 12, 'bold'), bd=6, width=15, textvariable=e_tea, justify='center', state='disabled')
entry_tea.grid(row=13, column=1)

#===================================== App Menu / Price ===================================
lbl_margherita = Label(Appmenu, font=('arial', 12, 'bold'), width=13, bd=6, text="$13.34", bg="gold").grid(row=1, column=2)
lbl_cheesepizza = Label(Appmenu, font=('arial', 12, 'bold'), bd=6, text="$14.99", bg="gold").grid(row=2, column=2)
lbl_pepperoni = Label(Appmenu, font=('arial', 12, 'bold'), bd=6, text="$11.54", bg="gold").grid(row=3, column=2)
lbl_veggie = Label(Appmenu, font=('arial', 12, 'bold'), bd=6, text="$15.35", bg="gold").grid(row=4, column=2)

lbl_hamburger = Label(Appmenu, font=('arial', 12, 'bold'), bd=6, text="$  2.46", bg="gold").grid(row=5, column=2)
lbl_cheeseburger = Label(Appmenu, font=('arial', 12, 'bold'), bd=6, text="$  3.46", bg="gold").grid(row=6, column=2)
lbl_chickenburger = Label(Appmenu, font=('arial', 12, 'bold'), bd=6, text="$  3.99", bg="gold").grid(row=7, column=2)
lbl_veganburger = Label(Appmenu, font=('arial', 12, 'bold'), bd=6, text="$  2.85", bg="gold").grid(row=8, column=2)

lbl_lemonade = Label(Appmenu, font=('arial', 12, 'bold'), bd=6, text="$  1.25", bg="gold").grid(row=9, column=2)
lbl_juice = Label(Appmenu, font=('arial', 12, 'bold'), bd=6, text="$  2.54", bg="gold").grid(row=10, column=2)
lbl_soda = Label(Appmenu, font=('arial', 12, 'bold'), bd=6, text="$  0.99", bg="gold").grid(row=11, column=2)
lbl_coffee = Label(Appmenu, font=('arial', 12, 'bold'), bd=6, text="$  2.70", bg="gold").grid(row=12, column=2)
lbl_tea = Label(Appmenu, font=('arial', 12, 'bold'), bd=6, text="$  1.70", bg="gold").grid(row=13, column=2)

#=============================== App Menu / Info and credits ==============================
lbl_empty = Label(Appmenu, bd=6, text="\t\t", bg="gold").grid(row=14, column=1)
lbl_empty = Label(Appmenu, font=('arial', 6, 'bold'), bd=6, text="\tThis is only a test program\n   Don't use this program for real purposes!", bg="gold", justify=LEFT).grid(row=15, column=1)

lbl_info_credit = Label(Appmenu, font=('arial', 8, 'bold'), bd=6, text="By Mijail Naal", bg="gold", justify=CENTER).grid(row=16, column=1)

#===================================== App Receipt Frame ==================================
txt_receipt = Text(Appreceipt, font=('arial', 8, 'bold'), bd=8, width=42, height=22)
txt_receipt.grid(row=1, column=0)

#====================================== App Information ===================================
lblfoods_price = Label(Appinfo, font=('arial', 6, 'bold'), text="Cost of foods: \t", bd=8)
lblfoods_price.grid(row=0, column=0, sticky=W)

txtfoods_price = Entry(Appinfo, font=('arial', 6, 'bold'), bd=6, width=30, justify='right', relief='flat', state='disable', textvariable=foods_price)
txtfoods_price.grid(row=0, column=1, sticky=W)

lblcost_of_beverages = Label(Appinfo, font=('arial', 6, 'bold'), text="Cost of Beverages: \t", bd=8)
lblcost_of_beverages.grid(row=1, column=0, sticky=W)

txtcost_of_beverages = Entry(Appinfo, font=('arial', 6, 'bold'), bd=6, width=30, justify='right', relief='flat', state='disable', textvariable=drinks_price)
txtcost_of_beverages.grid(row=1, column=1, sticky=W)

lblcosto_of_service_charge = Label(Appinfo, font=('arial', 6, 'bold'), text="Service Charge: \t", bd=8)
lblcosto_of_service_charge.grid(row=2, column=0, sticky=W)

txtcost_of_service_charge = Entry(Appinfo, font=('arial', 6, 'bold'), bd=6, width=30, justify='right', relief='flat', state='disable', textvariable=service_charge)
txtcost_of_service_charge.grid(row=2, column=1, sticky=W)

#=================================== Payment Information =================================
lblcost_of_tax = Label(Appinfo, font=('arial', 6, 'bold'), text="Taxes: \t", bd=8)
lblcost_of_tax.grid(row=3, column=0, sticky=W)

txtcost_of_tax = Entry(Appinfo, font=('arial', 6, 'bold'), bd=6, width=30, justify='right', relief='flat', state='disable', textvariable=paid_tax)
txtcost_of_tax.grid(row=3, column=1, sticky=W)

lblcost_of_subtotal = Label(Appinfo, font=('arial', 6, 'bold'), text="Subtotal: \t", bd=8)
lblcost_of_subtotal.grid(row=4, column=0, sticky=W)

txtcost_of_subtotal = Entry(Appinfo, font=('arial', 6, 'bold'), bd=6, width=30, justify='right', relief='flat', state='disable', textvariable=sub_total)
txtcost_of_subtotal.grid(row=4, column=1, sticky=W)

lblcost_of_total = Label(Appinfo, font=('arial', 10, 'bold'), text="Total: \t", bd=8)
lblcost_of_total.grid(row=5, column=0, sticky=W)

txtcost_of_total = Entry(Appinfo, font=('arial', 10, 'bold'), bd=6, width=17, justify='right', relief=SUNKEN, state='disable', textvariable=total_cost)
txtcost_of_total.grid(row=5, column=1, sticky=E)

#======================================= App Buttons =====================================
btn_total = Button(Appbuttons, bd=6, fg="black", font=('arial', 10, 'bold'), width=16, height=3, text="Total", command=total).grid(row=0, column=0)
btn_receipt = Button(Appbuttons, bd=6, fg="black", font=('arial', 10, 'bold'), width=15, height=3, text="Receipt", command=receipt).grid(row=0, column=1)
btn_reset = Button(Appbuttons, bd=6, fg="black", font=('arial', 10, 'bold'), width=16, height=2, text="Reset", command=reset).grid(row=1, column=0)
btn_exit = Button(Appbuttons, bd=6, fg="black", font=('arial', 10, 'bold'), width=15, height=2, text="Exit", command=exit).grid(row=1, column=1)

root.mainloop()
