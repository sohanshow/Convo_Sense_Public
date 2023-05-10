import asyncio
import azure.cognitiveservices.speech as speechsdk


# Set up the Azure Speech Service configuration
subscription_key = "5ba5cf63-a89f-4e88-9eb3-72fde1f92f6f"
service_region = "westus"

def recognize_speech_once():
    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=service_region)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config)

    print("Speak into your microphone.")
    result = speech_recognizer.recognize_once()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(result.text))
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition was canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))

if __name__ == "__main__":
    recognize_speech_once()