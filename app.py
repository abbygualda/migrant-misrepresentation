
from flask import Flask, render_template

app = Flask(__name__)


# this routes us to our home page 
@app.route("/", methods=['GET'])
def hello():
  return render_template('home.html', message='Migrant Misrepresentation')




if __name__ == "__main__":
  app.run()
