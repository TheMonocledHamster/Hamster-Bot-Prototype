import pyttsx3
import vosk
import os
import sys
import argparse
import queue
import sounddevice
import random
import json
from time import sleep


speechFlow = queue.Queue()

HamsterEngine = pyttsx3.init()


"""Follows the chatbot conversation script"""
def hamster_convo(HamsterEngine, ConvoScript, Recognizer):
    HamsterEngine.say("Greetings!")
    HamsterEngine.runAndWait()
    print("In conversation...")
    HamsterEngine.say(ConvoScript["question"])
    HamsterEngine.runAndWait()
    while True:
        data = speechFlow.get()
        if Recognizer.AcceptWaveform(data=data):
            word = json.loads(Recognizer.Result())["text"]
            if word in ConvoScript["response"]["yea"]:
                HamsterEngine.say([ConvoScript["trivia"][0]])
                HamsterEngine.runAndWait()
                HamsterEngine.say([ConvoScript["trivia"][random.randint(1, 13)]])
                HamsterEngine.runAndWait()
                break
            elif word in ConvoScript["response"]["nope"]:
                break
            elif not word:
                continue
            else:
                HamsterEngine.say("I beg your pardon")
                HamsterEngine.runAndWait()
                sleep(1)
                continue
        else:
            continue
    HamsterEngine.say("Okay, have a good day!")
    HamsterEngine.runAndWait()
    return
    


"""Thread callback for each word/audio block"""
def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    speechFlow.put(bytes(indata))


"""Helper for argument parsing"""
def str_or_int(text_string):
    try:
        return int(text_string)
    except ValueError:
        return text_string


Parser = argparse.ArgumentParser(add_help=False)

Parser.add_argument(
    '-l', '--list-devices', action='store_true',
    help = "List available audio devices and exit"
)

args, other_args = Parser.parse_known_args()

if args.list_devices:
    print(sounddevice.query_devices())
    Parser.exit(0)

Parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    parents=[Parser]
)

Parser.add_argument(
    '-m', '--model', type=str, metavar='MODEL_PATH',
    help='Path to the model'
)
Parser.add_argument(
    '-f', '--filename', type=str, metavar='FILENAME',
    help='audio file to store recording to'
)
Parser.add_argument(
    '-d', '--device', type=str_or_int,
    help='input device (numeric ID or substring)'
)
Parser.add_argument(
    '-r', '--voskrate', type=int, help='vosk sampling rate'
)
Parser.add_argument(
    '-R', '--espeakrate', type=int, help='espeak sampling rate'
)
Parser.add_argument(
    '-v', '--volume', type=float, help='espeak volume [0.0,1.0]'
)

args = Parser.parse_args(other_args)


try:
    with open('HamsterConvo.json', 'r') as json_file:
        ConvoScript = json.load(json_file)
except Exception as e:
    print(str(e))


try:
    if args.model is None:
        args.model = "model"
    if not os.path.exists(args.model):
        print("Please place the model named as 'model' in the directory")
        Parser.exit(0)
    if args.voskrate is None:
        device_info = sounddevice.query_devices(args.device, 'input')
        args.voskrate = int(device_info['default_samplerate'])
    if args.espeakrate is None:
        args.espeakrate = 160
    if args.volume is None:
        args.volume = HamsterEngine.getProperty('volume')
    if args.filename:
        dump = open(args.filename, 'wb')
    else:
        dump = None


    model = vosk.Model(args.model)


    with sounddevice.RawInputStream(samplerate=args.voskrate, blocksize = 8000, device=args.device, dtype='int16',
                        channels=1, callback=callback):
        Recognizer = vosk.KaldiRecognizer(model, args.voskrate)
        print('*'*80)
        print('Ctrl+C to stop')

        while True:
            data = speechFlow.get()
            if Recognizer.AcceptWaveform(data=data) and \
                json.loads(Recognizer.Result())["text"] in ConvoScript["wake-on-command"]:
                print("Greetings!")
                hamster_convo(HamsterEngine, ConvoScript, Recognizer)
                print("Goodbye!")
                Parser.exit(0)
            else:
                continue


except KeyboardInterrupt:
    print("\nGoodbye!")
    Parser.exit(0)
except Exception as e:
    Parser.exit(type(e).__name__+': '+str(e))
