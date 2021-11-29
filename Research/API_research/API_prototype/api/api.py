import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog using a list of dictionaries.
books =[
	{"id": 0,
	"title": "A Fire Upon the Deep",
	"author": "Vernor Vinge",
	"first_sentence": "The coldsleep itself was dreamless.",
	"year_published": "1992"},
	{"id": 1,
	"title": "The One Who Walk Away From Omelas",
	"author": "Ursula K. Le Guin",
	"first_sentence": "With a calmor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.",
	"year_published": "1973"},
	{"id": 2,
	"title": "Dhalgren",
	"author": "Samuel R. Delany",
	"first_sentence": "to wound the autumnal city.",
	"year_published": "1975"}
]


@app.route('/',methods=['GET'])
def home():
	return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

# A route to return all of the availbe entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
	return jsonify(books)	
	
	
# test - http://127.0.0.1:5000/api/v1/resources/books?id=2
@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
	#Check if ID was provided as part of URL
	#If ID provided, assign it to variable
	#If no ID, display an error in browser
	if 'id' in request.args:
		id = int(request.args['id'])
	else:
		return "ERROR: No id field provided. Please specify an ID in the URL"
		
	# Create an empty list of results
	results = []
	
	#Loop through data and match data with requested ID.
	#IDs are unique, but other fields might return many results
	for book in books:
		if book['id'] == id:
			results.append(book)
		
	#Use jsonify to convert from list of dictionaires to JSON
	return jsonify(results)


app.run()
