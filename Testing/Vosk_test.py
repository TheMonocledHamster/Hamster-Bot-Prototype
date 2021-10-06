import argparse
import os
import queue
import sounddevice as sd
import vosk
import sys

q = queue.Queue()

"""Called from a separate thread for each audio block"""
def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

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
    help='Path to the model')
parser.add_argument(
    '-f', '--filename', type=str, metavar='FILENAME',
    help='audio file to store recording to')
parser.add_argument(
    '-d', '--device', type=str_or_int,
    help='input device (numeric ID or substring)')
parser.add_argument(
    '-r', '--samplerate', type=int, help='sampling rate')
args = parser.parse_args(other_args)

try:
    if args.model is None:
        args.model = "Testing/model"
    if not os.path.exists(args.model):
        print("Please place the model as model in the directory")
        parser.exit(0)
    if args.samplerate is None:
        device_info = sd.query_devices(args.device,'input')
        args.samplerate = int(device_info['default_samplerate'])

    model = vosk.Model(args.model)

    if args.filename:
        dump = open(args.filename, "wb")
    else:
        dump = None

    with sd.RawInputStream(samplerate=args.samplerate, blocksize = 8000, device=args.device, dtype='int16', channels=1, callback=callback):
        print('*'*80)
        print('Ctrl+C to stop')

        rec = vosk.KaldiRecognizer(model, args.samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data=data):
                print(rec.Result())
            else:
                continue

except KeyboardInterrupt:
    print('\nDone')
    parser.exit(0)
except Exception as e:
    parser.exit(type(e).__name__+': '+str(e))