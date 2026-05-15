from pyexpat.errors import messages

from flask import Flask, render_template, request, redirect, url_for, session
import os
from engine import agent, system_prompt

app = Flask(__name__)
app.secret_key = os.urandom(24) # Set a secret key for session management


@app.route('/')
def home():
    if 'messages' not in session:
        session['messages'] = []
    return render_template('chat.html', messages=session.get('messages', []))

@app.route('/send', methods=['POST'])
def send_message():
    message = request.form['message']
    response = agent.invoke(
    {
        "messages": [
            {
                "role": "system",
                "content": message
            }
        ]
    },
    config={
            "configurable": {
                "thread_id": "1"
            }
        }
    )
    session['messages'].append({"type": "human", "content": message})
    session['messages'].append({"type": "agent", "content": response["messages"][-1].content})
    session.modified = True

    return redirect(url_for('home'))

app.run(debug=True)

