import streamlit as st
import pandas as pd


def get_max(lista):
    array = [0, 0, 0, 0]
    array[0] = lista.count("A")
    array[1] = lista.count("B")
    array[2] = lista.count("C")
    array[3] = lista.count("D")
    return array.index(max(array))


st.title("Che tipo sei? - ***S. Valentino Edition***")
df = pd.read_csv("D:/Escritorio/San_Valentin/domande.csv")
risposte = pd.read_csv("D:/Escritorio/San_Valentin/risposte.csv")
risposta = [0, 0, 0, 0, 0, 0, 0, 0]
for i in range(8):
    st.write(i + 1)
    risposta[i] = st.selectbox(
        df.loc[i]["domanda"], df.loc[i][-4::]).split("-")[0]
if st.checkbox("Concludi!"):
    if st.button("Scopri il risultato!"):
        st.write("A S.Valentino sei: ",
                 risposte.loc[get_max(risposta)]["tipo"])

