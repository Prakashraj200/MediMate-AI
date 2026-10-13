import re


def preprocess_clinical_text(text):
    """Normalize and clean user input string."""
    if not text:
        return ""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s\-\.]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text


def calculate_keyword_similarity(text, keyword_list):
    """Score query relevance against medical dictionary terms."""
    cleaned = preprocess_clinical_text(text)
    words = set(cleaned.split())
    matches = [kw for kw in keyword_list if kw in cleaned or any(w == kw for w in words)]
    confidence = len(matches) / max(len(keyword_list), 1)
    return matches, round(min(confidence * 2.5, 1.0), 2)
