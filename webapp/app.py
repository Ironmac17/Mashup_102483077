from flask import Flask, render_template, request
import subprocess
import re
import zipfile
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROLL_SCRIPT = os.path.abspath(os.path.join(BASE_DIR, "../program1/102483077.py"))


EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

def valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':

        singer = request.form['singer']
        videos = int(request.form['videos'])
        duration = int(request.form['duration'])
        email = request.form['email']
        send_email = request.form.get("send_email")

        # validations
        if videos <= 10:
            return render_template("index.html", message="Videos must be > 10")

        if duration <= 20:
            return render_template("index.html", message="Duration must be > 20 sec")

        if not valid_email(email):
            return render_template("index.html", message="Invalid email")

        output = "mashup.mp3"

        try:
            subprocess.run([
                "python",
                ROLL_SCRIPT,
                singer,
                str(videos),
                str(duration),
                output
            ], check=True)
        except Exception as e:
            return render_template("index.html", message="Mashup generation failed")

        # create zip
        zip_name = "result.zip"
        with zipfile.ZipFile(zip_name, 'w') as z:
            z.write(output)

        # send email only if checkbox selected
        if send_email:

            msg = EmailMessage()
            msg['Subject'] = 'Mashup Result'
            msg['From'] = EMAIL_USER
            msg['To'] = email
            msg.set_content("Your mashup file is attached")

            with open(zip_name,'rb') as f:
                msg.add_attachment(
                    f.read(),
                    maintype='application',
                    subtype='zip',
                    filename=zip_name
                )

            try:
                with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                    smtp.login(EMAIL_USER, EMAIL_PASS)
                    smtp.send_message(msg)
            except:
                return render_template("index.html", message="Email sending failed")

        return render_template("index.html", message="Mashup created successfully!")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
