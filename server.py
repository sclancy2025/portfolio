from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a', newline='') as database:
        file = database.write(f"{data['email']}, {data['subject']}, {data['message']}\n")

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])     


@app.route('/submit_form', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        try: 
            data = request.form.to_dict()
            write_to_csv(data)   
            return redirect("/thankyou.html")
        except:
            return "Did not save to database"
    
    else: 
        return "Something went wrong. Try again!"
    
# @app.route("/project.html")
# def project():
#     return render_template("project.html")

# @app.route("/index.html")
# def index():
#     return render_template("index.html")

# @app.route("/components.html")
# def components():
#     return render_template("components.html")


# @app.route('/<username>/<int:post_id>')
# def hello_world(username=None, post_id=None):
#     return render_template("index.html", name=username, post_id=post_id)


# @app.route("/user/<username>")
# def user(username):
#     return f"Hello {username}"


# @app.route("/about")
# def about():
#     return render_template("about.html")

# # @app.route("/favicon.ico")
# # def blog():
# #     return "<p>This is my blog</p>"

# @app.route("/blog/2020/dog")
# def blog2():
#     return "<p>This is my dog</p>"