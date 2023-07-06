# -*- coding: utf-8 -*-
import re

CONSONANTS = {
    'b': 'บ',
    'd': 'ด',
    'f': ['ฟ', 'ฝ'],
    'h': ['ฮ', 'ห'],
    'j': ['ย', 'หย'],
    'k': 'ก',
    'kʰ': ['ค', 'ข'],
    'l': ['ล', 'หล'],
    'm': ['ม', 'หม'],
    'n': ['น', 'หน'],
    'ŋ': ['ง', 'หง'],
    'pʰ': ['พ', 'ผ'],
    'p': 'ป',
    'r': ['ร', 'หร'],
    's': ['ซ', 'ส'],
    'tʰ': ['ท', 'ถ'],
    'c': 'จ',
    'cʰ': ['ช', 'ฉ'],
    't': 'ต',
    'w': ['ว', 'หว'],
    'ʔ': 'อ'
}

# HIGH_C = []
MIDDLE_C = ['k','c','d','t','b','p','ʔ']
# LOW_C = []

CLUSTERS = {
    'l': 'ล',
    'r': 'ร',
    'w': 'ว'
}

FINAL_CONSONANTS = {
    'j': 'ย',
    'k': 'ก',
    'm': 'ม',
    'n': 'น',
    'ŋ': 'ง',
    'p': 'บ',
    't': 'ด',
    'w': 'ว',
    'ʔ': 'อ'
}

# '-' for tone marks
VOWELS_SHORT = {
    'ia': 'เอี-ยะ',
    'a': ['อ-ะ', 'อั-', 'เอ-า'],
    'e': ['เอ-ะ', 'เอ็-'],
    'ɛ': ['แอ-ะ', 'แอ-'],
    'i': 'อิ-',
    'o': ['โอ-ะ', 'อ-'],
    'ᴐ': ['เอ-าะ', 'อ็-อ'],
    'u': 'อุ-',
    'ɯ': 'อึ-',
    'ɤ': 'เอ-อะ'
}

VOWELS_LONG = {
    'iːa': 'เอี-ย',
    'uːa': ['อั-ว', 'อ-ว'],
    'ɯːa': 'เอื-อ',
    'aː': 'อ-า',
    'eː': 'เอ-',
    'ɛː': 'แอ-',
    'iː': 'อี-',
    'oː': 'โอ-',
    'ᴐː': 'อ-อ',
    'uː': 'อู-',
    'ɯː': ['อื-อ', 'อื-'],
    'ɤː': ['เอ-อ', 'เอิ-', 'เอ-']
}

TONES_MARK = {
    '1': '',
    '2': '่',
    '3': '้',
    '4': '๊',
    '5': '๋',
}

# Compile the regex pattern
consonant_patterns = sorted(CONSONANTS.keys(), key=len, reverse=True)
cluster_patterns = sorted(CLUSTERS.keys(), key=len, reverse=True)
MERGED_VOWELS = {**VOWELS_SHORT, **VOWELS_LONG}
vowel_patterns = sorted(MERGED_VOWELS.keys(), key=len, reverse=True)
tone_patterns = sorted(TONES_MARK.keys(), key=len, reverse=True)

pattern_consonant = '|'.join(consonant_patterns)
pattern_cluster = '|'.join(cluster_patterns)
pattern_vowel = '|'.join(vowel_patterns)
pattern_final_consonant = pattern_consonant
pattern_tone = '|'.join(tone_patterns)

PATTERN = re.compile(
    f"({pattern_consonant})([{pattern_cluster}]?)?({pattern_vowel})([{pattern_final_consonant}]?)?({pattern_tone})?"
)

PANGRAM1 = 'นายสังฆภัณฑ์เฮงพิทักษ์ฝั่งผู้เฒ่าซึ่งมีอาชีพเป็นฅนขายฃวดถูกตำรวจปฏิบัติการจับฟ้องศาลฐานลักนาฬิกาคุณหญิงฉัตรชฎาฌานสมาธิ'
PANGRAM2 = 'เป็นมนุษย์สุดประเสริฐเลิศคุณค่ายังดีกว่าฝูงสัตว์เดรัจฉานจงฝ่าฟันพัฒนาวิชาการอย่าล้างผลาญฤาเข่นฆ่าบีฑาใครไม่ถือโทษโกรธแช่งซัดฮึดฮัดด่าหัดอภัยเหมือนกีฬาอัชฌาศัยปฏิบัติประพฤติกฎกำหนดใจพูดจาให้จ๊ะจ๋าน่าฟังเอย'


    





