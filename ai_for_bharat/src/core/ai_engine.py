"""
BharatSaarthi AI Engine
Core reasoning and response generation
"""

from knowledge.agriculture_kb import AgricultureKB
from knowledge.healthcare_kb import HealthcareKB
from knowledge.government_kb import GovernmentKB

class BharatSaarthiEngine:
    def __init__(self):
        """
        Initialize AI engine with domain knowledge bases
        """
        self.agri_kb = AgricultureKB()
        self.health_kb = HealthcareKB()
        self.govt_kb = GovernmentKB()
        print("✓ AI Engine initialized with knowledge bases")
    
    def process(self, query, intent):
        """
        Process user query and generate response
        """
        if intent == 'agriculture':
            return self.agri_kb.get_response(query)
        elif intent == 'healthcare':
            return self.health_kb.get_response(query)
        elif intent == 'government':
            return self.govt_kb.get_response(query)
        else:
            return self._general_response()
    
    def _general_response(self):
        """
        Handle general queries
        """
        return "मैं आपकी मदद कर सकता हूं। कृपया खेती, स्वास्थ्य या सरकारी योजना के बारे में पूछें।"
    
    def get_contextual_info(self, location=None, season=None):
        """
        Provide context-aware information based on location and season
        """
        context = {}
        if season:
            context['season_advice'] = f"Current season: {season}"
        if location:
            context['local_info'] = f"Location: {location}"
        return context
