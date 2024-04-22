# AI Calling Agent using twilio and openai

The AI Calling Agent is an innovative solution designed to automate both inbound and outbound calling processes, currently tailored as a mental health consultant. This project leverages a combination of cutting-edge technologies including Twilio for call handling, OpenAI for intelligent conversation, Pinecone for vector database services, and MongoDB for data persistence.

## Features

- **Inbound and Outbound Calls:** Handles both incoming and outgoing calls efficiently using Twilio.
- **AI-Powered Conversations:** Integrates OpenAI to provide responsive and context-aware interactions.
- **Data Handling:** Utilizes MongoDB for robust data management and Pinecone for querying capabilities.
- **Real-Time Response:** Employs Text-to-Speech (TTS) and Speech-to-Text (STT) for real-time communication.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequsit
Fill the env and config file.

### Installing

A step by step series of examples that tell you how to get a development environment running:

1. Clone the repository:
   ```bash
   git clone https://github.com/revolutionarybukhari/ai-calling-agent.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ai-calling-agent
   ```
3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```

## Usage

After starting the server, the application will be available on `http://localhost:5000/`. Use the following endpoints to interact with the AI calling agent:

- **GET /** - Test the connection and retrieve API status.
- **POST /voice** - Handle incoming calls.
- **GET /make_call?phone_number=+1234567890** - Initiate an outbound call to the specified number.
- **POST /handle_speech** - Process user speech from an ongoing call.

## Project Structure

```
/ai-calling-agent
│
├── app.py                # Flask application entry point
├── /modules              # Modular functionalities
│   ├── agent_tools.py
│   ├── chatbot.py
│   ├── mongodb.py
│   ├── sender.py
│   ├── tts.py
│   └── twilio_api.py
└── /static               # Static files directory
```

## Contributing

We welcome contributions from the community. If you wish to contribute to this project, please fork the repository and submit a pull request.

## Author

- **Syed Husnain Haider Bukhari** - *AI Automation Expert & Data Scientist* - [LinkedIn](https://www.linkedin.com/in/syed-husnain-haider-bukhari/) | [Instagram](https://www.instagram.com/revolutionarybukhari/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Thanks to Twilio, OpenAI, Pinecone, and MongoDB for providing the technologies that power this project.
