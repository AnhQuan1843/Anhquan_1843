from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.railfence.railfence_cipher import RailFenceCipher
from cipher.vigenere.vigenere_cipher import VigenereCipher
from cipher.playfair.playfair_cipher import PlayFairCipher
from cipher.transposition.transposition_cipher import TranspositionCipher

app = Flask(__name__)

# home page
@app.route("/")
def home():
    return render_template("index.html")

# caesar page
@app.route("/caesar")
def caesar():
    return render_template("caesar.html")

# encrypt
@app.route("/encrypt", methods=["POST"])
def caesar_encrypt():

    text = request.form["inputPlainText"]
    key = int(request.form["inputKeyPlain"])

    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)

    return render_template(
        "caesar.html",
        encrypted_text=encrypted_text,
        plain_text=text,
        key=key
    )

# decrypt
@app.route("/decrypt", methods=["POST"])
def caesar_decrypt():

    text = request.form["inputCipherText"]
    key = int(request.form["inputKeyCipher"])

    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)

    return render_template(
        "caesar.html",
        decrypted_text=decrypted_text,
        cipher_text=text,
        key=key
    )

# railfence page
@app.route("/railfence")
def railfence():
    return render_template("railfence.html")

# railfence encrypt
@app.route("/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    text = request.form["inputPlainText"]
    key = int(request.form["inputKeyPlain"])
    
    RailFence = RailFenceCipher()
    encrypted_text = RailFence.rail_fence_encrypt(text, key)
    
    return render_template(
        "railfence.html",
        encrypted_text=encrypted_text,
        plain_text=text,
        key=key
    )

# railfence decrypt
@app.route("/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    text = request.form["inputCipherText"]
    key = int(request.form["inputKeyCipher"])
    
    RailFence = RailFenceCipher()
    decrypted_text = RailFence.rail_fence_decrypt(text, key)
    
    return render_template(
        "railfence.html",
        decrypted_text=decrypted_text,
        cipher_text=text,
        key=key
    )

# vigenere page
@app.route("/vigenere")
def vigenere():
    return render_template("vigenere.html")

# vigenere encrypt
@app.route("/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    text = request.form["inputPlainText"]
    key = request.form["inputKeyPlain"]
    
    vigenere = VigenereCipher()
    encrypted_text = vigenere.vigenere_encrypt(text, key)
    
    return render_template(
        "vigenere.html",
        encrypted_text=encrypted_text,
        plain_text=text,
        key=key
    )

# vigenere decrypt
@app.route("/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    text = request.form["inputCipherText"]
    key = request.form["inputKeyCipher"]
    
    vigenere = VigenereCipher()
    decrypted_text = vigenere.vigenere_decrypt(text, key)
    
    return render_template(
        "vigenere.html",
        decrypted_text=decrypted_text,
        cipher_text=text,
        key=key
    )

# playfair page
@app.route("/playfair")
def playfair():
    return render_template("playfair.html")

# playfair encrypt
@app.route("/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    text = request.form["inputPlainText"]
    key = request.form["inputKeyPlain"]
    
    playfair = PlayFairCipher()
    matrix = playfair.create_playfair_matrix(key)
    encrypted_text = playfair.playfair_encrypt(text, matrix)
    
    return render_template(
        "playfair.html",
        encrypted_text=encrypted_text,
        plain_text=text,
        key=key
    )

# playfair decrypt
@app.route("/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    text = request.form["inputCipherText"]
    key = request.form["inputKeyCipher"]
    
    playfair = PlayFairCipher()
    matrix = playfair.create_playfair_matrix(key)
    decrypted_text = playfair.playfair_decrypt(text, matrix)
    
    return render_template(
        "playfair.html",
        decrypted_text=decrypted_text,
        cipher_text=text,
        key=key
    )

# transposition page
@app.route("/transposition")
def transposition():
    return render_template("transposition.html")

# transposition encrypt
@app.route("/transposition/encrypt", methods=["POST"])
def transposition_encrypt():
    text = request.form["inputPlainText"]
    key = int(request.form["inputKeyPlain"])
    
    transposition = TranspositionCipher()
    encrypted_text = transposition.encrypt(text, key)
    
    return render_template(
        "transposition.html",
        encrypted_text=encrypted_text,
        plain_text=text,
        key=key
    )

# transposition decrypt
@app.route("/transposition/decrypt", methods=["POST"])
def transposition_decrypt():
    text = request.form["inputCipherText"]
    key = int(request.form["inputKeyCipher"])
    
    transposition = TranspositionCipher()
    decrypted_text = transposition.decrypt(text, key)
    
    return render_template(
        "transposition.html",
        decrypted_text=decrypted_text,
        cipher_text=text,
        key=key
    )

# main
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)