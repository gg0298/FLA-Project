import tkinter as tk
from tkinter import messagebox

class PDAValidatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Push Down Automata - Enhanced String Validation")
        self.root.geometry("500x300")
        
        # Input field for the main string
        self.label_main = tk.Label(root, text="Enter the main string:")
        self.label_main.pack(pady=5)
        
        self.entry_main = tk.Entry(root, width=30)
        self.entry_main.pack(pady=5)
        
        # Input field for the substring
        self.label_substring = tk.Label(root, text="Enter the substring to search:")
        self.label_substring.pack(pady=5)
        
        self.entry_substring = tk.Entry(root, width=30)
        self.entry_substring.pack(pady=5)
        
        # Validate button
        self.validate_button = tk.Button(root, text="Validate String", command=self.validate_string)
        self.validate_button.pack(pady=10)
        
        # Result label
        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)
    
    def validate_string(self):
        main_string = self.entry_main.get()
        substring = self.entry_substring.get()
        
        if not main_string or not substring:
            messagebox.showwarning("Input Error", "Please enter both the main string and the substring.")
            return
        
        # Check cases
        start_match = main_string.startswith(substring)
        end_match = main_string.endswith(substring)
        middle_match = substring in main_string[1:-1]  # Checks if substring is in the middle
        
        # Result display logic
        results = []
        if start_match:
            results.append("String starts with the substring.")
        if end_match:
            results.append("String ends with the substring.")
        if middle_match:
            results.append("String contains the substring in the middle.")
        
        if results:
            result_text = "\n".join(results)
            self.result_label.config(text=result_text, fg="green")
            messagebox.showinfo("Result", result_text)
        else:
            self.result_label.config(text="No match found.", fg="red")
            messagebox.showwarning("Result", "No match found for the specified cases.")

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = PDAValidatorApp(root)
    root.mainloop()
