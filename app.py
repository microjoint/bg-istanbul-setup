from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_grid', methods=['POST'])
def generate_grid():
    if request.method == 'POST':
        if request.form['action'] == 'standard':
            grid = generate_standard_grid()
            return jsonify({'grid': grid})

def generate_standard_grid():
    import random

def generate_standard_grid():
    while True:
        # Create an empty 4x4 grid
        grid = [[0 for _ in range(4)] for _ in range(4)]

        # Randomly shuffle the numbers from 1 to 16
        numbers = list(range(1, 17))
        random.shuffle(numbers)

        # Place the shuffled numbers in the grid
        for i in range(4):
            for j in range(4):
                grid[i][j] = numbers.pop()

        # Find the positions of 8 and 9
        pos_8 = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 8][0]
        pos_9 = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 9][0]

        # Find the position of 7
        pos_7 = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 7][0]

        # Calculate Manhattan distance between 8 and 9
        distance = abs(pos_8[0] - pos_9[0]) + abs(pos_8[1] - pos_9[1])

        # Check if 7 is in an inner tile and distance between 8 and 9 > 2
        if (1 <= pos_7[0] <= 2) and (1 <= pos_7[1] <= 2) and (distance > 2):
            return grid


if __name__ == '__main__':
    app.run(debug=True)

