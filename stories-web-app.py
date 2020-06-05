from flask import Flask, redirect, request, render_template

class Story_Node(object):
    def __init__(self, sentence, root=None):
        self.sentence = sentence
        self.root = root
        self.nodes = {
            "top" : None,
            "bottom" : None,
            "left" : None,
            "right" : None
        }

    def __str__(self):
        return self.sentence

current_node = Story_Node("Once upon a time there was a developer.")
current_node.root = current_node

app = Flask(__name__)

@app.route("/")
@app.route("/restart")
def restart():
    global current_node
    current_node = current_node.root
    return redirect("/index")

@app.route("/add_node", methods=["POST"])
def add_node():
    global current_node

    sentence = request.form.get("sentence")
    node = request.form.get("node")

    if sentence:
        current_node.nodes[node] = Story_Node(sentence, current_node.root)

    return redirect("/index")

@app.route("/index")
@app.route("/index/<node>")
def index(node=None):
    global current_node

    if node and current_node.nodes[node]:
        current_node = current_node.nodes[node]

    return render_template("index.html", current_node=current_node)

if __name__ == "__main__":
    app.run()