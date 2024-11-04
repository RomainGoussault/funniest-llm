import ollama

from ollama import generate

def main():

    llm = "llama3.2:1b"
    ollama.pull(llm)

    text_input : str = """
    In a small village near a dark forest, a girl named Lila found a silver key buried in her garden. Curious, she put it in her pocket and followed a narrow path leading into the trees. The path brought her to an old door built into the roots of a giant oak tree. She turned the key, and the door slowly opened. Inside, she found a magical world lit by soft starlight, with stars close enough to touch. A gentle voice spoke, “Welcome, Keeper of the Key.” As Lila stepped inside, she realized she was part of an old story waiting for her to discover its secrets.
    """

    prompt : str = "Summarize this text in three sentences: " + text_input

    a = generate(llm, prompt, stream=False)["response"]

    print(a)


if __name__ == "__main__":
    main()
