"""
Core NLP analysis service.
This is intentionally simple so it can be upgraded later.
"""
def analyze_text(text:str):
    suspicious_words = ["hate","kill","attack"]
    found = [w for w in suspicious_words if w in text.lower()]
    return {
        "prediction":"Potential Hate Speech" if found else "No Hate Speech Detected",
        "flagged_terms": found,
        "explanation":"Detected potentially hostile terms." if found else "No obvious indicators found."
    }
