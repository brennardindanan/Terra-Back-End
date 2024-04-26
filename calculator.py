# Importing tkinter Library into Python Program
from tkinter  import * 
from Country import countries
from tkinter import messagebox
# Importing matplotlib as plt there will be a way to import this 
gui = Tk()  # Creating Object to Open GUI
count= countries()
gui.title("CO2 Calculator")  # Creating Title
gui.configure(background = "SeaGreen1")  # Setting Background Color

list_ques=[]  # Creating List
# Entry Boxes
country = Entry(gui)
country.grid(row = 0, column = 0 )
#function to go to the different country functions
def PickCountry():
  try:
    int(country.get())
    messagebox.showerror(title="Error",message="Wrong Input")
    country.delete(0,END)
  except:
    pass
  if country.get() == "":
    country.delete(0,END)
    messagebox.showerror(title="Error",message="No Input")
  else:
    if (country.get()).upper() == "UK" or (country.get()).upper() == "US":
      messagebox.showinfo(title="Update",message="Country added")
      list_ques.append((country.get()).lower())
      country.delete(0,END)
    elif (country.get()).lower() == "united kingdom" or (country.get()).upper() == "united states":
        messagebox.showinfo(title="Update",message="Country added")
        list_ques.append((country.get()).lower())
    else:
        messagebox.askokcancel(title="Error",message="Only UK and US is avaliable right now")
        country.delete(0,END)
  
#Button for submitting a country
submit_country = Button(gui,text="Submit",command=PickCountry)
submit_country.grid(row=1,column=0)

housing_elec = Entry(gui)
housing_elec.grid(row = 2, column = 0 )
housing_heat = Entry(gui)
housing_heat.grid(row = 3, column = 0)

def housing_submit():
  if housing_elec.get()=="":
    messagebox.showwarning(title="Error",message="No input")
  else:
    messagebox.askokcancel(title="Update",message="Are you sure?")
    list_ques.append(housing_elec.get())
    housing_elec.delete(0,END)

  if housing_heat.get()=="":
    messagebox.showwarning(title="Error",message="No input")
  else:
    messagebox.askokcancel(title="Update",message="Are you sure?")
    list_ques.append(housing_heat.get())
    housing_heat.delete(0,END)
  return list_ques

housing_button = Button(gui,text="Submit",command = housing_submit)
housing_button.grid(row=4,column=0)  

travel = Entry(gui)
travel.grid(row = 5, column = 0)

def traveling_submit():
  if travel.get()=="":
    messagebox.showwarning(title="Error",message="No input")
  else:
    messagebox.askokcancel(title="Update",message="Are you sure")
    list_ques.append(travel.get())
    travel.delete(0,END)
  return list_ques

travel_button = Button(gui,text="Submit",command=traveling_submit)
travel_button.grid(row=6,column=0)


def questioninfo():#make it possible get country and choose a different different funciton based on it
    num = ""
    results = []
    country = list_ques[0]
    list_ques.remove(country)
    for ques in list_ques:
        for convert in ques:
            if convert == ",":
                continue
            num += convert
        results.append(int(num))
        num = ""
    
    #pick a certian country to do caculations
    if country == "uk":
      week = countries.COFootprint_week_UK(results=results)
      year = countries.COFootprint_year_UK(results=results)
      messagebox.showinfo(title="Carbon Footprint", message="In a week your carbon Foot print is\n{0}".format(week) )
      messagebox.showinfo(title="Carbon Footprint", message="In a year your carbon Foot print is\n{0}".format(year) )
    elif country == "us":
      week = count.COFootprint_week_US(results)
      year = count.COFootprint_year_US(results)
      messagebox.showinfo(title="Carbon Footprint", message="In a week your carbon Foot print is\n{0}".format(week) )
      messagebox.showinfo(title="Carbon Footprint", message="In a year your carbon Foot print is\n{0}".format(year) )

final_submit = Button(gui,text="Submit all info",command=questioninfo)
final_submit.grid(row=7,column=0)


  
# Corresponding Entry Box Labels
box_one = Label(gui, text = "Country Location", bg = "gray26", fg = "white", font = "Arial")
box_one.grid(row = 0, column = 1,sticky=W)

box_two = Label(gui, text = "Electricity Usage Per Week (kWh)", bg = "gray26", fg = "white", font = "Arial")
box_two.grid(row = 2, column = 1,sticky=W)

box_three = Label(gui, text = "Gas Usage Per Week (kWh)", bg = "gray26", fg = "white", font = "Arial")
box_three.grid(row = 3, column = 1,sticky=W)

box_four = Label(gui, text = "Gasoline Usage Per Day", bg = "gray26", fg = "white", font = "Arial")
box_four.grid(row = 5, column = 1,sticky=W)

# Main Game Loop to keep GUI open Until Quit
gui.mainloop()#main loop to keep GUI open until quit
