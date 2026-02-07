# BharatSaarthi - System Architecture

## Overview
BharatSaarthi is an offline, voice-first AI system designed for rural India. It operates entirely on-device without requiring internet connectivity.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────┐
│                    USER INTERFACE                        │
│              (Voice Input / Voice Output)                │
└────────────────────┬────────────────────────────────────┘
                     │
         ┌───────────┴───────────┐
         │                       │
    ┌────▼─────┐          ┌─────▼────┐
    │   STT    │          │   TTS    │
    │ (Vosk)   │          │(pyttsx3) │
    └────┬─────┘          └─────▲────┘
         │                      │
         │    ┌─────────────────┘
         │    │
    ┌────▼────▼─────────────────────────────────┐
    │      Intent Classifier (NLP)              │
    │   (Hybrid: Rules + ML)                    │
    └────────────────┬──────────────────────────┘
                     │
    ┌────────────────▼──────────────────────────┐
    │         AI Engine (Core)                  │
    │   - Context Management                    │
    │   - Decision Logic                        │
    │   - Response Generation                   │
    └────┬────────┬────────┬────────────────────┘
         │        │        │
    ┌────▼───┐ ┌─▼────┐ ┌─▼──────┐
    │ Agri   │ │Health│ │ Govt   │
    │   KB   │ │  KB  │ │  KB    │
    └────────┘ └──────┘ └────────┘
         │        │        │
    ┌────▼────────▼────────▼────────┐
    │   SQLite (Offline Storage)    │
    └───────────────────────────────┘
```

## Component Details

### 1. Speech-to-Text (STT)
- **Technology**: Vosk (offline speech recognition)
- **Languages**: Hindi, Telugu, Tamil, Bengali, Marathi
- **Model Size**: ~50MB per language (compressed)
- **Latency**: <2 seconds on mid-range Android

### 2. Text-to-Speech (TTS)
- **Technology**: pyttsx3 (offline synthesis)
- **Voice Quality**: Natural-sounding Indian voices
- **Customization**: Speed, pitch adjustable for clarity

### 3. Intent Classifier
- **Approach**: Hybrid (Rule-based + ML)
- **Categories**: Agriculture, Healthcare, Government, Education
- **Accuracy**: ~85% on rural queries
- **Fallback**: Clarifying questions when uncertain

### 4. AI Engine
- **Decision Logic**: Rule-based + decision trees
- **Context Awareness**: Location, season, user profile
- **Response Generation**: Template-based with dynamic content

### 5. Knowledge Bases
- **Agriculture KB**: 
  - 50+ crop diseases
  - Seasonal advice
  - Fertilizer recommendations
  
- **Healthcare KB**:
  - Vaccination schedules
  - Common symptoms
  - Nearby facility info
  
- **Government KB**:
  - 100+ schemes
  - Eligibility criteria
  - Document requirements

## Data Flow

1. User speaks query in local language
2. STT converts speech to text
3. Intent Classifier identifies domain (agri/health/govt)
4. AI Engine retrieves relevant information from KB
5. Response generated in local language
6. TTS converts text to speech
7. User hears the answer

## Offline Capabilities

- All models stored on device
- SQLite for local data storage
- No API calls required
- Works in zero-connectivity areas

## Performance Metrics

- **Response Time**: <3 seconds end-to-end
- **Storage**: ~200MB total (all languages)
- **RAM Usage**: <100MB during operation
- **Battery**: Minimal impact (<5% per hour)

## Scalability

- Modular KB design (easy to add domains)
- Language models can be downloaded on-demand
- District-specific data can be pre-loaded
- Updates via SMS/offline sync when available

## Security & Privacy

- No data leaves the device
- No user tracking
- No cloud dependency
- Transparent AI responses (explainable)
