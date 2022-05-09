import streamlit as st
from dictionary import bin_to_char

# CONFIG

st.set_page_config(
    page_title="Binary Translator",
    page_icon="🤖",
    initial_sidebar_state="collapsed",
)

# FONCTIONS

def format_binary_code(binary_code):
    '''
    Add a space every 8 characters.
    Input: Binary code with no spaces
    Return: list of binary codes
    '''
    formated_text = ''.join(f'{char} ' if i % 8 == 0 else char for i, char in enumerate(binary_code, start=1))
    return formated_text.split()
    

def format_answer(text, space):
    '''
    Format text to add a newline every 80 characters.
    Input: string
    Return: 
    '''
    nb_char = 81 if space else 80
    return ''.join(f'{char}\n' if i % nb_char == 0 else char for i, char in enumerate(text, start=1))


def convert_to_text(text):
    '''
    Convert Binary code to text
    Input: string
    Retrun: string
    '''
    list_codes = format_binary_code(txt)
    try:
        answer = ''.join(bin_to_char[code] for code in list_codes)
    except KeyError:
        st.error("This isn't a valid binary code")
        st.stop()
    return answer


def convert_to_binary(text, space):
    '''
    Convert text to binary code
    Input: string and type of delimiter between each binary code.
    Retrun: string
    '''
    delimiter = ' ' if space else ''
    try:
        answer = delimiter.join(list(bin_to_char.keys())[list(bin_to_char.values()).index(char)] for char in text)
    except KeyError:
        st.error("One of charcaters on your text is not supported")
        st.stop()
    return answer

# MAIN

st.title('Talk to robots 🤖')
st.header('Binary Translator')

space = False
col1, col2 = st.columns([1, 2])
with col1:
    convert = st.radio('Convert', [
        'To Text',
        'To Binary'
    ])
    if convert == 'To Binary':
        space = st.checkbox('Output with spaces')
with col2:
    if convert == 'To Binary':
        value, help = 'Write your Text.', None
    elif convert == 'To Text':
        value = '01010111011100100110100101110100011001010010000001111001011011110111010101110010001000000101010001100101011110000111010000101110'
        help = 'Format : 1011011101110011 (no spaces or delimiters)'
    txt = st.text_area(
        'Text to translate', 
        value=value, 
        help=help,
        )

if convert == 'To Text':
    answer = convert_to_text(txt)
elif convert == 'To Binary':
    delimiter = ' ' if space else ''
    answer = convert_to_binary(txt, space)

st.markdown('---')
st.subheader('The translation')
st.code(format_answer(answer, space))