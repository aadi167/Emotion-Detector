import json
import requests

def emotion_detector(text_to_analyse):
    if not text_to_analyse.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    response_dict = json.loads(response.text)

    emotions = {
        'anger': response_dict['emotion']['anger'],
        'disgust': response_dict['emotion']['disgust'],
        'fear': response_dict['emotion']['fear'],
        'joy': response_dict['emotion']['joy'],
        'sadness': response_dict['emotion']['sadness']
    }

    emotions['dominant_emotion'] = max(emotions, key=emotions.get)
    return emotions
