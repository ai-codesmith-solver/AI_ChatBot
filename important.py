from a4f_local import A4F

client = A4F()

try:
    audio_bytes = client.audio.speech.create(
        model="tts-1",  # Model name (currently informational)
        input="Aye Dada, prem korle ekta din moton reply ashe na, ar ei ChatGPT toh ekdom instant! Ei duniya-r logic ami bujhte parchi na re! Ar ekhon toh pocket khali, sudhu dim ar Maggi diye ‘fine dining’ cholche!!",
        voice="shimmer"   # Choose a supported voice
    )
    with open("output.mp3", "wb") as f:
        f.write(audio_bytes)
    print("Generated output.mp3")
except Exception as e:
    print(f"An error occurred: {e}")