## HW 1
## SI 364 W18
## 1000 points

## Gabriella Gazdecki
## Section 003
## 14 January 2018
#################################

## List below here, in a comment/comments, the people you worked with on this assignment AND any resources you used to find code (50 point deduction for not doing so). If none, write "None".

##None

## [PROBLEM 1] - 150 points
## Below is code for one of the simplest possible Flask applications. Edit the code so that once you run this application locally and go to the URL 'http://localhost:5000/class', you see a page that says "Welcome to SI 364!"
import requests
import json
from flask import Flask, request
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_to_you():
    return 'Hello!'

@app.route('/class')
def welcome_class():
	return "<h1>Welcome to SI 364!</h1>"

@app.route('/movie/<movieName>')
def movie_search(movieName):
	base_url = 'https://itunes.apple.com/search?entity=movie&term='

	result = requests.get(base_url+movieName).text
	return result

@app.route('/question')
def fav_number():

	s = """<!DOCTYPE html>
<html>
<body>
<form action = "/result" method = "post">
  Enter your favorite number:<br>
  <input type="text" name="favNum" value="">
  <br>
  <input type="submit" value="Submit">
</form>
</body>
</html>"""
	return s

@app.route('/result', methods = ['POST', 'GET'])
def double_fav_number():

    if request.method == 'POST':
      number = request.form['favNum']

    double = int(number)*2
    return '<h>Double your favorite number is {}</h1>'.format(double)

@app.route('/problem4form', methods=["GET","POST"])
def problem_four():
    form = """<!DOCTYPE html>
<html>
<body>
<form action = "/problem4form" method = "GET">
  Thesaurus:<br>
  <input type="text" name="user_term" value="Enter your word here">
  <br>
  <input type="checkbox" name="synonym" value="Syn"> Show me the synonyms!<br>
  <input type="checkbox" name="antonym" value="Ant"> Show me the antonyms!<br>
  <input type="submit" value="Submit">
</form>
</body>
</html>"""
    if request.method == "GET":

        data = request.args.to_dict(True)
        user_input = ''
        synonyms = '<br>'
        antonyms = '<br>'
        if 'user_term' in data:
            user_input = data['user_term']

        if 'antonym' in data:
            ant_url = "https://api.datamuse.com/words?rel_ant="
            ant_resp = requests.get(ant_url+user_input)

            ant_dict = json.loads(ant_resp.text)

            for a in ant_dict:
                antonym = a["word"]
                antonyms += antonym
                antonyms += '<br>'
            if antonyms == '<br>':
                antonyms += 'No antonyms found'

        if 'synonym' in data:
            syn_url = "https://api.datamuse.com/words?rel_syn="
            syn_resp = requests.get(syn_url+user_input)

            syn_dict = json.loads(syn_resp.text)

            for s in syn_dict:
                synonym = s["word"]
                synonyms += synonym
                synonyms += '<br>'

    return form + "<br><br> The synonyms for {} are: {} <br><br> The antonyms for {} are: {}".format(user_input, synonyms, user_input, antonyms)


if __name__ == '__main__':
    app.run()


## [PROBLEM 2] - 250 points
## Edit the code chunk above again so that if you go to the URL 'http://localhost:5000/movie/<name-of-movie-here-one-word>' you see a big dictionary of data on the page. For example, if you go to the URL 'http://localhost:5000/movie/ratatouille', you should see something like the data shown in the included file sample_ratatouille_data.txt, which contains data about the animated movie Ratatouille. However, if you go to the url http://localhost:5000/movie/titanic, you should get different data, and if you go to the url 'http://localhost:5000/movie/dsagdsgskfsl' for example, you should see data on the page that looks like this:

# {
#  "resultCount":0,
#  "results": []
# }


## You should use the iTunes Search API to get that data.
## Docs for that API are here: https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/
## Of course, you'll also need the requests library and knowledge of how to make a request to a REST API for data.

## Run the app locally (repeatedly) and try these URLs out!

## [PROBLEM 3] - 250 points

## Edit the above Flask application code so that if you run the application locally and got to the URL http://localhost:5000/question, you see a form that asks you to enter your favorite number.
## Once you enter a number and submit it to the form, you should then see a web page that says "Double your favorite number is <number>". For example, if you enter 2 into the form, you should then see a page that says "Double your favorite number is 4". Careful about types in your Python code!
## You can assume a user will always enter a number only.


## [PROBLEM 4] - 350 points

## Come up with your own interactive data exchange that you want to see happen dynamically in the Flask application, and build it into the above code for a Flask application, following a few requirements.

## You should create a form that appears at the route: http://localhost:5000/problem4form

## Submitting the form should result in your seeing the results of the form on the same page.

## What you do for this problem should:
# - not be an exact repeat of something you did in class
# - must include an HTML form with checkboxes and text entry
# - should, on submission of data to the HTML form, show new data that depends upon the data entered into the submission form and is readable by humans (more readable than e.g. the data you got in Problem 2 of this HW). The new data should be gathered via API request or BeautifulSoup.

# You should feel free to be creative and do something fun for you --
# And use this opportunity to make sure you understand these steps: if you think going slowly and carefully writing out steps for a simpler data transaction, like Problem 1, will help build your understanding, you should definitely try that!

# You can assume that a user will give you the type of input/response you expect in your form; you do not need to handle errors or user confusion. (e.g. if your form asks for a name, you can assume a user will type a reasonable name; if your form asks for a number, you can assume a user will type a reasonable number; if your form asks the user to select a checkbox, you can assume they will do that.)

# Points will be assigned for each specification in the problem.
