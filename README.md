# 🎙️ Voice AI Assistant

> An intelligent voice-powered assistant that listens, understands, and acts on your commands using AI-powered workflow automation.

## 🎥 Demo Video

https://github.com/Hamza-ali1223/ABIS-Project/releases/download/release/demo.mp4

*Watch the assistant in action - creating calendar events, drafting emails, and engaging in natural conversation!*

## 📖 Overview

This Voice AI Assistant is a complete voice-to-voice automation system that combines speech recognition, artificial intelligence, and workflow automation to create a seamless personal assistant experience.

**Key Capabilities:**
- 🎤 **Voice Command Recognition** - Speak naturally and get instant transcription
- 📅 **Calendar Management** - Create reminders and schedule events with voice
- ✉️ **Email Drafting** - Compose Gmail drafts hands-free
- 💬 **Conversational AI** - Chat naturally with AI-powered responses
- 🔊 **Voice Feedback** - Hear confirmation and responses out loud
- 🔄 **Continuous Listening** - Always ready for your next command

## 🏗️ Architecture

```
┌─────────────┐
│   User      │ Speaks Command
│  (Voice)    │
└──────┬──────┘
       │
       ▼
┌─────────────────────────┐
│   stt.py                │  Records audio & converts
│   (Speech-to-Text)      │  speech to text
└──────┬──────────────────┘
       │
       ▼
┌─────────────────────────┐
│   request.py            │  Sends text to n8n
│   (Main Controller)     │  webhook endpoint
└──────┬──────────────────┘
       │
       ▼
┌─────────────────────────────────────────────────┐
│   n8n Workflow (Speech Agent.json)              │
│   ┌───────────────────────────────────────┐     │
│   │  Google Gemini AI                     │     │
│   │  Classifies intent:                   │     │
│   │  - "reminder" → Calendar Event        │     │
│   │  - "draft email" → Gmail Draft        │     │
│   │  - "chat" → Conversational Response   │     │
│   └───────────┬───────────────────────────┘     │
│               │                                  │
│       ┌───────┴────────┬─────────────┐          │
│       ▼                ▼             ▼          │
│  ┌─────────┐    ┌──────────┐   ┌────────┐      │
│  │Calendar │    │  Gmail   │   │  Chat  │      │
│  │ Event   │    │  Draft   │   │Response│      │
│  └────┬────┘    └────┬─────┘   └───┬────┘      │
│       │              │             │           │
│       └──────────────┴─────────────┘           │
│                      │                          │
│              ┌───────▼────────┐                 │
│              │  Code Nodes    │  Format response│
│              │  HTTP Requests │  Send to TTS    │
│              └───────┬────────┘                 │
└──────────────────────┼──────────────────────────┘
                       │
                       ▼
            ┌─────────────────────┐
            │  tts_service.py     │  Converts text to
            │  (Text-to-Speech)   │  speech & plays audio
            └─────────────────────┘
                       │
                       ▼
                  🔊 Audio Output
```

### Component Breakdown:

1. **Speech-to-Text Module** (`stt.py`) - Captures microphone input and transcribes speech
2. **Request Handler** (`request.py`) - Orchestrates the voice loop and API communication
3. **n8n Workflow Engine** - Processes intent with AI and routes to appropriate services
4. **Text-to-Speech Service** (`tts_service.py`) - FastAPI server that speaks responses

## 🛠️ Tech Stack

| Category | Technologies |
|----------|-------------|
| **Languages** | Python 3.11+ |
| **Frameworks** | FastAPI, n8n |
| **Speech** | `sounddevice`, `wavio`, `speech_recognition`, `pyttsx3` |
| **AI** | Google Gemini 2.5 Flash Lite |
| **APIs** | Google Calendar API, Gmail API |
| **HTTP** | `requests`, `uvicorn` |
| **Infrastructure** | Docker (n8n) |

## 📁 Project Structure

```
ABIS Project/
├── stt.py                  # Speech-to-Text module (audio recording & transcription)
├── request.py              # Main controller (voice loop & webhook communication)
├── tts_service.py          # Text-to-Speech FastAPI service
├── Speech Agent.json       # n8n workflow configuration
├── demo.mp4               # Demonstration video
└── README.md              # Project documentation
```

### File Descriptions:

- **`stt.py`** - Handles microphone recording, speech recognition using Google's API, and audio file management
- **`request.py`** - Infinite loop that captures voice commands and sends them to the n8n webhook
- **`tts_service.py`** - FastAPI server running on port 8000 that converts text responses to speech
- **`Speech Agent.json`** - Complete n8n workflow with AI processing, routing logic, and service integrations

## ⚙️ How It Works

### Step-by-Step Flow:

1. **🎤 Voice Input** - User speaks a command (5-second recording window)
2. **📝 Transcription** - Audio is converted to text using Google Speech Recognition
3. **🔗 Webhook Call** - Text is sent to n8n webhook at `http://localhost:5678/webhook/voice`
4. **🤖 AI Processing** - Google Gemini AI analyzes the intent and classifies it as:
   - **Reminder** - Creates Google Calendar event
   - **Draft Email** - Creates Gmail draft
   - **Chat** - Generates conversational response
5. **✅ Action Execution** - Appropriate service (Calendar/Gmail/Chat) processes the request
6. **💬 Response Generation** - Success message or AI response is formatted
7. **🔊 Voice Output** - Response is sent to TTS service and spoken aloud
8. **🔄 Loop Continues** - System waits for next voice command

### Example Use Cases:

**Calendar Reminder:**
- 🗣️ *"Remind me to call John at 3 PM tomorrow"*
- ✅ Creates calendar event
- 🔊 *"I've created a reminder to call John at 3 PM tomorrow"*

**Email Draft:**
- 🗣️ *"Draft an email to Sarah about the project meeting"*
- ✅ Creates Gmail draft
- 🔊 *"I've drafted an email to Sarah about the project meeting"*

**Conversation:**
- 🗣️ *"What's the weather like today?"*
- ✅ AI generates response
- 🔊 *"I don't have real-time weather data, but you can check your local weather app!"*

## 📋 Prerequisites

Before setting up the project, ensure you have:

- ✅ **Python 3.8+** installed
- ✅ **Docker & Docker Compose** installed
- ✅ **Google Cloud Account** with Calendar & Gmail APIs enabled
- ✅ **Google Gemini API Key**
- ✅ **Microphone** and **speakers** connected
- ✅ **Internet connection** for speech recognition and AI APIs

## 🚀 Installation & Setup

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
cd "ABIS Project"
```

### Step 2: Install Python Dependencies

```bash
pip install fastapi uvicorn pyttsx3 sounddevice wavio speechrecognition requests pydantic
```

### Step 3: Set Up n8n with Docker

```bash
docker run -d --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n
```

Access n8n at: `http://localhost:5678`

### Step 4: Import n8n Workflow

1. Open n8n dashboard (`http://localhost:5678`)
2. Click **"Workflows"** → **"Import from File"**
3. Select `Speech Agent.json`
4. Activate the workflow

### Step 5: Configure API Credentials

In n8n, set up credentials for:
- **Google Gemini API** (for AI processing)
- **Google Calendar API** (for calendar events)
- **Gmail API** (for email drafts)

### Step 6: Start the Services

**Terminal 1 - Start TTS Service:**
```bash
python tts_service.py
```

**Terminal 2 - Start Voice Assistant:**
```bash
python request.py
```

🎉 **You're ready!** Start speaking commands!

## 🎯 Usage

### Starting the Assistant

1. **Start TTS Service** (Terminal 1):
   ```bash
   python tts_service.py
   ```
   ✅ Server running at `http://127.0.0.1:8000`

2. **Start Voice Assistant** (Terminal 2):
   ```bash
   python request.py
   ```
   ✅ Listening for commands...

### Voice Command Examples

| Command Type | Example |
|-------------|---------|
| **Calendar** | "Remind me to submit the report at 2 PM" |
| **Email** | "Draft an email to the team about tomorrow's meeting" |
| **Chat** | "Tell me a joke" |
| **Chat** | "What can you help me with?" |

### Stopping the Assistant

- Press `Ctrl+C` in the terminal running `request.py`
- Say the stop word (default: "stop") if configured

## 👥 Contributors

### 🌟 Hamza
- Built the **Text-to-Speech FastAPI service** (`tts_service.py`)
- Configured **n8n workflow** (HTTP nodes, Code nodes for response formatting)
- Set up voice response integration

### 🌟 Wali
- Developed the **Speech-to-Text module** (`stt.py`)
- Implemented audio recording and transcription logic
- Audio file management system

### 🌟 Abdullah
- Created the **request handler** (`request.py`)
- Set up **n8n on Docker** and webhook infrastructure
- Implemented **Calendar and Gmail integration nodes** in n8n workflow

## 🙏 Acknowledgments

Special thanks to:
- **Google Gemini AI** for intelligent intent classification
- **n8n** for powerful workflow automation
- **Open-source community** for amazing libraries:
  - `speech_recognition` for Google Speech API integration
  - `pyttsx3` for offline text-to-speech
  - `FastAPI` for modern API development
  - `sounddevice` & `wavio` for audio handling

---

<div align="center">

**Built with ❤️ by Hamza, Wali & Abdullah**

*Empowering productivity through voice automation*

</div>
