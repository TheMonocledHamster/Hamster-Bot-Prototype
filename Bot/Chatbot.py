import pyttsx3
import vosk
import os
import sys
import argparse
import queue
import sounddevice as sd
import random
import json


"""Initialize queue for speech-to-text"""
speechFlow = queue.Queue()

"""Initialize TTS engine"""
HamsterEngine = pyttsx3.init()


"""Thread callback for each word/audio block"""
def callback(indata,frames,time,status):
    if status:
        print(status, file=sys.stderr)
    speechFlow.put(bytes(indata))

"""Helper for argument parsing"""
def str_or_int(text_string):
    try:
        return int(text_string)
    except ValueError:
        return text_string


parser = argparse.ArgumentParser(add_help=False)

parser.add_argument(
    '-l', '--list-devices', action='store_true',
    help = "List available audio devices and exit"
)

args, other_args = parser.parse_known_args()

if args.list_devices:
    print(sd.query_devices())
    parser.exit(0)

parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    parents=[parser]
)

parser.add_argument(
    '-m', '--model', type=str, metavar='MODEL_PATH',
    help='Path to the model'
)
parser.add_argument(
    '-f', '--filename', type=str, metavar='FILENAME',
    help='audio file to store recording to'
)
parser.add_argument(
    '-d', '--device', type=str_or_int,
    help='input device (numeric ID or substring)'
)
parser.add_argument(
    '-r', '--voskrate', type=int, help='vosk sampling rate'
)
parser.add_argument(
    '-R', '--espeakrate', type=int, help='espeak sampling rate'
)
parser.add_argument(
    '-v', '--volume', type=float, help='espeak volume [0.0,1.0]'
)

args = parser.parse_args(other_args)


try:
    if args.model is None:
        args.model = "model"
    if not os.path.exists(args.model):
        print("Please place the model named as 'model' in the directory")
        parser.exit(0)
    if args.voskrate is None:
        device_info = sd.query_devices(args.device,'input')
        args.voskrate = int(device_info['default_samplerate'])
    if args.espeakrate is None:
        args.espeakrate = HamsterEngine.getProperty('rate')
    if args.volume is None:
        args.volume = HamsterEngine.getProperty('volume')
    if args.filename:
        dump = open(args.filename, 'wb')
    else:
        dump = None


    model = vosk.Model(args.model)


    with sd.RawInputStream(samplerate=args.voskrate,blocksize = 8000, device=args.device, dtype='int16', channels=1, callback=callback):
        recognizer = vosk.KaldiRecognizer(model,args.voskrate)
        print('*'*80)
        print('Ctrl+C to stop')

        while True:
            data = speechFlow.get()
            if recognizer.AcceptWaveform(data=data):
                print(recognizer.Result())
            else:
                continue


except Exception as e:
    parser.exit(type(e).__name__+': '+str(e))