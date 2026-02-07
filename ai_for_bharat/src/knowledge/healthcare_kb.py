"""
Healthcare Knowledge Base
Contains vaccination schedules, basic health advice
"""

class HealthcareKB:
    def __init__(self):
        """
        Initialize healthcare knowledge base
        """
        self.vaccination_schedule = {
            'birth': 'BCG, OPV-0, Hepatitis B',
            '6_weeks': 'DPT-1, OPV-1, Hepatitis B-2',
            '10_weeks': 'DPT-2, OPV-2',
            '14_weeks': 'DPT-3, OPV-3',
            '9_months': 'Measles',
            '16_months': 'DPT Booster, OPV Booster'
        }
        
        self.common_symptoms = {
            'बुखार': 'पानी पीएं, आराम करें। 3 दिन से ज्यादा बुखार हो तो डॉक्टर से मिलें।',
            'खांसी': 'गर्म पानी पीएं। 2 हफ्ते से ज्यादा खांसी हो तो जांच कराएं।'
        }
        print("✓ Healthcare KB loaded")
    
    def get_response(self, query):
        """
        Generate healthcare-related response
        """
        query_lower = query.lower()
        
        # Vaccination queries
        if 'टीका' in query_lower or 'vaccine' in query_lower:
            return self._get_vaccination_info()
        
        # Symptom-based advice
        if 'बुखार' in query_lower:
            return self.common_symptoms['बुखार']
        
        if 'खांसी' in query_lower:
            return self.common_symptoms['खांसी']
        
        return "स्वास्थ्य संबंधी जानकारी के लिए टीकाकरण, बुखार, या अन्य लक्षण के बारे में पूछें।"
    
    def _get_vaccination_info(self):
        """
        Provide vaccination schedule
        """
        schedule = "बच्चों के टीकाकरण का समय:\n"
        schedule += "जन्म पर: BCG, OPV, Hepatitis B\n"
        schedule += "6 सप्ताह: DPT-1, OPV-1\n"
        schedule += "9 महीने: खसरा का टीका\n"
        schedule += "नजदीकी आंगनवाड़ी या PHC में संपर्क करें।"
        return schedule
