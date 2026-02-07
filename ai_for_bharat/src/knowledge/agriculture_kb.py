"""
Agriculture Knowledge Base
Contains farming advice, crop diseases, treatments
"""

class AgricultureKB:
    def __init__(self):
        """
        Initialize agriculture knowledge base
        In production: Load from SQLite database
        """
        self.crop_diseases = {
            'धान': {
                'पत्ती पर दाग': {
                    'treatment': 'कार्बेन्डाजिम दवा का छिड़काव करें',
                    'prevention': 'खेत में पानी जमा न होने दें'
                }
            },
            'गेहूं': {
                'रतुआ रोग': {
                    'treatment': 'प्रोपिकोनाजोल का उपयोग करें',
                    'prevention': 'प्रमाणित बीज का उपयोग करें'
                }
            }
        }
        
        self.seasonal_advice = {
            'खरीफ': 'धान, मक्का, बाजरा की बुवाई का समय',
            'रबी': 'गेहूं, चना, सरसों की बुवाई का समय'
        }
        print("✓ Agriculture KB loaded")
    
    def get_response(self, query):
        """
        Generate agriculture-related response
        """
        query_lower = query.lower()
        
        # Disease detection
        if 'दाग' in query_lower or 'बीमारी' in query_lower:
            return self._diagnose_disease(query)
        
        # Fertilizer advice
        if 'खाद' in query_lower or 'fertilizer' in query_lower:
            return "मिट्टी परीक्षण के आधार पर NPK खाद का उपयोग करें। नजदीकी कृषि केंद्र से संपर्क करें।"
        
        # General farming advice
        return "कृपया अपनी फसल और समस्या के बारे में बताएं। मैं आपकी मदद करूंगा।"
    
    def _diagnose_disease(self, query):
        """
        Diagnose crop disease from symptoms
        """
        if 'धान' in query or 'rice' in query:
            return "धान में पत्ती पर दाग हो सकता है। उपचार: कार्बेन्डाजिम दवा का छिड़काव करें। रोकथाम: खेत में पानी जमा न होने दें।"
        
        return "कृपया फसल का नाम और लक्षण बताएं। मैं सही उपचार बताऊंगा।"
