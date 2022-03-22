import streamlit as st
import speech_recognition as sr

recognizer1 = sr.Recognizer()
microphone1 = sr.Microphone()

def recognize_speech_from_mic(recognizer, microphone):
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")
    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Speak Now")
        audio = recognizer.listen(source)

    response = {
        "transaction": None,
        "error": None
    }

    try:
        response["transaction"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        response["error"] = "API Unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"

    return response


MyWords = recognize_speech_from_mic(recognizer=recognizer1, microphone=microphone1)

#Success Case
if MyWords["transaction"] is not None:
    MyWords["transaction"] = MyWords["transaction"].lower()
    print("Did you say: "+MyWords["transaction"])
    #Here you want to say "Yes or No". if yes, then push through algorithm.
    #if no, then you want to repeat MyWords = recognize_speech_from_mic()

#Failure Case
if (MyWords["error"] is not None):
    print("ERROR: "+MyWords["error"])
    #exit the recognize speech from mic. this would force them to press the button to resay their words



def recognize_speech_from_mic(recognizer, microphone):
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")
    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Speak Now")
        audio = recognizer.listen(source)

    response = {
        "transaction": None,
        "error": None
    }

    try:
        response["transaction"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        response["error"] = "API Unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"

    return response

def app_without_video(model):
    webrtc_ctx = webrtc_streamer(
        key="speech-to-text",
        mode=WebRtcMode.SENDONLY,
        audio_receiver_size=1024,
        client_settings=ClientSettings(
            rtc_configuration={
                "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
            },
            media_stream_constraints={"video": False, "audio": True},
        ),
    )

def Show_Page():

    st.title("English to Spanish Translator")
    st.write(""" Write Information about your work and the models and stuff here""")

    st.title("")
    st.write(""" #### Please Choose the Application Mode """)
    App_Mode = st.selectbox("App Mode", ["Sound Only", "Sound With Video"])

    if App_Mode == "Sound Only":
        print("1")
    else:
        print("2")
Show_Page()