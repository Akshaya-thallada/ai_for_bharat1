"""
Quick Demo Script for BharatSaarthi
Run this for automated demo
"""

import sys
sys.path.append('src')

from nlp.intent_classifier import IntentClassifier
from core.ai_engine import BharatSaarthiEngine

def run_demo():
    print("🇮🇳 BharatSaarthi - Automated Demo")
    print("=" * 60)
    
    # Initialize
    classifier = IntentClassifier()
    engine = BharatSaarthiEngine()
    
    print("✓ System initialized\n")
    
    # Demo queries
    queries = [
        ("मेरी धान की फसल पर दाग हैं", "Agriculture"),
        ("बच्चे को टीका लगवाना है", "Healthcare"),
        ("मुझे पेंशन योजना की जानकारी चाहिए", "Government"),
        ("खेत में खाद कब डालें", "Agriculture"),
        ("किसान योजना के बारे में बताओ", "Government")
    ]
    
    for query, domain in queries:
        print(f"📝 Query: {query}")
        print(f"🎯 Expected Domain: {domain}")
        
        intent = classifier.classify(query)
        print(f"🔍 Detected Intent: {intent}")
        
        response = engine.process(query, intent)
        
        print(f"🤖 Response:\n{response}")
        print("-" * 60 + "\n")

if __name__ == "__main__":
    run_demo()
