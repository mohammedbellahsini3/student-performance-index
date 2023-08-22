from flask import Flask, render_template, request

app = Flask(__name__,template_folder='template')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        study_hours = float(request.form.get('study_hours'))
        previous_scores = float(request.form.get('previous_scores'))
        extracurricular_activities = int(request.form.get('extracurricular_activities'))
        sleep_hours = float(request.form.get('sleep_hours'))
        sample_question_papers_practiced = int(request.form.get('sample_question_papers_practiced'))

        # Perform your prediction logic here based on the input values

        # For demonstration purposes, let's assume the prediction is calculated as a sum of input values
        prediction = study_hours + previous_scores + extracurricular_activities + sleep_hours + sample_question_papers_practiced

        return render_template('index.html', prediction=prediction)

    return render_template('index.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)

