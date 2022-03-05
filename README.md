# Hacker_Street_Boys
Mined Dataset 22 Health Care

Introduction:
In this project we have created a python program which converts real time voice to text and some NLP models are used on the text for pre-processing.

Prerequisites & Installations:
\*\*All the installations should be done on terminal and in the given sequence.

1. speech_recognition
   -pip install speech_recognition
   -conda install pyaudio

2. spacy
   -pip install spacy
   -python -m spacy download en_core_web_lg

3. scispacy
   -pip install spacy
   -pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_core_sci_sm-0.4.0.tar.gz
   -pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_ner_bc5cdr_md-0.4.0.tar.gz

4. negspacy
   -pip install negspacy

Features:

- Name, Age, Medicine and Disease/Symptoms are predicted using the real time audio.

Instructions to run the project:

1. First run the speech_to_text.py file which converts real-time audio to text and stores it in patient.txt file.
2. After that, run extract_info.py which takes input of the patient.txt file and applies pre-processing and extract meaningful information.
3. The third file i.e., symptom_prediction.ipynb predicts the disease/symptoms from the input provided in the text form.

Modules + files that are part of this project:

1. speech_to_text.py
2. extract_info.py
3. symptom_prediction.ipynb
4. overview-of-recordings.csv (Dataset)

\*\*ALL THE INSTALLATION AND WORKING INSTRUCTIONS IN THIS FILE ARE MEANT FOR WINDOWS USERS

TEAM 4 DETAILS:

- MIHIR BHANDERI - 19BCE023
- DEVANSH BHATT - 19BCE024
- DEV PATEL - 19BCE047
- DHAIRYA JADAV - 19BCE050
