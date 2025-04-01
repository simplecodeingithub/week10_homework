# import Flask class from the flask module,This is the main class for creating a Flask application.
from flask import Flask, request, Response, url_for

# create an instance of Flask class and assign it to a variable 'app' - Instantiating the Flask application
app = Flask(__name__)

# Decorator used to map the URL '/get/text' to a specific function,the URL ('/') is associated with the root URL.
# whenever a user visits the URL '/get/text', the function 'get_text' is executed.
@app.route('/get/text')
def get_text():
    # Create and returns a Response object with custom message and MIME type.
    return Response("Hello from flask using explict Response object", mimetype='text/plain')


# Defining a route that accepts two URL parameters: 'name' and 'age'
# url_for is for generating URLs for other routes dynamically.
@app.route('/index/<string:name>/<int:age>')
def index(name, age):
    url = url_for('get_text')
    return """
    <!DOCTYPE>
    <html>
        <head>
            <title>Simple - Flask routes</title>
        </head>
        <body>
            <h1>Name page</h1>
            <p>Hello {}!</p>
            <p>You are {} year(s) old.</p>
            <hr>
          <a href="{}">Welcome</a>
        </body>
    </html>
    """.format(name, age, url)


# Decorator used to map the URL '/<string:name>' to a specific(home) function,the URL ('/') is associated with the root URL.
# Home Page Route-This route takes the 'name' parameter from the URL.
@app.route('/<string:name>')
def home(name):
    # url_for is used to dynamically generate the URLs for the 'about' and 'contact' pages and with the 'name' parameter.
    about_url = url_for('about', name=name)
    contact_url = url_for('contact', name=name)

    # Dynamically link to the main_style.css file in the static folder
    css_url = url_for('static', filename='Stylesheets/main_style.css')

    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Home Page</title>
             <!-- Add a link to BS CSS -->
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
            <link rel="stylesheet" href="{}" type="text/css">
        </head>
       <body>
            <div class="container">
                <h1>Welcome to My Flask Application</h1>
                <h2>Hello, {}!</h2>
                <p>This is a simple Flask web application.</p>

                <h3>Features:</h3>
                <ul>
                    <li>Dynamic routing with Flask</li>
                    <li>Styled with CSS</li>
                    <li>Supports GET and POST requests</li>
                </ul>

                <h3>Steps to Use:</h3>
                <ol>
                    <li>Enter your name in the URL</li>
                    <li>Navigate through pages</li>
                    <li>Try sending a POST request</li>
                </ol>
              <hr>
            <p><a href="{}">About</a> | <a href="{}">Contact</a></p> 
        </div>
            <footer class="footer">Powered by Flask</footer>
            
                <!-- Bootstrap JS -->
            <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js" crossorigin="anonymous"></script>
        </body>
    </html>
    """.format(css_url, name, about_url, contact_url)


# About Page Route
@app.route('/about/<string:name>')
def about(name):
    contact_url = url_for('contact', name=name)
    home_url = url_for('home', name=name)

    # Dynamically link to the main_style.css file in the static folder
    css_url = url_for('static', filename='Stylesheets/main_style.css')

    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>About Page</title>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
            <link rel="stylesheet" href="{}" type="text/css">
        </head>
        <div class="container">
                <h1>About Me</h1>
                <h2>Hello, {}!</h2>
                <p>This is the About page of our Flask application.</p>
                
                <h3>What We Do:</h3>
                <ul>
                    <li>Building dynamic web applications</li>
                    <li>Using Flask and Python</li>
                    <li>Integrating styles with CSS</li>
                </ul>

                <p>Need to Contact us? Visit our <a href="{}">Contact Page</a>.</p>
                <hr>
                <p>Back to <a href="{}">Home</a></p>
            </div>
            <footer class="footer">Powered by Flask</footer>
             <!-- Bootstrap JS -->
            <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js" crossorigin="anonymous"></script>
        </body>
    </html>
    """.format(css_url, name, contact_url, home_url)


# Contact Page Route -This route takes the 'name' parameter and handles both GET and POST requests.
@app.route('/contact/<string:name>', methods=['GET', 'POST'])
def contact(name):
    home_url = url_for('home', name=name)
    about_url = url_for('about', name=name)
    # Dynamically link to the main_style.css file in the static folder
    css_url = url_for('static', filename='Stylesheets/main_style.css')

    if request.method == 'POST':
        data_sent = request.data.decode('utf-8')

        if not data_sent:
            return "No data received in the POST request.", 400

        return f"POST request received. The data you sent was: {data_sent}"

    # if the method is GET, simple returns an HTML contact page
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Contact Page</title>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
            <link rel="stylesheet" href="{}" type="text/css">
        </head>
        <body>
            <div class="container">
                <h1>Contact Us</h1>
                <h2>Hi, {}!</h2>
                <p>Feel free to reach out for any queries or support.</p>
                <h3>Contact Details:</h3>
                <ul>
                    <li>Email: example@gmail.com</li>
                    <li>Phone: +44 9012345678</li>
                    <li>Location: London, UK</li>
                </ul>
                <hr>
                <p><a href="{}">Home</a> | <a href="{}">About</a></p>
            </div>
            <footer class="footer">Powered by Flask</footer>
             <!-- Bootstrap JS -->
            <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js" crossorigin="anonymous"></script>
        </body>
    </html>
    """.format(css_url, name, home_url,about_url)


# if the script is invoked directly (rather than being imported),run the flask app.
if __name__ == '__main__':
    app.run(debug=True)



