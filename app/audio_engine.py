import base64
from elevenlabs.client import ElevenLabs

my_api_key = "YOUR_ELEVEN"
client = ElevenLabs(api_key=my_api_key)

def generate_warning_audio(detected_objects):
    items_str = ", ".join(detected_objects) if detected_objects else "unidentified hazards"
    script = f"Alert. Critical situation detected. Visual analysis confirms the presence of {items_str}. All personnel must evacuate the immediate zone. Emergency services have been pinged."
    
    try:
        audio = client.generate(
            text=script,
            voice="Rachel",
            model="eleven_monolingual_v1"
        )
        
        if type(audio) is bytes:
            audio_bytes = audio
        else:
            audio_bytes = b"".join([chunk for chunk in audio])
            
        audio_base64 = base64.b64encode(audio_bytes).decode('utf-8')
        return script, audio_base64
        
    except Exception as e:
        print(f"ELEVENLABS ERROR CAUGHT: {e}")
        return script, None