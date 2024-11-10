from flask import Flask, request, render_template_string
import tkinter as tk
import threading
import time

app = Flask(__name__)

# Function to show the break timer pop-up
def show_popup():
    root = tk.Tk()
    root.title("Break Time")

    window_width = 300
    window_height = 100
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_position = (screen_width // 2) - (window_width // 2)
    y_position = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    label = tk.Label(root, text="Break Time! Take a short break.", font=("Helvetica", 16))
    label.pack(expand=True)

    ok_button = tk.Button(root, text="OK", command=root.destroy)
    ok_button.pack()

    root.mainloop()

# Background thread function for the break timer
def break_timer_loop(interval):
    time.sleep(interval)
    show_popup()

# Route to serve the main page
@app.route("/", methods=["GET"])
def index():
    html_form = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Set Break Timer</title>
        <style>
            * {
              box-sizing: border-box;
              margin: 0;
              padding: 0;
            }
            body {
              font-family: Arial, sans-serif;
              display: flex;
              justify-content: center;
              align-items: center;
              height: 100vh;
              background: linear-gradient(to right, #667eea, #764ba2);
              color: #333;
            }
            .timer-container {
              background: #fff;
              padding: 30px;
              width: 100%;
              max-width: 400px;
              border-radius: 10px;
              box-shadow: 0 3px 10px rgba(0, 0, 0, 0.1);
              text-align: center;
            }
            h2 {
              font-size: 1.6rem;
              margin-bottom: 15px;
              color: #333;
            }
            label, input {
              font-size: 1rem;
            }
            input[type="number"] {
              width: 80px;
              padding: 6px;
              font-size: 1rem;
              text-align: center;
              border-radius: 6px;
              border: 1px solid #ddd;
              margin-bottom: 15px;
            }
            .submit-btn {
              background-color: #48c774;
              color: white;
              padding: 10px 20px;
              font-size: 1rem;
              cursor: pointer;
              border: none;
              border-radius: 6px;
              transition: background 0.3s ease, color 0.3s ease;
            }
            .submit-btn:hover {
              opacity: 0.9;
            }
        </style>
    </head>
    <body>
        <div class="timer-container">
            <h2>Set a Break Timer</h2>
            <form action="/start_break" method="post">
                <label for="interval">Enter break interval in minutes:</label><br>
                <input type="number" id="interval" name="interval" min="1" required><br>
                <input type="submit" value="Start Break Timer" class="submit-btn">
            </form>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_form)

# Route to start the break timer
@app.route("/start_break", methods=["POST"])
def start_break():
    try:
        interval = int(request.form.get("interval")) * 60  # Convert to seconds
        thread = threading.Thread(target=break_timer_loop, args=(interval,), daemon=True)
        thread.start()
        return "Break timer started! You can continue studying while the timer runs. <a href='/'>Back</a>"
    except ValueError:
        return "Invalid input. Please go back and enter a valid number."

if __name__ == "__main__":
    app.run(debug=True)
