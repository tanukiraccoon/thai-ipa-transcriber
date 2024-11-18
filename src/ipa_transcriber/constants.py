# -*- coding: utf-8 -*-
import re
INITIAL_CONSONANTS = {
    'b': 'บ',
    'd': 'ด',
    'f': ('ฟ','ฝ'),
    'h': ('ฮ','ห'),
    'j': ('ย','หย'),
    'k': 'ก',
    'kʰ': ('ค','ข'),
    'l': ('ล','หล'),
    'm': ('ม','หม'),
    'n': ('น','หน'),
    'ŋ': ('ง','หง'),
    'pʰ': ('พ','ผ'),
    'p': 'ป',
    'r': ('ร','หร'),
    's': ('ซ','ส'),
    'tʰ': ('ท','ถ'),
    'c': 'จ',
    'cʰ': ('ช','ฉ'),
    't': 'ต',
    'w': ('ว','หว'),
    'ʔ': 'อ'
}


CONSONANT_CLUSTERS = {
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
# key: (open_syl, close_syl, exceptional_syl)
SHORT_VOWELS = {
    'a': ('อ-ะ', 'อั-' ,'เอ-า'),
    'e': ('เอ-ะ', 'เอ็-'),
    'ɛ': ('แอ-ะ', 'แอ็-'),
    'i': ('อิ-', 'อิ-'),
    'o': ('โอ-ะ', 'อ-'),
    'ᴐ': ('เอ-าะ', 'อ็-อ'),
    'u': ('อุ-', 'อุ-'),
    'ɯ': ('อึ-', 'อึ-'),
    'ɤ': ('เอ-อะ', 'เอ-อะ')
}

LONG_VOWELS = {
    'aː': ('อ-า','อ-า'),
    'eː': ('เอ-','เอ-'),
    'ɛː': ('แอ-','แอ-'),
    'iː': ('อี-','อี-'),
    'oː': ('โอ-','โอ-'),
    'ᴐː': ('อ-อ','อ-อ'),
    'uː': ('อู-','อู-'),
    'ɯː': ('อื-อ', 'อื-'),
    'ɤː': ('เอ-อ', 'เอิ-','เอ-')
}
DIPTHONGS = {
    'ia': ('เอี-ยะ','เอี-ยะ'), # This sound does not exist in the Thai language.
    'iːa': ('เอี-ย','เอี-ย'),
    'ɯa': ('เอื-อะ','เอื-อะ'), # This sound does not exist in the Thai language.
    'ɯːa': ('เอื-อ','เอื-อ'),
    'ua': ('อั-วะ', 'อั-วะ'), # This sound does not exist in the Thai language.
    'uːa': ('อั-ว', 'อ-ว'),
}

TONES_MARK = {
    1: '',
    2: '่',
    3: '้',
    4: '๊',
    5: '๋',
}

# Merging for all vowels type
VOWELS = {**SHORT_VOWELS, **LONG_VOWELS, **DIPTHONGS}

# Sorting keys by length
vowels_sort = sorted(VOWELS, key=len, reverse=True)
initial_consonatns_sort = sorted(INITIAL_CONSONANTS, key=len, reverse=True)

# Compile the regex pattern
initial_consonants_pattern = '|'.join(initial_consonatns_sort)
clusters_pattern = '|'.join(CONSONANT_CLUSTERS)
vowels_pattern = '|'.join(vowels_sort)
final_consonants_pattern = '|'.join(FINAL_CONSONANTS)
tones_pattern = '|'.join(map(str, TONES_MARK))

PATTERN = re.compile(
    f"({initial_consonants_pattern})([{clusters_pattern}]?)?({vowels_pattern})([{final_consonants_pattern}]?)?({tones_pattern})?"
)

# THAI_PANGRAM1 = 'นายสังฆภัณฑ์เฮงพิทักษ์ฝั่งผู้เฒ่าซึ่งมีอาชีพเป็นฅนขายฃวดถูกตำรวจปฏิบัติการจับฟ้องศาลฐานลักนาฬิกาคุณหญิงฉัตรชฎาฌานสมาธิ'
# THAI_PANGRAM2 = 'เป็นมนุษย์สุดประเสริฐเลิศคุณค่ายังดีกว่าฝูงสัตว์เดรัจฉานจงฝ่าฟันพัฒนาวิชาการอย่าล้างผลาญฤาเข่นฆ่าบีฑาใครไม่ถือโทษโกรธแช่งซัดฮึดฮัดด่าหัดอภัยเหมือนกีฬาอัชฌาศัยปฏิบัติประพฤติกฎกำหนดใจพูดจาให้จ๊ะจ๋าน่าฟังเอย'