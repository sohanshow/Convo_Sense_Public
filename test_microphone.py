#!/usr/bin/env python3

import argparse
import queue
import sys
import sounddevice as sd
import time
import eel
from threading import Thread

import os

from vosk import Model, KaldiRecognizer

q = queue.Queue()

tmp = ""





def loadingMicReady():
    print("JavaScript is ready")
    eel.loadListening()

def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text

def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

def listen():
    global tmp
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        "-l", "--list-devices", action="store_true",
        help="show list of audio devices and exit")
    args, remaining = parser.parse_known_args()
    if args.list_devices:
        print(sd.query_devices())
        parser.exit(0)
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        parents=[parser])
    parser.add_argument(
        "-f", "--filename", type=str, metavar="FILENAME",
        help="audio file to store recording to")
    parser.add_argument(
        "-d", "--device", type=int_or_str,
        help="input device (numeric ID or substring)")
    parser.add_argument(
        "-r", "--samplerate", type=int, help="sampling rate")
    args = parser.parse_args(remaining)

    try:
        if args.samplerate is None:
            device_info = sd.query_devices(args.device, "input")
            # soundfile expects an int, sounddevice provides a float:
            args.samplerate = int(device_info["default_samplerate"])

        model = Model(lang="en-us")

        if args.filename:
            dump_fn = open(args.filename, "wb")
        else:
            dump_fn = None

        with sd.RawInputStream(samplerate=args.samplerate, blocksize = 8000, device=args.device,
                               dtype="int16", channels=1, callback=callback):


            print("#" * 80)
            print("Press Ctrl+C to stop the recording")
            print("#" * 80)

            print("Going to execute it.")


            rec = KaldiRecognizer(model, args.samplerate)
            starttime = time.time()

            loadingMicReady()
            eel.sleep(1)
            while True:
                data = q.get()
                if rec.AcceptWaveform(data):
                    # elapsed_time = time.time() - starttime
                    # print(elapsed_time)
                    k = rec.Result()
                    print(k)
                    #word_list = k.split()
                    #length_list = len(word_list)
                    #if length_list != 0:
                    #for i in range(length_list):
                    #nlp = word_list[0]
                    # print(type(nlp))
                    #print(nlp)
                    #f = open('text.txt', 'a')
                    tmp = tmp + " "+ k[14:len(k)-3]
                    #f.write(tmp)

                #print(nlp[10:len(nlp)-2])
                #f.write(" ")
                #f.close()
                #word_list.pop(0)
                # else:
                #     #print("Listening now")
                if dump_fn is not None:
                    dump_fn.write(data)


    except KeyboardInterrupt:
        print("\nDone")
        #f = open('testing.txt', 'w')
        #f.close()
        parser.exit(0)
    except Exception as e:
        parser.exit(type(e).__name__ + ": " + str(e))

def start_listen():
    listen_thread = Thread(target=listen)
    listen_thread.start()

