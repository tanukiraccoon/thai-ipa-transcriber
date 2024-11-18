# -*- coding: utf-8 -*-
import json

from .constants import (
    CONSONANT_CLUSTERS,
    FINAL_CONSONANTS,
    INITIAL_CONSONANTS,
    PATTERN,
    TONES_MARK,
    VOWELS,
)

class ThaiIPA:
    def __init__(self, ipa: str = "pʰrɯk4"):
        self.__ipa: str = ipa
        if match := PATTERN.match(self.__ipa):
            self.__extract_ipa(match)
        else:
            raise Exception(f"Unexpected IPA: {self.__ipa}.")

        self.__process()

    def __extract_ipa(self, match):
        (
            self._initial_en,
            self._cluster_en,
            self._vowel_en,
            self._final_en,
            self._tone,
        ) = match.groups()
        self._tone = int(self._tone)

    def __process(self):
        self.__select_initial_th()
        self.__select_cluster_th()
        self.__select_vowel_th()
        self.__select_final_th()
        self.__select_tone_mark()

    @property
    def initial_en(self):
        return self._initial_en

    @initial_en.setter
    def initial_en(self, char):
        self._initial_en = char
        self.__process()

    @property
    def cluster_en(self):
        return self._cluster_en

    @cluster_en.setter
    def cluster_en(self, char):
        self._cluster_en = char
        self.__process()

    @property
    def vowel_en(self):
        return self._vowel_en

    @vowel_en.setter
    def vowel_en(self, char):
        self._vowel_en = char
        self.__process()

    @property
    def final_en(self):
        return self._final_en

    @final_en.setter
    def final_en(self, char):
        self._final_en = char
        self.__process()

    @property
    def tone(self):
        return self._tone

    @tone.setter
    def tone(self, num):
        self._tone = int(num)
        self.__process()
        
    @property
    def initial_th(self):
        return self._initial_th

    @property
    def cluster_th(self):
        return self._cluster_th

    @property
    def vowel_ht(self):
        return self._vowel_th
    
    @property
    def final_th(self):
        return self._final_th

    @property
    def tone_mark(self):
        return self._tone_mark

    @tone.setter
    def tone(self, num):
        self._tone = int(num)
        self.__process()

    @property
    def is_long(self):
        return "ː" in self._vowel_en

    @property
    def is_dead(self):
        return self._final_en in ["k", "p", "t"] or (
            not self.is_long and not self._final_en
        )

    @property
    def is_open(self):
        return not self._final_en

    @property
    def is_mid(self):
        return len(INITIAL_CONSONANTS[self._initial_en]) == 1

    def __select_initial_th(self):
        if self.is_mid:
            self._initial_th = INITIAL_CONSONANTS[self._initial_en]
        else:
            self._initial_th = self.__get_initial_th_by_tone()

    def __get_initial_th_by_tone(self):
        match self._tone:
            case 1 | 3 | 4:
                return INITIAL_CONSONANTS[self._initial_en][0]
            case 2 | 5:
                return INITIAL_CONSONANTS[self._initial_en][1]
            case _:
                raise Exception(
                    f"Unexpected tone value: {self._tone}, IPA: {self._ipa} in function __select_initial_th"
                )

    def __select_cluster_th(self):
        self._cluster_th = CONSONANT_CLUSTERS.get(self._cluster_en, "")

    def __select_vowel_th(self):
        if (self._vowel_en, self._final_en) in [("a", "w"), ("ɤː", "j")]:
            self._vowel_th = VOWELS[self._vowel_en][2]
        else:
            self._vowel_th = (
                VOWELS[self._vowel_en][0] if self.is_open else VOWELS[self._vowel_en][1]
            )

    def __select_final_th(self):
        if (self._vowel_en, self._final_en) == ("a", "w"):
            self._final_th = ""
        else:
            self._final_th = FINAL_CONSONANTS.get(self._final_en, "")

    def __select_tone_mark(self):
        if self.is_mid:
            if self.is_dead and self._tone == 2:
                self._tone_mark = TONES_MARK[1]
            else:
                self._tone_mark = TONES_MARK[self._tone]
        else:
            self._tone_mark = self.__get_tone_mark_by_initial()

    def __get_tone_mark_by_initial(self):
        match self._tone:
            case 1:
                return TONES_MARK[self._tone]
            case 2:
                return TONES_MARK[1] if self.is_dead else TONES_MARK[self._tone]
            case 3:
                return (
                    TONES_MARK[1] if (self.is_dead and self.is_long) else TONES_MARK[2]
                )
            case 4:
                return (
                    TONES_MARK[1]
                    if (self.is_dead and not self.is_long)
                    else TONES_MARK[3]
                )
            case 5:
                return TONES_MARK[self._tone] if self.is_dead else TONES_MARK[1]
            case _:
                raise Exception(
                    f"Unexpected tone value: {self._tone}, IPA: {self.ipa} in function __select_tone_mark"
                )

    def spell(self):
        s = self._initial_th + self._cluster_th
        s = self._vowel_th.replace("อ", s, 1)
        s = s.replace("-", self._tone_mark)
        s = s + self._final_th
        return s

    def get_components(self, lang=None, additional=False):
        
        addit = (self.is_long, self.is_dead, self.is_mid, self.is_open) if additional else ()
        
        en_components = (
            self._initial_en,
            self._cluster_en,
            self._vowel_en,
            self._final_en,
            self._tone,
        )

        th_components = (
            self._initial_th,
            self._cluster_th,
            self._vowel_th,
            self._final_th,
            self._tone_mark,
        )

        if lang == "en":
            return common_components + addit
        elif lang == "th":
            return thai_components + addit
        else:
            return [common_components + addit, thai_components + addit]