from tkinter import*
from tkinter import Tk, ttk, Label, Entry, Frame, Button, OptionMenu, StringVar
import mysql.connector
import random
from tkinter import messagebox


class Add_Land:
    def __init__(self, root):
        self.root=root
        self.root.title("Land Management System")
        self.root.geometry("1195x440+330+330")




        #===================Variables=====================
        self.var_landid=StringVar()
        x=random.randint(1,99999)
        self.var_landid.set(str(x))

        self.var_owner_name=StringVar()
        self.var_land_area=StringVar()
        self.var_state=StringVar()
        self.var_city=StringVar()
        self.var_location=StringVar()
        self.var_address=StringVar()
        self.var_notes=StringVar()
        self.var_area_unit=StringVar()
        self.var_sale_price=StringVar()
        self.var_purchased_price=StringVar()
        self.var_usage=StringVar()



        


        #================TITLE=======================
        lbl_title=Label(self.root, text="Add Land Details", font=("times new roman", 22,"bold"), bg="black", fg="gold", relief=RIDGE)
        lbl_title.place(x=0, y = 0, width=1195, height=30)


        #==============Label Frame===============
        labelframeleft=LabelFrame(self.root, bd=2, relief=RIDGE, text="Land Details", font=("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=30, width=325, height=405)

        #============Entries========
        #Land ID
        lbl_landId=Label(labelframeleft, text="Land ID:",font=("times new roman", 12), padx=2, pady=6)
        lbl_landId.grid(row=0, column=0, sticky=W)

        entry_id=ttk.Entry(labelframeleft, textvariable=self.var_landid,width=18,font=("times new roman", 12),state="readonly")
        entry_id.grid(row=0, column=1)
        #Owner info
        lbl_owner_name = Label(labelframeleft, text="Owner Name:", font=("times new roman", 12), padx=2, pady=6)
        lbl_owner_name.grid(row=1, column=0, sticky="w")
        entry_owner_name = Entry(labelframeleft, textvariable=self.var_owner_name,width=20, font=("times new roman", 12))
        entry_owner_name.grid(row=1, column=1)
        #State
        lbl_state = Label(labelframeleft, text="State:", font=("times new roman", 12), padx=2, pady=6)
        lbl_state.grid(row=2, column=0, sticky="w")
        self.combo_state = ttk.Combobox(labelframeleft, textvariable=self.var_state, font=("times new roman", 12), width=20, state="readonly")
        self.combo_state["value"] = ("Ashanti", "Ahafo Region", "Bono East Region", "Bono Region", "Central Region", "Eastern Region", 
                                     "Great Accra Region", "Northern Region" ,"North East Region", "Upper Eastern Region",
                                     "Upper Western Region", "Volta Region" ,"Western Region", "Oti Region", "Savannah Region")  # Add your states here
        self.combo_state.current(0)
        self.combo_state.grid(row=2, column=1)
        
        #City
        
        lbl_city = Label(labelframeleft, text="City:", font=("times new roman", 12), padx=2, pady=6)
        lbl_city.grid(row=3, column=0, sticky="w")
        self.combo_city = ttk.Combobox(labelframeleft, textvariable=self.var_city, font=("times new roman", 12), width=20, state="readonly")
        self.combo_city.grid(row=3, column=1)
        self.combo_state.bind("<<ComboboxSelected>>", self.update_cities)

        # Update cities based on the selected state
        self.update_cities()
        
        #Land Area
        lbl_size_area = Label(labelframeleft, text="Size/Area:", font=("times new roman", 12), padx=2, pady=6)
        lbl_size_area.grid(row=4, column=0, sticky=W)
        entry_size_area = Entry(labelframeleft, width=14, textvariable=self.var_land_area, font=("times new roman", 12))
        entry_size_area.grid(row=4, column=1, sticky=W)
        self.size_area_unit_var = StringVar(value="Acres")
        option_menu_size_area_unit = OptionMenu(labelframeleft, self.size_area_unit_var, "Acres", "Square meters")
        option_menu_size_area_unit.grid(row=4, column=1, sticky=E)

        # Sales Price
        lbl_sale_price = Label(labelframeleft, text="Sale Price:", font=("times new roman", 12), padx=2, pady=6)
        lbl_sale_price.grid(row=5, column=0, sticky=W)
        entry_sale_price = Entry(labelframeleft, textvariable=self.var_sale_price, width=20, font=("times new roman", 12))
        entry_sale_price.grid(row=5, column=1)

        # Purchase Price
        lbl_purchase_price = Label(labelframeleft, text="Purchase Price:", font=("times new roman", 12), padx=2, pady=6)
        lbl_purchase_price.grid(row=6, column=0, sticky=W)
        entry_purchase_price = Entry(labelframeleft, textvariable=self.var_purchased_price, width=20, font=("times new roman", 12))
        entry_purchase_price.grid(row=6, column=1)

        # Usage
        lbl_usage = Label(labelframeleft, text="Usage:", font=("times new roman", 12), padx=2, pady=6)
        lbl_usage.grid(row=7, column=0, sticky=W)
        entry_usage = Entry(labelframeleft, textvariable=self.var_usage, width=20, font=("times new roman", 12))
        entry_usage.grid(row=7, column=1)

        # Address
        lbl_address = Label(labelframeleft, text="Address:", font=("times new roman", 12), padx=2, pady=6)
        lbl_address.grid(row=8, column=0, sticky=W)
        entry_address = Entry(labelframeleft, textvariable=self.var_address, width=20, font=("times new roman", 12))
        entry_address.grid(row=8, column=1)

        # Notes
        lbl_notes = Label(labelframeleft, text="Notes:", font=("times new roman", 12), padx=2, pady=6)
        lbl_notes.grid(row=9, column=0, sticky=NW)
        entry_notes = Entry(labelframeleft, width=20, textvariable=self.var_notes, font=("times new roman", 12))
        entry_notes.grid(row=9, column=1, sticky=NW)

        #========================Button Frame=============================
        button_frame=LabelFrame(labelframeleft, bd=2, relief=RIDGE, padx=2)
        button_frame.place(x=4, y=340, width=310, height=40)
        save_button = Button(button_frame, text="Save Entry", command=self.add_data,font=("times new roman", 12), bg="black", fg="gold")
        save_button.grid(row=9, column=0, padx=1, pady=1)

        update_button = Button(button_frame, text="Update",command=self.update,font=("times new roman", 12), bg="black", fg="gold")
        update_button.grid(row=9, column=1, padx=1, pady=1)
        delete_button = Button(button_frame, text="Delete",command=self.delete,font=("times new roman", 12), bg="black", fg="gold")
        delete_button.grid(row=9, column=2, padx=1, pady=1)
        reset_button = Button(button_frame, text="Reset",command=self.reset,font=("times new roman", 12), bg="black", fg="gold")
        reset_button.grid(row=9, column=3, padx=1, pady=1)

        


        #============Table Frame Search System===============
        tableframe=LabelFrame(self.root, bd=2, relief=RIDGE, text="View Table", font=("times new roman", 12, "bold"), padx=2)
        tableframe.place(x=335, y=30, width=860, height=400)

        lbl_searchby=Label(tableframe, font=("times new roman", 12, "bold"), text="Search By:", bg="Blue", fg="white")
        lbl_searchby.grid(row=0, column=0, sticky=W, padx=2)
        self.var_search=StringVar()
        search=ttk.Combobox(tableframe,textvariable=self.var_search, font=("times new roman", 12, "bold"), width=24, state="readonly")
        search["values"]=("Land ID", "Owner's Name", "Location", "price") 

        search.current(0)
        search.grid(row=0, column=1, padx=2)
        self.var_txtSearch=StringVar()
        text_search=ttk.Entry(tableframe, textvariable=self.var_txtSearch,font=("times new roman", 12), width=24)
        text_search.grid(row=0, column=2, padx=2)

        search_button=Button(tableframe, text="Search", command=self.search,font=("times new roman", 11, "bold"), bg="black", fg="Gold", width=10)
        search_button.grid(row=0, column=3,padx=1)

        showall_button=Button(tableframe, text="Show All", command=self.show_data,font=("times new roman", 11, "bold") ,bg="black", fg="Gold", width=10)
        showall_button.grid(row=0, column=4,padx=1)

        #===========================DATA TABLE=================
        data_tableframe=LabelFrame(tableframe, bd=2, relief=RIDGE, padx=2)
        data_tableframe.place(x=0, y=50, width=860, height=325)

        scroll_xaxis=ttk.Scrollbar(data_tableframe, orient=HORIZONTAL)
        scroll_yaxis=ttk.Scrollbar(data_tableframe, orient=VERTICAL)

        self.land_details_table=ttk.Treeview(data_tableframe, column=("Land ID", "Owner's Name","State", "City","Sales Price", "Purchased Price","Land's Area","Area Unit",
                                                                        "Address","Usage",  "Notes" ), xscrollcommand=scroll_xaxis.set, yscrollcommand=scroll_yaxis.set)
        
        scroll_xaxis.pack(side=BOTTOM,fill=X)
        scroll_yaxis.pack(side=RIGHT,fill=Y)

        scroll_xaxis.config(command=self.land_details_table.xview)
        scroll_yaxis.config(command=self.land_details_table.yview)

        self.land_details_table.heading("Land ID", text="Land ID")
        self.land_details_table.heading("Owner's Name", text="Owner's Name")
        self.land_details_table.heading("State", text="State")
        self.land_details_table.heading("City", text="City")
        self.land_details_table.heading("Sales Price", text="Sales Price")
        self.land_details_table.heading("Purchased Price", text="Purchased Price")
        self.land_details_table.heading("Land's Area", text="Land's Area")
        self.land_details_table.heading("Area Unit", text="Area Unit")
        self.land_details_table.heading("Address", text="Address")
        self.land_details_table.heading("Usage", text="Usage")
        
        self.land_details_table.heading("Notes", text="Notes")
        


        # Show the headings and pack the Treeview
        self.land_details_table['show'] = 'headings'
        

        self.land_details_table.column("Land ID", width=80, anchor=W)
        self.land_details_table.column("Owner's Name", width=150, anchor=W)
        self.land_details_table.column("State", width=100, anchor=W)
        self.land_details_table.column("City", width=100, anchor=W)
        self.land_details_table.column("Sales Price", width=100, anchor=W)
        self.land_details_table.column("Purchased Price", width=100, anchor=W)
        
        self.land_details_table.column("Land's Area", width=100, anchor=W)
        self.land_details_table.column("Area Unit", width=100, anchor=W)
        self.land_details_table.column("Address",  width=100, anchor=W)
        self.land_details_table.column("Usage",  width=100, anchor=W)
        
        self.land_details_table.column("Notes",  width=100, anchor=W)
 
        self.land_details_table.pack(fill=BOTH, expand=1)
        self.land_details_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.show_data()
  #======================UPDATE CITY FUNCTION==================
    def update_cities(self, event=None):
        state = self.combo_state.get()
        cities = {
            "Ashanti": ["Kumasi", "Obuasi", "Mampoong", "Agogo", "Ejura", "Konongo", "Mamponteng", "Jauso", "Akronfuom", "Barekese"],
            "Ahafo Region": ["Mim Ahafo", "Goaso", "Becham", "Duayaw Nkwanta", "Ataechimantia", "Kenyasi", "Hwidiem"],
            "Bono East Region": ["Atelbubu-Amantin", "Kinstampo North", "Nkoranza South", "Knoaranza", "Pru East", "Pru West"],
            "Bono Region": ["Sanyani", "Berekum", "Dormaa Ahenkro", "Wenchi", "Odaumasi", "Banda", "Berekum East", "Berekum West", "Dormaa Central", "Dormaa West", "Jaman North", "Jaman South", "Sunyani", "Sunyani West", "Tain"],
            "Central Region": ["Cape Coast", "Elmina", "Kakum", "Assin Mnaso", "Winneba", "Mankessim", "Apong Swedru"],
            "Eastern Region": ["Koforidua", "Abetifi", "Aburi", "Adukrom", "Akim Swedru", "Akro Odumase Krobo", "Akwamuman", "Akwatia", "Akosombo", "Anum", "Asafo"],
            "Great Accra Region": ["Accra", "Gbawe", "Tema", "Dome", "Taifa", "Teshie", "Madina", "Nungua", "Lashibi"],
            "Northern Region": ["Tamale", "Gushegu", "Yendi", "Bimbilla", "Walewale", "Salaga", "Damongo", "Savelugu", "Bolgatanga", "Nalerigu"],
            "North East Region": ["Nalerigu", "Bunkpurugu", "Yendi", "Bimbilla", "Walewale", "Salaga"],
            "Upper Eastern Region": ["Bolgatanga", "Paga", "Sandema", "Bawku", "Zebilla"],
            "Upper Western Region": ["Nandom", "Daffiema", "Jirapa", "Kaleo", "Nadowli", "Lawra", "Tumu"],
            "Volta Region": ["Ho", "Sogakope", "Amedzofe", "Tafi Atome", "Keta", "Kpando", "Hohoe", "Anloga", "Denu"],
            "Western Region": ["Aowin", "Enchi", "Daieso", "Bia Bia", "Bibiani", "Bodi", "Juaboso", "Sefwi Adabokrom", "Suaman"],
            "Oti Region": ["Biakoye", "Dambai", "Jasikan", "Nkwanta", "Knonya"],
            "Savannah Region": ["Bole", "Buipe", "Damongo", "Daboya", "Kpalbe", "Salaga", "Sawla"]
        }

        city_list = cities.get(state, [])
        
        # Clear the current list of cities in the combobox
        self.combo_city['values'] = city_list
        
        # Select the first city if the list is not empty
        if city_list:
            self.combo_city.current(0)
        else:
            # If no cities are available, clear the selection
            self.combo_city.set('')


#====================ADD Data FUnction============
    def add_data(self):
        if self.var_owner_name.get()=="" or self.var_sale_price.get()=="":
            messagebox.showerror("Error", "Owner's Name or Sale's Price is not added!",parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost",
                                            username="root",
                                            password="safi",
                                            database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into land_mangement values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                        self.var_landid.get(),
                                        self.var_owner_name.get(),
                                        self.var_state.get(),
                                        self.var_city.get(),
                                        self.var_sale_price.get(),
                                        self.var_purchased_price.get(),
                                        self.var_land_area.get(),
                                        self.size_area_unit_var.get(),
                                
                                        self.var_address.get(),
                                        self.var_usage.get(),
                                        self.var_notes.get()
                                                            ))
                conn.commit()
                self.show_data()
                conn.close()
                messagebox.showinfo("Success", "Land has been added!", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Something Went Wrong: {str(es)}", parent=self.root)




    def show_data(self):
        conn=mysql.connector.connect(host="localhost",
                                            username="root",
                                            password="safi",
                                            database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from land_mangement")
        fetched_data= my_cursor.fetchall()
        if len(fetched_data)!=0:
            self.land_details_table.delete(*self.land_details_table.get_children())
            for i in fetched_data:
                self.land_details_table.insert("",END,values=i)
            
            conn.commit()
        conn.close()


    def get_cursor(self, event=''):
        cursor_row = self.land_details_table.focus()  # Get the focused row
        content = self.land_details_table.item(cursor_row)
        row = content["values"]

        # Check if row has the expected number of elements
        if row and len(row) >= 10:  # Ensure row has at least 10 elements
            self.var_landid.set(row[0])
            self.var_owner_name.set(row[1])
            self.var_state.set(row[2])
            self.var_city.set(row[3])
            self.update_cities()
            self.var_sale_price.set(row[4])
            self.var_purchased_price.set(row[5])
            self.var_land_area.set(row[6])
            self.var_area_unit.set(row[7])
            
            self.var_address.set(row[8])
            self.var_usage.set(row[9])
            self.var_notes.set(row[10])
        else:
            # Handle cases where row is empty or has insufficient data
            print("No data or incomplete data in the selected row")



    def update(self):
        if self.var_owner_name.get()=='':
            messagebox.showerror("Error", "Please Enter the Owner's Name", parent=self.root)
        else:

            conn=mysql.connector.connect(host="localhost",
                                                username="root",
                                                password="safi",
                                                database="management")
            my_cursor=conn.cursor()
            my_cursor.execute(
                                "UPDATE land_mangement SET `Owner's Name`=%s, `State`=%s, `City`=%s,`sales Price`=%s, `Purchased price`=%s, `Land's Area`=%s, `Area Unit`=%s, `Address`=%s, `Usage`=%s, `Notes`=%s WHERE `Land ID`=%s",
                                (
                                    self.var_owner_name.get(),
                                    self.var_state.get(),
                                    self.var_city.get(),
                                    self.var_sale_price.get(),
                                    self.var_purchased_price.get(),
                                    self.var_land_area.get(),
                                    self.size_area_unit_var.get(),
                                    
                                    self.var_address.get(),
                                    self.var_usage.get(),
                                    self.var_notes.get(),
                                    self.var_landid.get(),
                                )
                            )
            conn.commit()
            self.show_data()
            conn.close()
            messagebox.showinfo("Update", "The information has been updated successfully", parent=self.root)



    """def delete(self):
        delete=messagebox.askyesno("Land Management System", "Are you sure you want to delete this land or entry?", parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",
                                                username="root",
                                                password="safi",
                                                database="management")
            my_cursor=conn.cursor()
            query="delete from land_mangement where 'Land ID'=%s"
            value=(self.var_landid.get(),)
            my_cursor.execute(query, value)
        else:
            if not delete:
                return
            
        conn.commit()
        self.show_data()
        conn.close()"""
    def delete(self):
        # Confirm deletion with the user
        confirm_delete = messagebox.askyesno(
            "Land Management System", 
            "Are you sure you want to delete this land or entry?", 
            parent=self.root
        )

        if confirm_delete:
            try:
                # Connect to the MySQL database
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="safi",
                    database="management"
                )
                my_cursor = conn.cursor()

                # SQL query to delete the record with the given Land ID
                query = "DELETE FROM land_mangement WHERE `Land ID` = %s"
                value = (self.var_landid.get(),)  

                my_cursor.execute(query, value)  
                conn.commit() 

                # Refresh the TreeView after deletion
                self.show_data()  
                messagebox.showinfo("Success", "Entry has been deleted successfully.", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"An error occurred: {str(es)}", parent=self.root)

            finally:
                # Always close the connection
                conn.close()

        else:
            # If user cancels, do nothing
            messagebox.showinfo("Canceled", "Deletion has been canceled.", parent=self.root)


    def reset(self):
       
        # Clear other fields
        self.var_owner_name.set("")  # Clear the owner's name
        
        self.var_sale_price.set("")  # Clear the sale price
        self.var_purchased_price.set("")  # Clear the purchased price
        self.var_land_area.set("")  # Clear the land area
        self.size_area_unit_var.set("Acres")  # Reset the unit of area
        self.var_location.set("")  # Clear the location
        self.var_address.set("")  # Clear the address
        self.var_usage.set("")  # Clear the usage
        self.var_notes.set("")  # Clear the notes
         # Generate a new random Land ID
        
        x = random.randint(1, 99999)  # Random ID from 1 to 99999
        self.var_landid.set(str(x))  # Set the Land ID


        # Reset any additional elements or UI components if needed
        # For example, if you have a Combobox for location, you might reset its selection
        #self.combo_loc.current(0)  # Set Combobox to the first value (default)

    def search(self):
        conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="safi",
                    database="management"
                )
        my_cursor = conn.cursor()
        column = self.var_search.get()  # Get the search column
        search_text = self.var_txtSearch.get()  # Get the text to search for

        query = f"SELECT * FROM land_mangement WHERE `{column}` LIKE %s"
        search_value = (f"%{search_text}%",)  # Using a tuple for parameterized queries

        my_cursor.execute(query, search_value)  # Execute the parameterized query
        rows = my_cursor.fetchall() 
        
        if len (rows)!=0:
            self.land_details_table.delete(*self.land_details_table.get_children())
            for i in rows:
                self.land_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()





def main():
    root=Tk()
    obj=Add_Land(root)
    root.mainloop()




if __name__ == "__main__":
    main()