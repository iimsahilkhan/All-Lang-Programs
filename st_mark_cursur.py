import tkinter as tk
from tkinter import messagebox

class MarksheetGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Marksheet")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f0f0")

        # Title
        title_label = tk.Label(root, text="INVERTIS UNIVERSITY", font=("Arial", 16, "bold"), bg="#f0f0f0")
        title_label.pack(pady=10)
        
        subtitle_label = tk.Label(root, text="Student Marksheet", font=("Arial", 14), bg="#f0f0f0")
        subtitle_label.pack(pady=5)

        # Create frame for input fields
        input_frame = tk.Frame(root, bg="#f0f0f0")
        input_frame.pack(pady=20)

        # Subject marks entry fields
        self.subjects = {
            "Physics": tk.StringVar(),
            "Chemistry": tk.StringVar(),
            "Mathematics": tk.StringVar(),
            "English": tk.StringVar(),
            "Python": tk.StringVar()
        }

        # Create entry fields
        for subject, var in self.subjects.items():
            frame = tk.Frame(input_frame, bg="#f0f0f0")
            frame.pack(pady=5)
            tk.Label(frame, text=f"{subject}:", width=10, bg="#f0f0f0").pack(side=tk.LEFT)
            tk.Entry(frame, textvariable=var, width=10).pack(side=tk.LEFT)

        # Calculate button
        tk.Button(root, text="Calculate Results", command=self.calculate_results,
                 bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=20)

        # Results frame
        self.result_frame = tk.Frame(root, bg="#f0f0f0")
        self.result_frame.pack(pady=10)

    def calculate_results(self):
        try:
            # Get marks from entry fields
            marks = [int(var.get()) for var in self.subjects.values()]
            
            # Validate marks
            if any(mark < 0 or mark > 100 for mark in marks):
                messagebox.showerror("Error", "Marks should be between 0 and 100")
                return

            # Calculate results
            total = sum(marks)
            percentage = (total / 500) * 100
            average = total / 5

            # Determine grade
            if total >= 500:
                grade = "A"
            elif total >= 400:
                grade = "B"
            elif total >= 300:
                grade = "C"
            else:
                grade = "F"

            # Clear previous results
            for widget in self.result_frame.winfo_children():
                widget.destroy()

            # Display results
            results = [
                f"Total Marks: {total}",
                f"Percentage: {percentage:.2f}%",
                f"Average: {average:.2f}",
                f"Grade: {grade}"
            ]

            for result in results:
                tk.Label(self.result_frame, text=result, font=("Arial", 12),
                        bg="#f0f0f0").pack(pady=5)

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for all subjects")

if __name__ == "__main__":
    root = tk.Tk()
    app = MarksheetGUI(root)
    root.mainloop()
