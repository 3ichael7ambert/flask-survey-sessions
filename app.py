from flask import Flask, request, render_template, redirect, flash
from surveys import satisfaction_survey as survey

app = Flask(__name__)

@app.route("/")
def show_survey_start():
    """Select a survey."""
    return render_template("begin_survey.html", survey=survey)


@app.route("/begin", methods=["POST"])
def start_survey():
    """Clear the session of responses."""
    return redirect("/questions/0")


@app.route("/answer", methods=["POST"])
def handle_question():
    """Save response and redirect to next question."""
    # get the response choice
    choice = request.form['answer']
    # TODO: add this response to the list of responses


    if (len(responses) == len(survey.questions)):
        # They've answered all the questions! Thank them.
        return redirect("/complete")
    else:
        return redirect(f"/questions/{len(responses)}")


@app.route("/questions/<int:qid>")
def show_question(qid):
    """Display current question."""
    # TODO: check that we're allowed to be here

    question = survey.questions[qid]
    return render_template(
        "question.html", question_num=qid, question=question)


@app.route("/complete")
def complete():
    """Survey complete. Show completion page."""
    return render_template("complete.html")
