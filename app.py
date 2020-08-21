####STANDARD CODE
# import necessary libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__)
#########

# create route that renders index.html template
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/main")
def main():
    return render_template('main.html')

@app.route("/portfolio-work")
def portfolio_work():
    return render_template('portfolio-work.html')

@app.route("/services")
def services():
    return render_template('services.html')

@app.route("/single-blog")
def single_blog():
    return render_template('single-blog.html')

@app.route("/work_details")
def work_details():
    return render_template('work_details.html')

####STANDARD CODE
if __name__ == "__main__":
    app.run(debug=True)
#########