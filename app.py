from flask import Flask, request, jsonify

app = Flask(__name__)

Book = [{"id": 1, "name": "English", "subject": "yes"},
        {"id": 1, "name": "Math", "subject": "No"}]

@app.get("/Book")
def get_Book():
    
    book_id = request.args.get("id", type=int)
    name = request.args.get("name")
    
    filtered_books = Book
    if book_id is not None:
        filtered_books = [book for book in filtered_books if book["id"] == book_id]
        
    
    return jsonify(filtered_books)

@app.post("/Book")
def add_Book():
    data = request.json
    new_Book = {"id": len(Book)+1, "name": data["name"], "subject": data["subject"]}
    Book.append(new_Book)
    return jsonify(new_Book)

@app.delete("/Book/<int:book_id>")
def delete_Book(book_id):
    global Book
    original_length = len(Book)
    Book = [book for book in Book if book["id"] != book_id]
    if len(Book) == original_length:
        return jsonify({"error": "not found"}), 404
    return jsonify({"message": f"succesfully delted"}, 200)

@app.put("/Book/<int:book_id>")
def update_Book(book_id):
    data = request.json
    for book in Book:
        if book["id"] == book_id:
            
            book["name"] = data.get("name", book["name"])
            book["subject"] = data.get("subject", book["subject"])
            
            return jsonify({"message": f"{book_id} is updated", "book": book}), 200
    
    return jsonify({"error": "not found"}), 404


if (__name__)== "__main__":
    app.run(debug=True)