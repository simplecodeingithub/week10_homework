from flask import Flask, request, url_for

app = Flask(__name__)


@app.route("/about")
def about():
    # url_for() generates a URL to the specified endpoint (function name)
    # This prevents hardcoding URLs and ensures our links remain valid even if routes change
    index_url = url_for('index')  # Generate URL to the index/home page

    # Return a multi-line f-string containing HTML
    # f-strings (formatted string literals) allow embedding Python expressions inside {}
    # Double curly braces {{ }} in the CSS are escaped to render as single braces in output
    return f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>About This Flask App</title>
            <style>
                /* Basic CSS styling for the about page */
                body {{ 
                    font-family: Arial, sans-serif;  /* Set font family */
                    line-height: 1.6;               /* Set line spacing */
                    margin: 0;                      /* Remove default margin */
                    padding: 20px;                  /* Add padding around content */
                }}
                .container {{ 
                    max-width: 800px;               /* Limit content width */
                    margin: 0 auto;                 /* Center the container */
                }}
                h1 {{ 
                    color: #333;                    /* Dark gray heading color */
                }}
                .nav {{ 
                    margin-bottom: 20px;            /* Space after navigation */
                }}
                .nav a {{ 
                    margin-right: 15px;             /* Space between navigation links */
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <!-- Navigation menu -->
                <div class="nav">
                    <!-- Each link is generated dynamically using url_for() -->
                    <!-- This ensures links remain valid even if routes change -->
                    <a href="{index_url}">Home</a>
                    <a href="{url_for('hello_from_flask')}">Hello</a>
                    <a href="{url_for('goodbye_from_flask')}">Goodbye</a>
                </div>

                <!-- Main content section -->
                <h1>About This Flask Application</h1>
                <p>This is a simple Flask web application created as a learning exercise.</p>

                <!-- Features section - lists key components of the application -->
                <h2>Features</h2>
                <ul>
                    <li>Dynamic routing with parameters</li>
                    <li>GET and POST request handling</li>
                    <li>URL generation with url_for</li>
                    <li>Simple HTML templating</li>
                </ul>

                <!-- Technologies section - lists tools and languages used -->
                <h2>Technologies Used</h2>
                <ul>
                    <li>Python</li>
                    <li>Flask</li>
                    <li>HTML</li>
                </ul>

                <!-- Footer information -->
                <p>Created by: Your Name</p>

                <!-- Dynamic date generation -->
                <!-- __import__() is a Python built-in function that imports a module at runtime -->
                <!-- This imports the datetime module, then accesses the datetime class -->
                <!-- .now() gets the current date and time -->
                <!-- .strftime() formats the date as a readable string (Month Day, Year) -->
                <p>Last Updated: {__import__('datetime').datetime.now().strftime('%B %d, %Y')}</p>
            </div>
        </body>
    </html>
    """