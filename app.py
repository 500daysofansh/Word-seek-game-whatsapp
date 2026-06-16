from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse
import random

app = Flask(__name__)

# Load 5-letter words from file
with open("words.txt", "r") as f:
    WORDS = [word.strip().lower() for word in f if len(word.strip()) == 5]

sessions = {}

def get_feedback(guess, target):
    result = ""
    for g, t in zip(guess, target):
        if g == t:
            result += "🟩"
        elif g in target:
            result += "🟨"
        else:
            result += "🟥"
    return result

@app.route("/message", methods=["POST"])
def message():
    user_id = request.form.get("From")
    text = request.form.get("Body", "").strip().lower()

    if not user_id:
        return Response("Missing sender info", status=400)

    if user_id not in sessions or text == "/new":
        sessions[user_id] = {"target": random.choice(WORDS), "guesses": []}
        reply = "Game started! Guess the 5-letter word!"
    elif len(text) != 5 or text not in WORDS:
        reply = f"{text} is not a valid word."
    else:
        target = sessions[user_id]["target"]
        feedback = get_feedback(text, target)
        sessions[user_id]["guesses"].append((text, feedback))
        reply = "\n".join([f"{f} {g.upper()}" for g, f in sessions[user_id]["guesses"]])
        if text == target:
            reply += "\n🎉 Correct! Start again with /new"
            del sessions[user_id]

    twiml = MessagingResponse()
    twiml.message(reply)
    return Response(str(twiml), mimetype="application/xml")

if __name__ == "__main__":
    app.run(port=5000)
