from fastapi import FastAPI
from pydantic import BaseModel
import pyttsx3
import uvicorn
import threading

# Initialize FastAPI app
app = FastAPI()

# Request model
class SpeechRequest(BaseModel):
    reply: str

# Global variables
current_engine = None
is_speaking = False
engine_lock = threading.Lock()

def create_engine():
    """Create and return a new TTS engine"""
    engine = pyttsx3.init()
    return engine

def stop_current_engine():
    """Stop current engine if running"""
    global current_engine, is_speaking
    if current_engine and is_speaking:
        try:
            current_engine.stop()
            is_speaking = False
        except:
            pass
    current_engine = None

# Health endpoint
@app.get("/health")
def health():
    return {"status": "ok"}

# TTS endpoint
@app.post("/speak")
def speak(request: SpeechRequest):
    global current_engine, is_speaking
    
    def speak_text():
        global current_engine, is_speaking
        
        with engine_lock:
            # Stop current engine if running
            stop_current_engine()
            
            # Re-initialize engine
            current_engine = create_engine()
            is_speaking = True
        
        try:
            # Speak the text
            current_engine.say(request.reply)
            current_engine.runAndWait()
        except Exception as e:
            print(f"TTS Error: {e}")
        finally:
            with engine_lock:
                is_speaking = False
                current_engine = None
    
    # Run in background thread
    thread = threading.Thread(target=speak_text)
    thread.daemon = True
    thread.start()
    
    return {"status": "success", "message": "Speech started (previous interrupted)"}

# Run server
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)