import tkinter as tk
from tkinter import *
import webbrowser
import re
from tkinter import messagebox
from tkinter import Tk, Label
from PIL import ImageTk, Image

def generate_document():
    # Get user inputs
    type1 = type_var.get()
    specific_type = specific_type_var.get()
    topic = topic_entry.get()
    num = num_entry.get()
    whom_to_prefer = whom_to_prefer_var.get()

    # Generate document
    if specific_type ==  "Quiz":
        output = f"Create a {specific_type} on {topic} consisting of {num} questions, preferred for {whom_to_prefer}"
    elif specific_type == "Slides":
        output = f"Create a {specific_type} on {topic} consisting of {num} slides, preferred for {whom_to_prefer}"
    else:
        output = f"Create a {specific_type} on {topic} consisting of {num} lines, preferred for {whom_to_prefer}"
    
    # Clear previous output
    #if output_entry:
    output_entry.delete(0, tk.END)
        
    # Display output in entry box
    output_entry.insert(0, output)

def callback(output):
    # Define ChatGPT URL
    chatgpt_url = "https://chat.openai.com"

    # Open the ChatGPT website in the default browser
    webbrowser.open(chatgpt_url)
    
    return output

# Validation function to check for special characters
def validate_topic(topic):
    if not topic:
        return True  # Allow empty string
    pattern = r'^[a-zA-Z0-9 ]+$' # pattern to validate only alphabets, digits and spaces
    if re.search(pattern, topic):
        return True
    else:
        messagebox.showerror("Error", "Topic name can only contain alphabets, digits and spaces!")
        return False

def validate_numbers(numbers):
    if not numbers:
        return True  # Allow empty string
    pattern = r"^[0-9]+$"
    if re.search(pattern, numbers):
        return True
    else:
        messagebox.showerror("Error", "Numbers field can only contain digits!")
        return False



# Create tkinter GUI
root = tk.Tk()
root.title("CHATGTP PROMTER")

# maximize the main window
root.state('zoomed')

#root.geometry('1200x450')
#root.resizable(0, 0)

headlabelfont = ("Noto Sans CJK TC", 15, 'bold')
labelfont = ('Garamond', 14)
entryfont = ('Garamond', 12)

lf_bg = 'Coral'

title_frame = Frame(root, bg=lf_bg)
title_frame.pack(side=TOP, padx=5, pady=5, fill=X)

tk.Label(title_frame, text="CHAT GPT", font=headlabelfont, bg='Firebrick').pack(side=TOP, fill=X)

image = Image.open("C:\\Users\\Admin\\OneDrive\\Documents\\EXE Files\\Chatgpt Promter\\Chat.png")
image = image.resize((1650, 30))
tk_image = ImageTk.PhotoImage(image)

image_label = tk.Label(title_frame, image=tk_image)
image_label.pack(anchor="se")

Frame(root, bg=lf_bg)

# Create type menu
type_options = {
    "Teach": ["Slides", "Story", "Socratic method of teaching","Gamification in teaching"],
    "Asses": ["Quiz","Puzzle","Projects"],
}

audience_options = ["Age between 0 to 10", "Age between 11 to 15", "Age between 16 to 20", "Age between 21 to 35", "Age above 35"]

type_var = tk.StringVar(value="Teach")
specific_type_var = tk.StringVar(value="Slides")
whom_to_prefer_var = tk.StringVar(value="Age between 0 to 10")

type_frame = Frame(root, bg=lf_bg)
type_frame.pack(side=TOP, padx=5, pady=5, fill=X)

type_label = tk.Label(type_frame, text="Type:", width=20, font=labelfont, bg=lf_bg)
type_label.pack(side=LEFT)


def update_specific_type_options(value):
    specific_type_var.set(type_options[value][0])
    specific_type_menu["menu"].delete(0, "end")
    for specific_type in type_options[value]:
        specific_type_menu["menu"].add_command(label=specific_type, command=lambda specific_type=specific_type: specific_type_var.set(specific_type))


type_menu = tk.OptionMenu(type_frame, type_var, *type_options.keys(), command=update_specific_type_options)
type_menu.pack(side=LEFT, padx=5, pady=5, fill=X)

specific_type_frame = Frame(root, bg=lf_bg)
specific_type_frame.pack(side=TOP, padx=5, pady=5, fill=X)
specific_type_label = tk.Label(specific_type_frame, text="Specific type:",  width=20, font=labelfont, bg=lf_bg)
specific_type_label.pack(side=LEFT)
specific_type_menu = tk.OptionMenu(specific_type_frame, specific_type_var, *type_options[type_var.get()])
specific_type_menu.pack(side=LEFT, padx=5, pady=5, fill=X)

# Create other input fields
topic_frame = Frame(root, bg=lf_bg)
topic_frame.pack(side=TOP, padx=5, pady=5, fill=X)
topic_label = tk.Label(topic_frame, text="Topic:",  width=20, font=labelfont, bg=lf_bg)
topic_label.pack(side=LEFT)
topic_entry = tk.Entry(topic_frame, width=90, font=entryfont)
topic_entry.pack(side=LEFT, padx=5, pady=5, fill=X)

# Attach validation function to topic entry widget
validate_topic_cmd = root.register(validate_topic)
topic_entry.config(validate="key", validatecommand=(validate_topic_cmd, '%P'))


num_frame = Frame(root, bg=lf_bg)
num_frame.pack(side=TOP, padx=5, pady=5, fill=X)
num_label = tk.Label(num_frame, text="Number:",  width=20, font=labelfont, bg=lf_bg)
num_label.pack(side=LEFT)
num_entry = tk.Entry(num_frame, width=90, font=entryfont)
num_entry.pack(side=LEFT, padx=5, pady=5, fill=X)

# Attach validation function to numbers entry widget
validate_numbers_cmd = root.register(validate_numbers)
num_entry.config(validate="key", validatecommand=(validate_numbers_cmd, '%P'))


whom_to_prefer = Frame(root, bg=lf_bg)
whom_to_prefer.pack(side=TOP, padx=5, pady=5, fill=X)
whom_to_prefer_label = tk.Label(whom_to_prefer, text="Audience:", width=20, font=labelfont, bg=lf_bg)
whom_to_prefer_label.pack(side=LEFT)
whom_to_prefer_menu = tk.OptionMenu(whom_to_prefer, whom_to_prefer_var, *audience_options)
whom_to_prefer_menu.pack(side=LEFT, padx=5, pady=5, fill=X)

# Create generate button
button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, pady=10)
generate_button = tk.Button(button_frame, text="Generate", command=generate_document, width=15, font=labelfont)
generate_button.grid(row=0, column=0, padx=5, pady=5, sticky=W)

# Create ChatGPT button
chatgpt_button = tk.Button(button_frame, text="Open ChatGPT", command=lambda: callback(None), width=15, font=labelfont)
chatgpt_button.grid(row=0, column=1, padx=5, pady=5, sticky=W)

# Create output label
output_frame = Frame(root, bg=lf_bg)
output_frame.pack(side=TOP, padx=5, pady=5, fill=X)
output_label = tk.Label(output_frame, text="", width=20, font=labelfont, bg=lf_bg)
output_label.pack(side=LEFT)
output_entry = tk.Entry(output_frame, width=90, font=entryfont)
output_entry.pack(side=LEFT, padx=5, pady=5, fill=X)


def clear_fields():
    topic_entry.delete(0, tk.END)
    num_entry.delete(0, tk.END)
    output_entry.delete(0, tk.END)
    
# Clear button
clear_button = tk.Button(button_frame, text="Clear", command=lambda: clear_fields(), width=15, font=labelfont)
clear_button.grid(row=0, column=2, padx=5, pady=5, sticky=E)

# Run the tkinter mainloop
root.mainloop()
