from unidecode import unidecode
import matplotlib.pyplot as plt


def add_data(df):
     df['contenido'] = df['contenido'].apply(unidecode).str.lower()
     df['length'] = df['contenido'].apply(len)

def preprocess(text):
    excluir=[]
    preprocess_text = re.sub(r'\b\d{7,}\b|\b\d{,5}\b|\w*/\w*',' ',text)
    preprocess_text = re.sub(r'\s{2,}',' ',preprocess_text)
    doc=nlp(preprocess_text)
    for t in doc.ents:
      if t.label_ == "PER":
        excluir.append(t.text)
    tokens = [t.text for t in list(nlp(preprocess_text)) if not t.is_stop and len(t.text)>3 and t.text not in excluir]
    preprocess_text=" ".join(tokens)
    return preprocess_text
