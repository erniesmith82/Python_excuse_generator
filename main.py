import random
import tkinter as tk
from tkinter import messagebox

excuse_starters = [
    "I'm sorry, but",
    "Unfortunately,",
    "I'm afraid",
    "Due to unforeseen circumstances,",
    "I regret to inform you that",
    "Listen, it pains me to say this but",
    "I don't know how to tell you this but",
    "Yeah, I'm sorry, but"
]

excuse_reasons = [
    "my dog ate my homework",
    "my alarm didn't go off",
    "there was heavy traffic on my way",
    "I had a sudden family emergency",
    "my computer crashed"
]

excuse_endings = [
    "so I couldn't complete the task on time.",
    "which led to the delay.",
    "resulting in my inability to meet the deadline.",
    "causing me to miss out on the important event."
]

def generate_excuse():
    random_starter = random.choice(excuse_starters)
    random_reason = random.choice(excuse_reasons)
    random_ending = random.choice(excuse_endings)
    final_excuse = random_starter + " " + random_reason + " " + random_ending
    return final_excuse

def generate_excuses():
    num_excuses = int(num_excuse_entry.get())
    excuses_text.delete("1.0", tk.END)
    for _ in range(num_excuses):
        excuse = generate_excuse()
        excuses_text.insert(tk.END, excuse + "\n" + "-" * 40 + "\n")

def show_about():
    about_text = (
        "Excuse Generator\n\n"
        "This program generates random excuses for various situations.\n"
        "Created by: Ernie Smith\n"
        "Version: 1.0"
    )
    messagebox.showinfo("About", about_text)

# Create the main GUI window
root = tk.Tk()
root.title("Excuse Generator")

# Create widgets
num_excuse_label = tk.Label(root, text="Enter the number of excuses to generate:", font=("Arial", 14, "bold"))
num_excuse_entry = tk.Entry(root, width=5, font=("Arial", 12, "bold"))
generate_button = tk.Button(root, text="Generate Excuses", command=generate_excuses, font=("Arial", 12, "bold"))
excuses_text = tk.Text(root, wrap=tk.WORD, font=("Arial", 16), bg="black", fg="white")
about_button = tk.Button(root, text="About", command=show_about)

# Place widgets on the grid
num_excuse_label.grid(row=1, column=0, columnspan=2, pady=15)
num_excuse_entry.grid(row=1, column=2, columnspan=2, pady=5)
generate_button.grid(row=2, column=0, columnspan=4, pady=10)
excuses_text.grid(row=3, column=0, columnspan=4, padx=10, pady=10)
about_button.grid(row=4, column=0, columnspan=4, padx=5, pady=10)


# Start the GUI event loop
root.mainloop()