# Chatbot Application

This is a simple chatbot application built using Flask. The application allows users to interact with an LLM through a chatbot interface. You must install Ollama and your desired LLM model beforehand.

- ## Ollama: [Ollama Download](https://ollama.com/download)

- ## Deepseek-R1: (Choose a model according to your system specs) Simply Run command

```sh
ollama pull <name of llm model>
```

## Project Structure

- `app.py`: The main Flask application file.
- `requirements.txt`: A list of dependencies required for the project.
- `static/styles.css`: The CSS file for styling the web interface.
- `templates/index.html`: The HTML template for the web interface.

## Installation

1. Clone the repository:

    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

1. Start the Flask application:

    ```sh
    python app.py
    ```

2. Open your web browser and go to `http://localhost:5000`.

## Usage

- The root route (`/`) renders the main chat interface.
- The chat route (`/chat`) handles POST requests with user messages and returns responses from the chatbot.

## Files

### [app.py](http://_vscodecontentref_/4)

This file contains the main Flask application. It defines two routes:

- `/`: Renders the [index.html](http://_vscodecontentref_/5) template.
- `/chat`: Handles POST requests with user messages and interacts with an external API to generate chatbot responses.

### [requirements.txt](http://_vscodecontentref_/6)

This file lists all the dependencies required for the project.

### [styles.css](http://_vscodecontentref_/7)

This file contains the CSS styles for the web interface.

### [index.html](http://_vscodecontentref_/8)

This file contains the HTML structure for the chat interface.

## Example

To send a message to the chatbot, type your message in the input field and click the "Send" button. The chatbot's response will be displayed in the chatbox.

## Debugging

Debugging lines are included in both the frontend and backend to help trace the flow of data:

- In [app.py](http://_vscodecontentref_/9), the backend response is printed before being sent to the frontend.
- In [index.html](http://_vscodecontentref_/10), the frontend logs the received data to the console.
