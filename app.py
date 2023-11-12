from flask import Flask, request, render_template, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def macro_calculator():
    logo_url = url_for('static', filename='images/BG_MTN_LOGO_WHITE-256w.png')
    brand_logo_url = url_for('static', filename='images/BG_MTN_LOGO_horizontal-blak-words-NOLLC.png')

    if request.method == 'POST':
        weight = float(request.form.get('weight'))
        fat_percent = float(request.form.get('fat_percent'))

        lean_body_mass = weight - ((fat_percent / 100) * weight)

        macros = {
            "trying to get lean": {"protein": 1, "carb": 1.75, "fat": 0.3},
            "trying to maintain weight": {"protein": 1, "carb": 2, "fat": 0.5},
            "trying to bulk up": {"protein": 1.2, "carb": 2.75, "fat": 0.75},
        }

        caloric_indices = {"protein": 4, "carb": 4, "fat": 9}

        results = {}

        for level, ratio in macros.items():
            intake = {macronutrient: int(lean_body_mass * value) for macronutrient, value in ratio.items()}
            calories = {macronutrient: int(value * caloric_indices[macronutrient]) for macronutrient, value in
                        intake.items()}
            total_calories = sum(calories.values())
            results[level] = {
                "intake": intake,
                "calories": calories,
                "total_calories": total_calories,
            }

        return render_template(
            'results.html',
            results=results,
            logo_url=logo_url,
            brand_logo_url=brand_logo_url,
            weight=weight,
            fat_percent=fat_percent
        )

    return render_template(
        'index.html',
        logo_url=logo_url,
        brand_logo_url=brand_logo_url
    )


if __name__ == "__main__":
    app.run()

