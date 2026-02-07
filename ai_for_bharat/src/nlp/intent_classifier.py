"""
Intent Classification Engine
Lightweight NLP for understanding user queries
"""

import re

class IntentClassifier:
    def __init__(self):
        """
        Initialize intent classifier with keyword patterns
        Hybrid approach: Rule-based + ML (for production)
        """
        self.intent_patterns = {
            'agriculture': [
                'fasal', 'kheti', 'crop', 'bimari', 'disease', 'keet', 'pest',
                'khad', 'fertilizer', 'बीमारी', 'फसल', 'खेती', 'खाद', 'दाग'
            ],
            'healthcare': [
                'teeka', 'vaccine', 'dawai', 'medicine', 'doctor', 'hospital',
                'bimari', 'टीका', 'दवाई', 'डॉक्टर', 'बीमारी'
            ],
            'government': [
                'yojana', 'scheme', 'pension', 'ration', 'card', 'subsidy',
                'योजना', 'पेंशन', 'राशन', 'सब्सिडी'
            ],
            'education': [
                'school', 'scholarship', 'padhai', 'exam', 'छात्रवृत्ति', 'स्कूल'
            ]
        }
        print("✓ Intent Classifier loaded")
    
    def classify(self, text):
        """
        Classify user intent from text
        Returns: intent category
        """
        text_lower = text.lower()
        
        # Check each intent and count keyword matches
        intent_scores = {}
        for intent, keywords in self.intent_patterns.items():
            score = 0
            for keyword in keywords:
                if keyword.lower() in text_lower:
                    score += 1
            if score > 0:
                intent_scores[intent] = score
        
        # Return intent with highest score
        if intent_scores:
            return max(intent_scores, key=intent_scores.get)
        
        return 'general'
    
    def extract_entities(self, text):
        """
        Extract key entities (crop name, disease, location, etc.)
        """
        entities = {}
        
        # Example: Extract crop names
        crops = ['धान', 'गेहूं', 'मक्का', 'rice', 'wheat', 'corn']
        for crop in crops:
            if crop in text.lower():
                entities['crop'] = crop
        
        return entities
