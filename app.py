from flask import Flask, request, jsonify

import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

notes = []

@app.route("/")
def home():
    logging.info("Home route hit")
    return 1/0
 
# POST new note
@app.route("/notes", methods=["POST"])
def add_note():
    data = request.json

    note = {
        "id": len(notes),
        "text": data.get("text")
    }

    notes.append(note)
    return jsonify({"message": "note added", "note": note})

# DELETE note
@app.route("/delete/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            return jsonify({"message": "deleted"})
    
    return jsonify({"message": "not found"}), 404

@app.errorhandler(500)
def internal_error(e):
    return jsonify({"error": "internal server error"}), 500


app.run(host="0.0.0.0", port=5000)
