from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bmi/hitung', methods=["POST"])
def user():
    tinggi=float(request.form.get('tinggi'))
    berat=float(request.form.get('berat'))

    bmi = berat/(tinggi/100)**2
    if bmi <= 18.4:
        ket = "anda kurus"
    elif bmi <= 25:
        ket = "anda normal"
    elif bmi <= 40:
        ket = "anda berlebihan"
    else:
        ket = "anda bahaya"
    data = {'ket' : ket}
    return jsonify(data)
if __name__ == '__main__':
    app.run(debug=True, port=4000)