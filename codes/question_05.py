

def reverse_characters_string(text: str) -> str:
    """Função que inverte os caracteres de um string."""
    new_text = ''
    text_size = len(text)
    while text_size:
        new_text += text[text_size-1]
        text_size -= 1

    return new_text


print(reverse_characters_string("Texto para teste"))