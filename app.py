from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import os
app = Flask(__name__)  # ✅ This must come BEFORE any @app.route

@app.route('/')
def home():
    return render_template('index.html')

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configure mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')


mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = Message(subject=f"Portfolio Message from {name}",
                      sender=email,
                      recipients=['your_email@gmail.com'],
                      body=message)
        mail.send(msg)
        flash('Message sent successfully!')
        return redirect(url_for('thankyou'))
    return render_template('contact.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

@app.route('/resume.html')
def resume():
    return render_template('resume.html')

if __name__ == '__main__':
    app.run(debug=True)
