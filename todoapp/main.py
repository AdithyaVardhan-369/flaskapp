from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def intoduce():
    from .data.about import bot #controller
    return render_template('index.html',
        data=bot,
        question={'key':'name',"text":"what should I call you by?"}
    )

@app.route("/message",methods=['POST'])
def user_message():
    if request.method == 'POST':
        from .intents import handle
        return handle(request.form)
    else:
        return "INVALID"



if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
    
    