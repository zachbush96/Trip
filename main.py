import json
import random
from flask import Flask, render_template
import openai
from bs4 import BeautifulSoup
import os

openai.api_key = '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'

app = Flask(__name__)


def is_valid_html(html_string):
	try:
		soup = BeautifulSoup(html_string, 'html.parser')
		# Also make sure there is a style tag and JavaScript code
		if soup.find('script') is None:
			print("Invalid 1")
			return False
		return True
	except Exception:
		print("Invalid 2")
		return False


# Function that hits the OpenAI endpoint and returns the response
def get_code(futureFileNumber):
	# 50/50 chance of using OpenAI or the local file
	if random.randint(0, 1) == 0:
		print("Using local file")
		try:
			file_list = os.listdir("GeneratedSites")
			print("File_List: " + str(file_list))
			if len(file_list) > 0:
				# Pick a random file from the list of files
				file_path = os.path.join("GeneratedSites", random.choice(file_list))
        #file_path = os.path.join("GeneratedSites", str(len(file_list) - 1) + ".html")
				print("File_Path: " + file_path)
				with open(file_path, "r") as outfile:
					return outfile.read()
			else:
				print("No local files available")
				return "No local files available"
		except Exception:
			print("Error reading local file")
			return "Error reading local file"
	else:
		print("Using OpenAI")
		print("Sending API request")
		response = openai.ChatCompletion.create(
			model="gpt-3.5-turbo",
			messages=[{
				"role": "user",
				"content": "Please use HTML, JavaScript, and animie.js to create a fullscreen interactive animation / visual experience. Please include interesting morphing shapes and a lot of detail and complex patterns. All movement should be subtle and happen slowly. All colors should change based on a gradient. Make sure there is movement in this animation. Please only output HTML. No preface or explanation. Begin with <html>"
			}]
		)
		ReturnedHTML = response.choices[0].message.content.strip()
		# Save the HTML to a local HTML file (randomly named) in a folder called GeneratedSites
		file_name = futureFileNumber + ".html"
		file_path = os.path.join("GeneratedSites", file_name)

		with open(file_path, "w") as outfile:
			outfile.write(ReturnedHTML)
		print("API response saved")
		return ReturnedHTML

#Endpoint that deletes a file from the GeneratedSites folder (passed in as a parameter)
@app.route('/delete/<file_name>')
def delete_file(file_name):
    try:
        file_path = os.path.join("GeneratedSites", file_name+".html")
			
        os.remove(file_path)
        return "File deleted"
    except Exception:
        return "Error deleting file"


@app.route('/')
def generate_html():
	print("Endpoint hit")
	while True:
		randomNumber = str(random.randint(0, 10000))
		generated_text = get_code(randomNumber)
		print(generated_text[:15])
		soup = BeautifulSoup(generated_text, 'html.parser')  # parse the HTML
		generated_html = str(soup)  # convert the HTML to a string
		if is_valid_html(generated_html):
			return render_template('index.html', generated_html=generated_html, file_name=randomNumber)
		else:
			print("Trying again... " + generated_text[:275])
			soup = BeautifulSoup(generated_text, 'html.parser')  # parse the HTML
			generated_html = str(soup)  # convert the HTML to a string
			if is_valid_html(generated_html):
				return render_template('index.html', generated_html=generated_html, file_name=randomNumber)
			else:
				return "Invalid HTML generated twice. Please refresh"


if __name__ == '__main__':
	app.run(host='0.0.0.0')
