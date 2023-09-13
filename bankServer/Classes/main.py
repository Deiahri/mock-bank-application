import traceback
from flask import Flask, request
import dataInterpreter

app = Flask(__name__)


@app.route("/bank_server", methods=["POST", "GET"])
def home():
    import json
    try:
        raw_data = request.data.__str__()
        data = raw_data[raw_data.index("{"):-1].replace("\\'", "'").replace("\\\"", "\"")
        print(data)
        sent_data = json.loads(data)
        r = dataInterpreter.interpret(sent_data)
        with open("output.txt", "w") as file:
            json.dump(r, file, indent=4)
        return r
    except Exception as e:
        print(e.args)
        return {
            "error": f"{e}",
        }, 300


app.run()

