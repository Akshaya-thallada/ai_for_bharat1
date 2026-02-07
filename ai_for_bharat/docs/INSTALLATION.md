# BharatSaarthi - Installation Guide

## Prerequisites

### System Requirements
- **OS**: Windows 10+, macOS 10.14+, Linux (Ubuntu 18.04+)
- **Python**: 3.8 or higher
- **RAM**: 2GB minimum (4GB recommended)
- **Storage**: 500MB free space

### For Android Deployment
- **Android**: 6.0 (Marshmallow) or higher
- **RAM**: 1GB minimum
- **Storage**: 300MB free space

---

## Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/bharatsaarthi.git
cd bharatsaarthi
```

### 2. Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Download Language Models (Optional)
For full offline speech recognition, download Vosk models:

```bash
# Hindi model (~50MB)
wget https://alphacephei.com/vosk/models/vosk-model-small-hi-0.22.zip
unzip vosk-model-small-hi-0.22.zip -d data/models/

# Other languages available at: https://alphacephei.com/vosk/models
```

### 5. Initialize Database
```bash
python scripts/init_database.py
```

### 6. Run the Application
```bash
python src/main.py
```

---

## Troubleshooting

### Issue: pyttsx3 not working on Linux
**Solution**: Install espeak
```bash
sudo apt-get install espeak
```

### Issue: Vosk model not found
**Solution**: Ensure models are in `data/models/` directory

### Issue: Permission denied on macOS
**Solution**: Grant microphone access in System Preferences

---

## Development Setup

### Install Development Dependencies
```bash
pip install -r requirements-dev.txt
```

### Run Tests
```bash
pytest tests/
```

### Code Formatting
```bash
black src/
flake8 src/
```

---

## Android Deployment

### Using Buildozer (Linux/macOS)
```bash
# Install buildozer
pip install buildozer

# Build APK
buildozer android debug

# APK will be in bin/ directory
```

### Using Python-for-Android (Advanced)
See `docs/ANDROID_BUILD.md` for detailed instructions

---

## Configuration

### Language Settings
Edit `config/settings.json`:
```json
{
  "default_language": "hi",
  "supported_languages": ["hi", "te", "ta", "bn"],
  "voice_speed": 150
}
```

### Knowledge Base Updates
Place new data files in `data/knowledge/` and run:
```bash
python scripts/update_kb.py
```

---

## Quick Start (Demo Mode)

For quick testing without full setup:
```bash
python src/main.py --demo
```

This runs with minimal dependencies and sample data.

---

## Support

For issues or questions:
- GitHub Issues: [link]
- Email: support@bharatsaarthi.in
- Documentation: [link]
