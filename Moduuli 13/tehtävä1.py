from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

@app.route('/alkuluku/<int:number>')
def check_prime(number):
    is_prime_result = is_prime(number)
    response = {"Number": number, "isPrime": is_prime_result}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
