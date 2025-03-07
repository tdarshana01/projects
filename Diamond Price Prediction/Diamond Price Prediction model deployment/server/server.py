from docutils.nodes import table
from flask import Flask, request, jsonify, redirect, render_template
import util

app = Flask(__name__)

@app.route('/estimate_price', methods=['POST'])
def estimate_price():
    try:
        carat = request.form['carat']
        depth = request.form['depth']
        table = request.form['table']
        x = request.form['x']
        y = request.form['y']
        z = request.form['z']
        cut = request.form['cut']
        color = request.form['color']
        clarity = request.form['clarity']

        estimated_price = util.estimate_price(carat, cut, color, clarity,depth, table, x, y, z)
        return redirect(f"/api/result?price={estimated_price}")

    except Exception as e:
        print(f'error occurred: {e}')
        return jsonify({"error": "An error occurred while processing the request"}), 500


@app.route('/result')
def result():
    price = request.args.get('price')
    return render_template('result.html',price=price)

if __name__ == '__main__':
    app.run(debug=True)