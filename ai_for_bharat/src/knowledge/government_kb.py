"""
Government Schemes Knowledge Base
Contains information about government schemes and eligibility
"""

class GovernmentKB:
    def __init__(self):
        """
        Initialize government schemes knowledge base
        """
        self.schemes = {
            'pm_kisan': {
                'name': 'PM-KISAN योजना',
                'eligibility': 'सभी किसान परिवार जिनके पास खेती योग्य जमीन है',
                'benefit': '₹6000 प्रति वर्ष (₹2000 की 3 किस्तें)',
                'documents': 'आधार कार्ड, बैंक खाता, जमीन के कागजात'
            },
            'ayushman_bharat': {
                'name': 'आयुष्मान भारत योजना',
                'eligibility': 'गरीबी रेखा से नीचे के परिवार',
                'benefit': '₹5 लाख तक का मुफ्त इलाज',
                'documents': 'राशन कार्ड, आधार कार्ड'
            },
            'pension': {
                'name': 'वृद्धावस्था पेंशन',
                'eligibility': '60 वर्ष से अधिक आयु, BPL परिवार',
                'benefit': '₹200-500 प्रति माह (राज्य के अनुसार)',
                'documents': 'आयु प्रमाण पत्र, आधार कार्ड, BPL कार्ड'
            }
        }
        print("✓ Government Schemes KB loaded")
    
    def get_response(self, query):
        """
        Generate government scheme-related response
        """
        query_lower = query.lower()
        
        # PM-KISAN queries
        if 'किसान' in query_lower or 'kisan' in query_lower:
            return self._format_scheme_info('pm_kisan')
        
        # Ayushman Bharat queries
        if 'इलाज' in query_lower or 'health' in query_lower:
            return self._format_scheme_info('ayushman_bharat')
        
        # Pension queries
        if 'पेंशन' in query_lower or 'pension' in query_lower:
            return self._format_scheme_info('pension')
        
        return "सरकारी योजनाओं के बारे में पूछें: PM-KISAN, आयुष्मान भारत, पेंशन योजना आदि।"
    
    def _format_scheme_info(self, scheme_key):
        """
        Format scheme information for user
        """
        scheme = self.schemes[scheme_key]
        response = f"{scheme['name']}\n"
        response += f"पात्रता: {scheme['eligibility']}\n"
        response += f"लाभ: {scheme['benefit']}\n"
        response += f"जरूरी दस्तावेज: {scheme['documents']}\n"
        response += "नजदीकी CSC या ग्राम पंचायत में आवेदन करें।"
        return response
