
try:
    from flask import Flask, render_template, request  # pyright: ignore[reportMissingImports]
except ModuleNotFoundError as e:
    raise ModuleNotFoundError("Flask module is not installed. Install it with 'pip install flask'.") from e
from datetime import datetime

app = Flask(__name__)

meal_history = []

@app.route("/", methods=["GET", "POST"])
def index():
    total_calories = sum(meal["calories"] for meal in meal_history)
    total_protein = sum(meal["protein"] for meal in meal_history)
    total_carbs = sum(meal["carbs"] for meal in meal_history)
    total_fats = sum(meal["fats"] for meal in meal_history)

    if request.method == "POST":
        meal = {
            "name": request.form["name"],
            "calories": int(request.form["calories"]),
            "protein": float(request.form["protein"]),
            "carbs": float(request.form["carbs"]),
            "fats": float(request.form["fats"]),
            "time": datetime.now().strftime("%H:%M:%S")
        }

        meal_history.append(meal)

        total_calories += meal["calories"]
        total_protein += meal["protein"]
        total_carbs += meal["carbs"]
        total_fats += meal["fats"]

    return render_template(
        "index.html",
        meals=meal_history,
        total_calories=total_calories,
        total_protein=round(total_protein, 2),
        total_carbs=round(total_carbs, 2),
        total_fats=round(total_fats, 2)
    )

if __name__ == "__main__":
    app.run(debug=True)
