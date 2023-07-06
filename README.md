# Thai IPA Transcriber

Thai IPA Transcriber is a Python script that allows you to convert Thai IPA (International Phonetic Alphabet) transcriptions of single syllables to their corresponding Thai spelling letters. It provides a convenient way to map Thai IPA symbols to their respective characters based on the phonetic rules and conventions of the Thai language.

## Usage

1. Make sure you have Python installed on your system.
2. Import the `IPA` class from `ipa_transcriber.py`
3. Create an instance of the `IPA` class with a Thai IPA transcription of a single syllable as the input.
4. Access the Thai spelling letters and other properties using the instance attributes.
5. Use the `spell()` method to obtain the Thai word spelled with the Thai spelling letters.

## Example

```python
from ipa_transcriber import IPA

ipa = IPA('pʰrɯk4') # พฤกษ์

# Accessing the IPA letters
print(ipa.initial_en)    # Output: pʰ
print(ipa.cluster_en)    # Output: r
print(ipa.vowel_en)      # Output: ɯ
print(ipa.final_en)      # Output: k

# Accessing the Thai spelling letters
print(ipa.initial_th)    # Output: พ
print(ipa.cluster_th)    # Output: ร
print(ipa.vowel_th)      # Output: อึ-
print(ipa.final_th)      # Output: ก

# Additional information
print(ipa.tone)          # Output: 4
print(ipa.tone_mark)     # Output: ''
print(ipa.dead_syl)      # Output: True
print(ipa.long_vow)      # Output: False

# Getting the Thai word spelled with Thai spelling letters
print(ipa.spell())       # Output: พรึก
```
## Limitation
- The transcriber assumes a one-syllable input and may not handle multi-syllable transcriptions correctly.
- If the Thai tone is Tone 3 (falling tone / เสียงโท) and the original word uses a high-class letter, this script will use a low-class letter for spelling. Please keep this in mind when using the transcriber.
- When spelling the vowel sounds "aj" represented by the characters "ไ-" and "ใ-", the transcriber will use the characters "-ัย" instead.
