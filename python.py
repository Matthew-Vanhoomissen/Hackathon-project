from flask import Flask, request, render_template
import tkinter as tk
import threading
import time

app = Flask(__name__)

def show_popup():
    root = tk.Tk()
    root.title("Reminder")
    
    window_width = 300
    window_height = 100
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    x_position = (screen_width // 2) - (window_width // 2)
    y_position = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    
    label = tk.Label(root, text="You got this!", font=("Helvetica", 16))
    label.pack(expand=True)
    
    ok_button = tk.Button(root, text="OK", command=root.destroy)
    ok_button.pack()
    
    root.mainloop()

def reminder_loop(interval):
    while True:
        time.sleep(interval)
        show_popup()

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/start_reminder", methods=["POST"])
def start_reminder():
    try:
        interval = int(request.form.get("interval")) * 60  # Convert to seconds
        thread = threading.Thread(target=reminder_loop, args=(interval,), daemon=True)
        thread.start()
        return "Reminder started! Close this tab to stop. <a href='/'>Back</a>"
    except ValueError:
        return "Invalid input. Please go back and enter a valid number."

if __name__ == "__main__":
    app.run(debug=True)
