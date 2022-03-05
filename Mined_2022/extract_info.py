# -*- coding: utf-8 -*-

import spacy
import scispacy
import negspacy

from negspacy.negation import Negex

# Extracting file data and preprocessing
def file(filename="patient.txt"):
    text_file = open(filename, "r")
    data = text_file.read()
    text_file.close()

    # Name and Age Extractor
    sp_lg = spacy.load('en_core_web_lg')
    for ent in sp_lg(data).ents:
        if ent.label_ == "PERSON":
            name = ent.text.strip()
            print("Name: ", name)
        elif ent.label_ == "DATE":
            age = ent.text.strip()
            if len(age) < 3:
                print("Age: ", age)

    # Negation data analyzer
    nlp = spacy.load("en_core_sci_sm")
    nlp.add_pipe("negex")
    neg_doc = nlp(data)
    negation = {}
    for w in neg_doc.ents:
        negation[w.text] = w._.negex

    # Diseases/Symptoms and Medicine Extractor
    disease_model = spacy.load("en_ner_bc5cdr_md")
    doc = disease_model(data)
    for ent in doc.ents:
        if ent.label_ == "CHEMICAL":
            medicine = ent.text
            print("Medicine:", medicine)
        elif ent.label_ == "DISEASE":
            disease = ent.text

            # Negated Disease is rulled out
            if disease in negation:
                if negation[disease] == False:
                    print("Disease/Symptoms:", disease)

if __name__ == "__main__":
    file()
