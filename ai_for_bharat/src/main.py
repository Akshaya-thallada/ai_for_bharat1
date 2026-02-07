"""
BharatSaarthi - Main Entry Point
Offline Voice-First AI Guide for Rural Citizens
"""

from nlp.intent_classifier import IntentClassifier
from core.ai_engine import BharatSaarthiEngine

def main():
    print("🇮🇳 BharatSaarthi - Digital Village Helper")
    print("=" * 50)
    
    # Initialize components
    intent_classifier = IntentClassifier()
    ai_engine = BharatSaarthiEngine()
    
    print("\n✓ All systems initialized (Offline Mode)")
    print("✓ Ready to assist in local languages")
    print("✓ Text-based demo (Voice coming soon)")
    print("\n" + "=" * 50)
    print("Try these sample queries:")
    print("1. मेरी धान की फसल पर दाग हैं")
    print("2. बच्चे के टीके कब लगते हैं")
    print("3. मुझे पेंशन मिलेगी")
    print("=" * 50)
    print("\nType your query or 'exit' to quit\n")
    
    while True:
        # Text input for demo
        user_input = input("आप (You): ")
        
        if user_input.lower() in ['exit', 'quit', 'बाहर', '']:
            print("\n✓ धन्यवाद! (Thank you!)")
            print("✓ BharatSaarthi - Serving Rural India")
            break
        
        # Process query
        intent = intent_classifier.classify(user_input)
        response = ai_engine.process(user_input, intent)
        
        print(f"\n🤖 BharatSaarthi: {response}\n")
        print("-" * 50 + "\n")

if __name__ == "__main__":
    main()
