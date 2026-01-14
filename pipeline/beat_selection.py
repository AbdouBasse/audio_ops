def select_beat(audio_features):
    tempo = audio_features.get("tempo", 0)

    if tempo == 0 or tempo < 90:
        return "beat_lofi.wav"
    elif 90 <= tempo < 120:
        return "beat_pop.wav"
    else:
        return "beat_trap.wav"


if __name__ == "__main__":
    test_audio = {"tempo": 85}
    print(select_beat(test_audio))

