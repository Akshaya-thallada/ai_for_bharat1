"""
Text-to-Speech Engine (Offline)
Uses pyttsx3 for offline voice synthesis
"""

import pyttsx3

class TextToSpeech:
    def __init__(self, language='hi'):
        """
        Initialize offline TTS engine
        """
        self.engine = pyttsx3.init()
        self.language = language
        self._configure_voice()
        print(f"✓ TTS Engine loaded for {language}")
    
    def _configure_voice(self):
        """Configure voice properties for Indian languages"""
        self.engine.setProperty('rate', 150)  # Slower for clarity
        self.engine.setProperty('volume', 0.9)
    
    def speak(self, text):
        """
        Convert text to speech and play
        """
        self.engine.say(text)
        self.engine.runAndWait()
    
    def save_audio(self, text, filename):
        """
        Save speech to audio file for offline playback
        """
        self.engine.save_to_file(text, filename)
        self.engine.runAndWait()
