import activateMic
import json
from dejavu import Dejavu
from dejavu.logic.recognizer.file_recognizer import FileRecognizer
from dejavu.logic.recognizer.microphone_recognizer import MicrophoneRecognizer

# load config from a JSON file (or anything outputting a python dictionary)
config = {
    "database": {
        "host": "db",
        "user": "postgres",
        "password": "password",
        "database": "dejavu"
    },
    "database_type": "postgres"
}

def runDejavu():
    # create a Dejavu instance
    djv = Dejavu(config)

    # service.py executed as script
    # do something
    activateMic.micStart()
    results = djv.recognize(FileRecognizer, "mp3/recording.wav")
    print(f"From file we recognized: {results}\n")


if __name__ == '__main__':
    runDejavu()
    
    

