import tkinter as tk
from tkinter import ttk, messagebox, Text


class DateEntryForm:

    def __init__(self):

        self.window = tk.Tk()
        self.window.title("Date Entry Form")

        self.frame = tk.Frame(self.window)
        self.frame.pack()

        # Saving User Info
        self.user_info_frame = tk.LabelFrame(self.frame, text="User Information")
        self.user_info_frame.grid(row=0, column=0, padx=20, pady=20)

        self.first_name_label = tk.Label(self.user_info_frame, text="First Name")
        self.first_name_label.grid(row=0, column=0)
        self.last_name_label = tk.Label(self.user_info_frame, text="Last Name")
        self.last_name_label.grid(row=0, column=1)

        self.first_name_entry = tk.Entry(self.user_info_frame)
        self.last_name_entry = tk.Entry(self.user_info_frame)
        self.first_name_entry.grid(row=1, column=0)
        self.last_name_entry.grid(row=1, column=1)
        
        self.title = tk.Label(self.user_info_frame, text="Title")
        self.title_combobox = ttk.Combobox(self.user_info_frame, values=["", "Mr.", "Ms.", "Dr."])
        self.title.grid(row=0, column=2)
        self.title_combobox.grid(row=1, column=2)

        self.age_label = tk.Label(self.user_info_frame, text="Age")
        self.age_spinbox = tk.Spinbox(self.user_info_frame, from_=18, to=110)
        self.age_label.grid(row=2, column=0)
        self.age_spinbox.grid(row=3, column=0)
        
        self.nationality_label = tk.Label(self.user_info_frame, text="Nationality")
        self.nationality_combobox = ttk.Combobox(self.user_info_frame, values=["", "American", "British", "Chinese", "Indian", "French", "German", "Japanese", "Russian", "Brazilian", "Australian", "Canadian", "Mexican", "Italian", "Spanish", "South Korean", "Egyptian", "Nigerian", "South African", "Turkish", "Pakistani"]
)
        self.nationality_label.grid(row=2, column=1)
        self.nationality_combobox.grid(row=3, column=1)

        for widget in self.user_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)    

        # Saving Course Info
        self.courses_frame = tk.LabelFrame(self.frame, text="Courses")
        self.courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=20)
        
        self.registered_label = tk.Label(self.courses_frame, text="Registeration Status")
        
        self.reg_status_var = tk.StringVar(value="Not Registered")
        self.registered_check = tk.Checkbutton(self.courses_frame, text="Currently Registered", variable=self.reg_status_var, onvalue="Registered", offvalue="Not Registered")
        self.registered_label.grid(row=0, column=0)
        self.registered_check.grid(row=1, column=0)

        self.completed_course = tk.Label(self.courses_frame, text="#Completed Courses")
        self.completed_course_spinbox = tk.Spinbox(self.courses_frame, from_=0, to=10)
        self.completed_course.grid(row=0, column=1)
        self.completed_course_spinbox.grid(row=1, column=1)

        self.semesters = tk.Label(self.courses_frame, text="#of Semesters")
        self.semesters_spinbox = tk.Spinbox(self.courses_frame, from_=0, to=10)
        self.semesters.grid(row=0, column=2)
        self.semesters_spinbox.grid(row=1, column=2)

        for widget in self.courses_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)    

        # Terms & Condition 
        self.terms_frame = tk.LabelFrame(self.frame, text="Terms & Condition ")
        self.terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=20)

        self.terms_status_var = tk.IntVar()

        self.terms_check = tk.Checkbutton(self.terms_frame, text="I accept the terms & condition", variable=self.terms_status_var)
        self.terms_check.grid(row=0, column=0)

        for widget in self.terms_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)    
            
        # Print Data
        self.button = tk.Button(self.frame, text="Enter Data", command=self.enter_data)
        self.button.grid(padx=20, pady=20, sticky="news", row=3, column=0)

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.mainloop()

    def enter_data(self):
        if self.terms_status_var.get() == 0:
            messagebox.showwarning(title="Error", message="You have not accepted the terms")
        elif not self.first_name_entry.get() or not self.last_name_entry.get():
            messagebox.showwarning(title="Error", message="First Name or Last Name is Empty")
        else:
            first_name = self.first_name_entry.get()
            last_name = self.last_name_entry.get()
            title = self.title_combobox.get()
            age = self.age_spinbox.get()
            nationality = self.nationality_combobox.get()
            registration_status = self.reg_status_var.get()
            completed_courses = self.completed_course_spinbox.get()
            semesters = self.semesters_spinbox.get()

            custom_message_box = tk.Toplevel(self.window)
            custom_message_box.title("User Information")

            message = f"Name: {title} {first_name} {last_name}\nAge: {age}\nNationality: {nationality}\nRegistration Status: You are {registration_status}\nYour semester is {semesters} and the number of courses you have completed is/are {completed_courses}"

            text_widget = Text(custom_message_box, wrap=tk.WORD, height=10, width=50, font=("Helvetica", 10), padx=10, pady=10)  # Adjust font family and size
            text_widget.insert(tk.END, message)
            text_widget.config(state=tk.DISABLED)  # Make the text widget read-only
            text_widget.pack()

            close_button = tk.Button(custom_message_box, text="Close", command=custom_message_box.destroy)
            close_button.pack(pady=10)   

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.window.destroy()  


DateEntryForm()

