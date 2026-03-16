class PlayFairCipher:

    def create_playfair_matrix(self, key):
        key = key.upper().replace("J", "I")
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

        matrix = []
        used = set()

        for char in key:
            if char not in used and char in alphabet:
                used.add(char)
                matrix.append(char)

        for char in alphabet:
            if char not in used:
                used.add(char)
                matrix.append(char)

        playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
        return playfair_matrix


    def find_letter_coords(self, matrix, letter):
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == letter:
                    return row, col


    def playfair_encrypt(self, plain_text, matrix):
        plain_text = plain_text.upper().replace("J", "I")
        encrypted_text = ""

        i = 0
        while i < len(plain_text):
            a = plain_text[i]

            if i + 1 < len(plain_text):
                b = plain_text[i+1]
            else:
                b = "X"

            if a == b:
                b = "X"
                i += 1
            else:
                i += 2

            row1, col1 = self.find_letter_coords(matrix, a)
            row2, col2 = self.find_letter_coords(matrix, b)

            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5]
                encrypted_text += matrix[row2][(col2 + 1) % 5]

            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1]
                encrypted_text += matrix[(row2 + 1) % 5][col2]

            else:
                encrypted_text += matrix[row1][col2]
                encrypted_text += matrix[row2][col1]

        return encrypted_text


    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""

        for i in range(0, len(cipher_text), 2):
            a = cipher_text[i]
            b = cipher_text[i+1]

            row1, col1 = self.find_letter_coords(matrix, a)
            row2, col2 = self.find_letter_coords(matrix, b)

            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5]
                decrypted_text += matrix[row2][(col2 - 1) % 5]

            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1]
                decrypted_text += matrix[(row2 - 1) % 5][col2]

            else:
                decrypted_text += matrix[row1][col2]
                decrypted_text += matrix[row2][col1]

        return decrypted_text