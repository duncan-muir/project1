# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by replacing
    all `T` to `U`
    """
    return "".join(["U" if base == "T" else base for base in seq])


def reverse_transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by replacing
    all `T` to `U` then reverses the sequence
    """

    # transcribe using above function
    transcription = transcribe(seq)

    # reverse string by indexing from last to first
    reverse = ""
    i = len(transcription) - 1
    while i >= 0:
        reverse += transcription[i]
        i -= 1

    return reverse
