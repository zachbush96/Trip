# Trip

## Introduction

"Trip" is a simple yet interesting project that uses Python, HTML, and OpenAI's GPT-3 model to create an interactive visual experience. It uses Flask, a lightweight web framework in Python, to serve a webpage that displays an HTML animation generated by the GPT-3 model. 

The main script, `main.py`, sends a request to OpenAI's GPT-3 model asking it to generate HTML and JavaScript code for an interactive animation. This generated code is then rendered on the webpage served by Flask. The project also has a feature where it can randomly decide to use an HTML file from the local system instead of generating it using the GPT-3 model.

The project currently contains two main files:

1. `main.py`: This is the main script that runs the Flask server and handles the interactions with the GPT-3 model.
2. `index.html`: This is the basic HTML structure that is served by the Flask server. The generated HTML code from the GPT-3 model is inserted into this structure.

## Languages Used

- Python (67.5%)
- HTML (32.5%)

## Installation and Usage

To use this project, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies. The project uses Flask and OpenAI's python client library, so you can install them using pip:

    ```bash
    pip install flask openai
    ```

3. Run the `main.py` script:

    ```bash
    python main.py
    ```

4. The Flask server will start running and you can access the webpage on `localhost:5000`.

Please note that you need to provide your OpenAI API key in the `main.py` file to use the GPT-3 model.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is open source, under the MIT license.