# BharatSaarthi - Requirements Specification

## Document Information
- **Project:** BharatSaarthi - Offline Voice-First AI for Rural India
- **Version:** 1.0
- **Date:** February 2026
- **Status:** Active Development

---

## Table of Contents
1. [Introduction](#introduction)
2. [Stakeholders](#stakeholders)
3. [Functional Requirements](#functional-requirements)
4. [Non-Functional Requirements](#non-functional-requirements)
5. [System Requirements](#system-requirements)
6. [User Requirements](#user-requirements)
7. [Data Requirements](#data-requirements)
8. [Interface Requirements](#interface-requirements)
9. [Constraints](#constraints)
10. [Acceptance Criteria](#acceptance-criteria)

---

## 1. Introduction

### 1.1 Purpose
This document specifies the requirements for BharatSaarthi, an offline, voice-first AI assistant designed to help rural Indian citizens access information about agriculture, healthcare, and government services.

### 1.2 Scope
BharatSaarthi will:
- Operate completely offline without internet connectivity
- Support voice-based interaction in multiple Indian languages
- Provide information across three domains: Agriculture, Healthcare, and Government Services
- Run on low-end Android devices (Android 6.0+)
- Maintain user privacy by processing all data on-device

### 1.3 Target Users
- Rural farmers (150M+)
- Rural mothers and caregivers
- Senior citizens in rural areas
- Citizens seeking government scheme information
- Low-literacy users with minimal tech experience

---

## 2. Stakeholders

### 2.1 Primary Stakeholders
- **End Users:** Rural citizens with limited internet access and low digital literacy
- **Government:** Ministry of Rural Development, NITI Aayog, State Governments
- **NGOs:** Rural development organizations
- **Healthcare Workers:** ASHA workers, ANMs, PHC staff
- **Agricultural Officers:** Krishi Vigyan Kendras, Agriculture departments

### 2.2 Secondary Stakeholders
- **Telecom Operators:** For distribution partnerships
- **Device Manufacturers:** For pre-installation
- **Content Providers:** Agricultural experts, healthcare professionals
- **Investors:** For funding and scaling

---

## 3. Functional Requirements

### 3.1 Core Functionality

#### FR-1: Voice Input Processing
**Priority:** MUST HAVE  
**Description:** System shall accept voice input in local languages  
**Acceptance Criteria:**
- Accept voice input in Hindi, Telugu, Tamil, Bengali, Marathi
- Process voice input offline without internet
- Handle rural accents and dialects
- Minimum 80% speech recognition accuracy
- Response time < 3 seconds

#### FR-2: Intent Classification
**Priority:** MUST HAVE  
**Description:** System shall identify user intent from queries  
**Acceptance Criteria:**
- Classify queries into: Agriculture, Healthcare, Government, General
- Minimum 85% classification accuracy
- Handle ambiguous queries with clarifying questions
- Support both voice and text input

#### FR-3: Knowledge Retrieval
**Priority:** MUST HAVE  
**Description:** System shall retrieve relevant information from knowledge base  
**Acceptance Criteria:**
- Query local SQLite database
- Return results in < 1 second
- Provide accurate, verified information
- Include source references where applicable

#### FR-4: Response Generation
**Priority:** MUST HAVE  
**Description:** System shall generate contextual responses  
**Acceptance Criteria:**
- Generate responses in user's language
- Use simple, jargon-free language
- Provide actionable advice
- Include next steps or contact information

#### FR-5: Voice Output
**Priority:** MUST HAVE  
**Description:** System shall convert text responses to speech  
**Acceptance Criteria:**
- Generate clear, natural-sounding speech
- Support multiple Indian languages
- Adjustable speech rate (slow/normal/fast)
- Work offline without internet

### 3.2 Domain-Specific Requirements

#### FR-6: Agriculture Domain
**Priority:** MUST HAVE  
**Description:** Provide agricultural information and advice  
**Acceptance Criteria:**
- Crop disease diagnosis (50+ diseases)
- Fertilizer recommendations
- Seasonal farming advice
- Pest control guidance
- Weather-appropriate suggestions
- Local market prices (when available)

**Example Queries:**
- "मेरी धान की फसल पर दाग हैं" (My rice crop has spots)
- "खेत में खाद कब डालें" (When to apply fertilizer)
- "गेहूं की बुवाई का समय" (Wheat sowing time)

#### FR-7: Healthcare Domain
**Priority:** MUST HAVE  
**Description:** Provide healthcare information and guidance  
**Acceptance Criteria:**
- Vaccination schedules (birth to 16 months)
- Basic symptom guidance
- Nearby facility information
- Emergency contact numbers
- Maternal health information
- Child nutrition advice

**Example Queries:**
- "बच्चे को टीका लगवाना है" (Need to vaccinate child)
- "बुखार की दवाई" (Medicine for fever)
- "नजदीकी अस्पताल कहाँ है" (Where is nearest hospital)

#### FR-8: Government Services Domain
**Priority:** MUST HAVE  
**Description:** Provide government scheme information  
**Acceptance Criteria:**
- 100+ government schemes covered
- Eligibility criteria for each scheme
- Required documents list
- Application process guidance
- Contact information for local offices
- Benefit amounts and timelines

**Example Queries:**
- "मुझे पेंशन मिलेगी?" (Will I get pension?)
- "किसान योजना के बारे में बताओ" (Tell about farmer scheme)
- "राशन कार्ड कैसे बनाएं" (How to make ration card)

### 3.3 User Interaction Requirements

#### FR-9: Clarification Handling
**Priority:** SHOULD HAVE  
**Description:** Ask clarifying questions when intent is unclear  
**Acceptance Criteria:**
- Detect ambiguous queries (confidence < 70%)
- Ask simple yes/no or multiple-choice questions
- Maximum 2 clarifying questions per query
- Provide examples to guide user

#### FR-10: Error Handling
**Priority:** MUST HAVE  
**Description:** Handle errors gracefully  
**Acceptance Criteria:**
- Provide helpful error messages
- Suggest alternative queries
- Never crash or freeze
- Log errors for improvement

#### FR-11: Multi-Turn Conversations
**Priority:** SHOULD HAVE  
**Description:** Support follow-up questions  
**Acceptance Criteria:**
- Remember context from previous query
- Support up to 3 turns in conversation
- Clear context when topic changes

### 3.4 Data Management Requirements

#### FR-12: Offline Data Storage
**Priority:** MUST HAVE  
**Description:** Store all data locally on device  
**Acceptance Criteria:**
- Use SQLite for structured data
- Total storage < 200MB
- Fast query performance (< 100ms)
- Data integrity maintained

#### FR-13: Data Updates
**Priority:** SHOULD HAVE  
**Description:** Update knowledge base periodically  
**Acceptance Criteria:**
- Support offline updates via USB
- Support SMS-based critical updates
- Validate data before updating
- Rollback capability if update fails

#### FR-14: User Privacy
**Priority:** MUST HAVE  
**Description:** Protect user privacy  
**Acceptance Criteria:**
- No data sent to cloud
- No user tracking or analytics
- Optional local caching (encrypted)
- Clear privacy policy

---

## 4. Non-Functional Requirements

### 4.1 Performance Requirements

#### NFR-1: Response Time
**Priority:** MUST HAVE  
**Requirement:** End-to-end response time < 3 seconds  
**Measurement:** 95th percentile of all queries  
**Rationale:** Users expect quick responses for good UX

#### NFR-2: App Size
**Priority:** MUST HAVE  
**Requirement:** Total app size < 200MB (including one language pack)  
**Measurement:** APK size + initial data  
**Rationale:** Low-end devices have limited storage

#### NFR-3: Battery Consumption
**Priority:** SHOULD HAVE  
**Requirement:** < 5% battery drain per hour of active use  
**Measurement:** Battery stats on Android  
**Rationale:** Rural areas have limited charging access

#### NFR-4: Memory Usage
**Priority:** SHOULD HAVE  
**Requirement:** < 100MB RAM during operation  
**Measurement:** Android memory profiler  
**Rationale:** Low-end devices have 1-2GB RAM

### 4.2 Reliability Requirements

#### NFR-5: Availability
**Priority:** MUST HAVE  
**Requirement:** 99.9% uptime (offline operation)  
**Measurement:** Crash-free sessions  
**Rationale:** Users depend on system for critical information

#### NFR-6: Accuracy
**Priority:** MUST HAVE  
**Requirement:** 
- Intent classification: 85% accuracy
- Speech recognition: 80% accuracy
- Information accuracy: 95% verified
**Measurement:** Test dataset evaluation  
**Rationale:** Incorrect information can be harmful

#### NFR-7: Fault Tolerance
**Priority:** MUST HAVE  
**Requirement:** Graceful degradation on errors  
**Measurement:** Error handling test cases  
**Rationale:** System should never crash

### 4.3 Usability Requirements

#### NFR-8: Learnability
**Priority:** MUST HAVE  
**Requirement:** 80% of users can complete basic task within 5 minutes  
**Measurement:** User testing sessions  
**Rationale:** Low-literacy users need simple interface

#### NFR-9: Accessibility
**Priority:** MUST HAVE  
**Requirement:** 
- Voice-only operation possible
- Large touch targets (min 48dp)
- High contrast UI
- Screen reader compatible
**Measurement:** Accessibility audit  
**Rationale:** Users may have visual or motor impairments

#### NFR-10: Language Support
**Priority:** MUST HAVE  
**Requirement:** Support 5+ Indian languages initially  
**Languages:** Hindi, Telugu, Tamil, Bengali, Marathi  
**Measurement:** Language coverage  
**Rationale:** India has 22 official languages

### 4.4 Scalability Requirements

#### NFR-11: User Scalability
**Priority:** SHOULD HAVE  
**Requirement:** Support 10M+ concurrent users  
**Measurement:** Load testing (offline, so device-level)  
**Rationale:** Target is 800M+ rural citizens

#### NFR-12: Data Scalability
**Priority:** SHOULD HAVE  
**Requirement:** Support 10,000+ knowledge base entries  
**Measurement:** Database performance tests  
**Rationale:** Need comprehensive coverage

#### NFR-13: Geographic Scalability
**Priority:** SHOULD HAVE  
**Requirement:** Support state/district-specific information  
**Measurement:** Regional data coverage  
**Rationale:** Schemes vary by state

### 4.5 Security Requirements

#### NFR-14: Data Security
**Priority:** MUST HAVE  
**Requirement:** 
- All data encrypted at rest
- No data transmission to external servers
- Secure local storage
**Measurement:** Security audit  
**Rationale:** Protect user privacy

#### NFR-15: Code Security
**Priority:** SHOULD HAVE  
**Requirement:** 
- No hardcoded credentials
- Input validation on all queries
- Protection against injection attacks
**Measurement:** Code review, penetration testing  
**Rationale:** Prevent malicious use

### 4.6 Maintainability Requirements

#### NFR-16: Code Quality
**Priority:** SHOULD HAVE  
**Requirement:** 
- Modular architecture
- 80%+ code documentation
- Unit test coverage > 70%
**Measurement:** Code metrics  
**Rationale:** Easy to maintain and extend

#### NFR-17: Extensibility
**Priority:** SHOULD HAVE  
**Requirement:** 
- Plugin architecture for new domains
- Easy to add new languages
- Configurable knowledge base
**Measurement:** Time to add new feature  
**Rationale:** Need to scale quickly

---

## 5. System Requirements

### 5.1 Hardware Requirements

#### Minimum Device Specifications
- **Processor:** 1.2 GHz Quad-core
- **RAM:** 1 GB
- **Storage:** 500 MB free space
- **Display:** 4.5" screen, 480x800 resolution
- **Audio:** Microphone and speaker
- **OS:** Android 6.0 (Marshmallow) or higher

#### Recommended Device Specifications
- **Processor:** 1.5 GHz Octa-core
- **RAM:** 2 GB
- **Storage:** 1 GB free space
- **Display:** 5.5" screen, 720x1280 resolution
- **Audio:** Noise-canceling microphone
- **OS:** Android 8.0 (Oreo) or higher

### 5.2 Software Requirements

#### Development Environment
- **Language:** Python 3.7+
- **ML Framework:** TensorFlow Lite 2.x
- **Database:** SQLite 3.x
- **Web Framework:** Flask 2.x (for web demo)
- **Testing:** pytest, unittest

#### Runtime Dependencies
- **Speech Recognition:** Vosk 0.3.x
- **Text-to-Speech:** pyttsx3 2.9+
- **NLP:** scikit-learn 1.0+
- **Data Processing:** pandas 1.3+, numpy 1.21+

#### Mobile Deployment
- **Build Tool:** Buildozer (for Android)
- **Framework:** Kivy or BeeWare
- **Min SDK:** Android API 23 (Android 6.0)
- **Target SDK:** Android API 30 (Android 11)

---

## 6. User Requirements

### 6.1 User Stories

#### US-1: Farmer Crop Disease
**As a** farmer  
**I want to** identify crop diseases by describing symptoms  
**So that** I can treat my crops before they die  

**Acceptance Criteria:**
- Can describe symptoms in local language
- Get disease name and treatment within 3 seconds
- Receive prevention tips
- Get contact info for local agriculture office

#### US-2: Mother Vaccination
**As a** mother  
**I want to** know when my child needs vaccinations  
**So that** I can protect my child from diseases  

**Acceptance Criteria:**
- Can ask about vaccination schedule
- Get age-appropriate vaccine list
- Receive reminder capability
- Get location of nearest vaccination center

#### US-3: Senior Pension
**As a** senior citizen  
**I want to** check if I'm eligible for pension  
**So that** I can apply and receive benefits  

**Acceptance Criteria:**
- Can ask about pension eligibility
- Get clear yes/no answer with criteria
- Receive list of required documents
- Get application process steps

#### US-4: First-Time User
**As a** first-time user  
**I want to** understand what the app can do  
**So that** I can use it effectively  

**Acceptance Criteria:**
- Simple onboarding (< 1 minute)
- Example queries shown
- Voice tutorial available
- Can skip and explore

#### US-5: Low-Literacy User
**As a** user who cannot read  
**I want to** use the app entirely by voice  
**So that** I can access information independently  

**Acceptance Criteria:**
- No reading required
- All instructions spoken
- Voice-only navigation
- Audio feedback for all actions

### 6.2 User Personas

#### Persona 1: Ramesh (Farmer)
- **Age:** 45
- **Education:** 5th grade
- **Language:** Hindi (rural dialect)
- **Tech Experience:** Basic phone usage
- **Device:** Low-end Android (₹5,000)
- **Internet:** No reliable connection
- **Primary Need:** Crop disease diagnosis
- **Usage Pattern:** 2-3 times per week during farming season

#### Persona 2: Savita (Mother)
- **Age:** 32
- **Education:** Illiterate
- **Language:** Telugu
- **Tech Experience:** None
- **Device:** Borrowed smartphone
- **Internet:** No access
- **Primary Need:** Child healthcare information
- **Usage Pattern:** Monthly for vaccination reminders

#### Persona 3: Raju (Senior Citizen)
- **Age:** 68
- **Education:** 8th grade
- **Language:** Tamil
- **Tech Experience:** Minimal
- **Device:** Feature phone (future target)
- **Internet:** No access
- **Primary Need:** Government pension information
- **Usage Pattern:** One-time for application, occasional queries

---

## 7. Data Requirements

### 7.1 Knowledge Base Requirements

#### Agriculture Data
- **Crops Covered:** 20+ major crops (rice, wheat, cotton, sugarcane, etc.)
- **Diseases:** 50+ common diseases with symptoms, treatment, prevention
- **Pests:** 30+ common pests with identification and control
- **Fertilizers:** NPK recommendations by crop and soil type
- **Seasonal Advice:** Sowing, harvesting times by region
- **Update Frequency:** Quarterly

#### Healthcare Data
- **Vaccination Schedule:** Birth to 16 months (WHO/ICMR guidelines)
- **Common Symptoms:** 20+ symptoms with basic guidance
- **Maternal Health:** Pregnancy care, nutrition advice
- **Child Nutrition:** Age-appropriate diet recommendations
- **Emergency Numbers:** State-wise helplines
- **Update Frequency:** Annually

#### Government Schemes Data
- **Central Schemes:** 50+ schemes (PM-KISAN, Ayushman Bharat, etc.)
- **State Schemes:** Top 10 schemes per state
- **Eligibility Criteria:** Clear, simple language
- **Documents Required:** Complete list with alternatives
- **Application Process:** Step-by-step instructions
- **Update Frequency:** Monthly

### 7.2 Data Quality Requirements

- **Accuracy:** 95%+ verified by domain experts
- **Completeness:** All mandatory fields populated
- **Consistency:** Standardized format across domains
- **Timeliness:** Updated within 30 days of official changes
- **Relevance:** Applicable to rural Indian context

### 7.3 Data Sources

- **Agriculture:** ICAR, State Agriculture Departments, KVKs
- **Healthcare:** WHO, ICMR, State Health Departments
- **Government:** MyGov India, State Government Portals
- **Validation:** Domain experts, field testing

---

## 8. Interface Requirements

### 8.1 User Interface Requirements

#### UI-1: Voice Interface (Primary)
- Voice input button (large, prominent)
- Visual feedback during listening
- Waveform animation during speech
- Clear "listening" / "processing" / "speaking" states

#### UI-2: Text Interface (Fallback)
- Text input field for typing queries
- On-screen keyboard support
- Copy-paste functionality
- Quick query buttons

#### UI-3: Response Display
- Large, readable text (min 16sp)
- High contrast (WCAG AA compliant)
- Option to replay audio response
- Share response capability

#### UI-4: Navigation
- Simple, flat navigation (max 2 levels)
- Back button always visible
- Home button to restart
- Settings easily accessible

### 8.2 Web Interface Requirements (Demo)

#### WI-1: Responsive Design
- Works on desktop, tablet, mobile
- Adapts to screen size
- Touch-friendly controls
- Fast loading (< 2 seconds)

#### WI-2: Interactive Demo
- Live chat interface
- Quick query buttons
- Real-time responses
- Example queries shown

#### WI-3: Information Display
- Feature showcase
- Statistics dashboard
- Use case examples
- Technical details

---

## 9. Constraints

### 9.1 Technical Constraints

#### TC-1: Offline Operation
**Constraint:** Must work without internet connectivity  
**Impact:** Cannot use cloud APIs, must use on-device processing  
**Mitigation:** Use compressed models, local database

#### TC-2: Device Limitations
**Constraint:** Must run on low-end Android devices (1GB RAM)  
**Impact:** Limited model size, processing power  
**Mitigation:** Model compression, lazy loading, efficient algorithms

#### TC-3: Storage Limitations
**Constraint:** Total app size < 200MB  
**Impact:** Limited knowledge base size, single language pack  
**Mitigation:** Compression, downloadable language packs

### 9.2 Business Constraints

#### BC-1: Budget
**Constraint:** Limited development budget  
**Impact:** Small team, limited resources  
**Mitigation:** Open-source tools, modular development

#### BC-2: Timeline
**Constraint:** 6-month development timeline  
**Impact:** Must prioritize features  
**Mitigation:** MVP approach, phased rollout

### 9.3 Regulatory Constraints

#### RC-1: Data Privacy
**Constraint:** Must comply with Indian data protection laws  
**Impact:** No data collection without consent  
**Mitigation:** Offline-first design, no data transmission

#### RC-2: Medical Disclaimer
**Constraint:** Cannot provide medical diagnosis  
**Impact:** Healthcare advice must be general  
**Mitigation:** Clear disclaimers, refer to professionals

#### RC-3: Government Information
**Constraint:** Must use official government sources  
**Impact:** Cannot create or modify scheme information  
**Mitigation:** Direct sourcing from official portals

---

## 10. Acceptance Criteria

### 10.1 Functional Acceptance

#### AC-1: Core Functionality
- [ ] Voice input works in 5+ languages
- [ ] Intent classification accuracy > 85%
- [ ] Response time < 3 seconds
- [ ] All 3 domains functional
- [ ] Offline operation verified

#### AC-2: Domain Coverage
- [ ] Agriculture: 50+ diseases covered
- [ ] Healthcare: Complete vaccination schedule
- [ ] Government: 100+ schemes covered
- [ ] All information verified by experts

#### AC-3: User Experience
- [ ] 80% users complete task in < 5 minutes
- [ ] 90% users find responses helpful
- [ ] 85% users can operate without assistance
- [ ] No critical bugs in production

### 10.2 Non-Functional Acceptance

#### AC-4: Performance
- [ ] App size < 200MB
- [ ] Battery usage < 5% per hour
- [ ] Memory usage < 100MB
- [ ] 99.9% crash-free sessions

#### AC-5: Quality
- [ ] Code coverage > 70%
- [ ] All critical paths tested
- [ ] Security audit passed
- [ ] Accessibility audit passed

### 10.3 User Acceptance Testing

#### AC-6: Field Testing
- [ ] Tested with 100+ rural users
- [ ] Tested in 5+ states
- [ ] Tested in zero-connectivity areas
- [ ] User satisfaction > 75%

#### AC-7: Expert Validation
- [ ] Agricultural experts approve content
- [ ] Healthcare professionals approve content
- [ ] Government officials approve scheme info
- [ ] Language experts approve translations

---

## 11. Success Metrics

### 11.1 Adoption Metrics
- **Target:** 100K users in first 6 months
- **Measurement:** App installs, active users
- **Goal:** 50% monthly active users

### 11.2 Engagement Metrics
- **Target:** 3+ queries per user per month
- **Measurement:** Query logs (anonymized)
- **Goal:** 60% user retention after 3 months

### 11.3 Impact Metrics
- **Target:** 80% users find information helpful
- **Measurement:** User surveys, feedback
- **Goal:** 70% users take action based on advice

### 11.4 Technical Metrics
- **Target:** 99% uptime, < 1% crash rate
- **Measurement:** Analytics, crash reports
- **Goal:** 4+ star rating on Play Store

---

## 12. Future Requirements (Phase 2)

### FR-Future-1: Visual Recognition
- Camera-based crop disease identification
- Photo upload and analysis
- 80%+ accuracy on common diseases

### FR-Future-2: Personalization
- User profile and history
- Personalized recommendations
- Learning from user interactions

### FR-Future-3: Peer Network
- Share knowledge between users
- Community Q&A
- Local expert network

### FR-Future-4: Additional Domains
- Education (scholarships, schools)
- Finance (banking, loans)
- Legal (basic rights, procedures)

### FR-Future-5: Advanced Features
- Multi-language support (20+ languages)
- Dialect recognition
- Context-aware suggestions
- Predictive advice

---

## 13. Glossary

- **ASHA:** Accredited Social Health Activist
- **ANM:** Auxiliary Nurse Midwife
- **BPL:** Below Poverty Line
- **CSC:** Common Service Center
- **ICAR:** Indian Council of Agricultural Research
- **ICMR:** Indian Council of Medical Research
- **KVK:** Krishi Vigyan Kendra (Agricultural Science Center)
- **NLP:** Natural Language Processing
- **PHC:** Primary Health Center
- **STT:** Speech-to-Text
- **TTS:** Text-to-Speech

---

## 14. Approval

### Document Approval
- **Author:** [Your Name]
- **Reviewed By:** [Reviewer Name]
- **Approved By:** [Approver Name]
- **Date:** February 7, 2026
- **Version:** 1.0

### Change History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | Feb 7, 2026 | [Your Name] | Initial requirements document |

---

**End of Requirements Document**
