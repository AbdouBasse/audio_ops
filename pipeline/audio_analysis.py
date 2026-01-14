import librosa

def analyze_audio(path):
    y, sr = librosa.load(path)
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

    return {
        "duration": librosa.get_duration(y=y, sr=sr),
        "tempo": tempo
    }

if __name__ == "__main__":
    info = analyze_audio("/home/abasse/DevOps_Audio/data/raw_audio/sample.wav")
    print(info)

