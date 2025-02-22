from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage

# Flask setup
app = Flask(__name__)

# Email settings
SENDER_EMAIL = "tony.wilson58@gmail.com"
SENDER_PASSWORD = "hshr ylug xpxr lxvd"  # Replace this with your actual App Password

# Function to send email
def send_email(recipient_email, subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = recipient_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

# Routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send_email", methods=["POST"])
def send_email_route():
    recipient_email = request.form["email"]
    subject = "Psychological Safety Assessment"
    body = "Here is your psychological safety assessment link: https://forms.gle/dPz8gyMkrWA3pkdR7"

    if send_email(recipient_email, subject, body):
        return "Email sent successfully!"
    else:
        return "Error sending email. Please try again."

# Run Flask app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)  # Replace this with your actual App Password

# Function to send email
def send_email(recipient_email, subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = recipient_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

# Routes

def index():
    return render_template("index.html")

@app.route("/send_email", methods=["POST"])
def send_email_route():
    recipient_email = request.form["email"]
    subject = "Psychological Safety Assessment"
    body = "Here is your psychological safety assessment link: https://forms.gle/dPz8gyMkrWA3pkdR7"

    if send_email(recipient_email, subject, body):
        return "Email sent successfully!"
    else:
        return "Error sending email. Please try again."

# Run Flask app

    app.run(debug=True, host="0.0.0.0", port=5000)
