"""
Unit tests for Intent Classifier
"""

import sys
sys.path.append('../src')

from nlp.intent_classifier import IntentClassifier

def test_agriculture_intent():
    classifier = IntentClassifier()
    
    # Hindi queries
    assert classifier.classify("मेरी फसल पर दाग हैं") == "agriculture"
    assert classifier.classify("खेत में खाद कब डालें") == "agriculture"
    
    # English queries
    assert classifier.classify("My crop has disease") == "agriculture"
    
    print("✓ Agriculture intent tests passed")

def test_healthcare_intent():
    classifier = IntentClassifier()
    
    # Hindi queries
    assert classifier.classify("बच्चे को टीका लगवाना है") == "healthcare"
    assert classifier.classify("बुखार की दवाई चाहिए") == "healthcare"
    
    # English queries
    assert classifier.classify("Need vaccine information") == "healthcare"
    
    print("✓ Healthcare intent tests passed")

def test_government_intent():
    classifier = IntentClassifier()
    
    # Hindi queries
    assert classifier.classify("मुझे पेंशन योजना की जानकारी चाहिए") == "government"
    assert classifier.classify("किसान योजना के लिए आवेदन") == "government"
    
    # English queries
    assert classifier.classify("How to apply for pension scheme") == "government"
    
    print("✓ Government intent tests passed")

def test_general_intent():
    classifier = IntentClassifier()
    
    assert classifier.classify("नमस्ते") == "general"
    assert classifier.classify("Hello") == "general"
    
    print("✓ General intent tests passed")

if __name__ == "__main__":
    test_agriculture_intent()
    test_healthcare_intent()
    test_government_intent()
    test_general_intent()
    print("\n✅ All tests passed!")
