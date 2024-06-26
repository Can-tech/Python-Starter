from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import csv
from wtforms import ValidationError
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)

def validate_map_link(form, field):
    # Regular expression for a Google Maps link
    pattern = r'^https:\/\/www\.google\.com\/maps\/place\/.*$'
    if not re.match(pattern, field.data):
        raise ValidationError('Invalid map link.')


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired(), validate_map_link])
    open = StringField('Open time', validators=[DataRequired()])
    close = StringField('Close time', validators=[DataRequired()])
    coffee = StringField('Coffee rate', validators=[DataRequired()])
    wifi = StringField('Wifi rate', validators=[DataRequired()])
    power = StringField('Power Rate', validators=[DataRequired()])

    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET","POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        form_data=[]
        for field in form:
            form_data = [field.data for field in form if field.name != 'csrf_token']
        with open('cafe-data.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            # Add the new row
            writer.writerow(form_data)

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
