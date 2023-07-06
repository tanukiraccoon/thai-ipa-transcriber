# -*- coding: utf-8 -*-

from .constants import PATTERN, CONSONANTS, CLUSTERS, FINAL_CONSONANTS, MERGED_VOWELS, MIDDLE_C, TONES_MARK

class IPA:
    def __init__(self, ipa):
        self.ipa = ipa

        self.initial_en = ''
        self.cluster_en = ''
        self.vowel_en = ''
        self.final_en = ''
        self.tone = ''

        self.parse_ipa()

        self.initial_th = ''
        self.cluster_th = ''
        self.vowel_th = ''
        self.final_th = ''
        self.tone_mark = ''
        
        self.dead_syl = False
        self.long_vow = False
        
        self.process()

    def process(self):
        self.isLong()
        self.isDead()
        self.ipa_to_thai()
        self.select_initial()
        self.select_vowel()
        self.select_tonemark()
       
    #แยกส่วนประกอบของ IPA
    def parse_ipa(self):
        match = PATTERN.match(self.ipa)
        if match:
            self.initial_en = match[1]
            self.cluster_en = match[2]
            self.vowel_en = match[3]
            self.final_en = match[4]
            self.tone= match[5]
    
    # สระเสียงสั้น เสียงยาว
    def isLong(self):
        # self.long_vow = 'ː' in self.ipa
        self.long_vow = 'ː' in self.vowel_en

    # คำเป็น คำตาย
    def isDead(self):
        self.dead_syl = self.final_en in ['k', 'p', 't'] or (not self.long_vow and not self.final_en)

    # Convert en to th char
    def ipa_to_thai(self):
        self.initial_th = CONSONANTS.get(self.initial_en, '')   
        self.cluster_th = CLUSTERS.get(self.cluster_en, '')  
        self.vowel_th = MERGED_VOWELS.get(self.vowel_en, '')  
        self.final_th = FINAL_CONSONANTS.get(self.final_en, '')  

    # เปลี่ยนเสียงเป็นรูป
    def tone2mark(self,tone):
        return TONES_MARK.get(tone, '')

    # เลือกพยัญชนะต้น อักษรสูงกลางต่ำ ตามเสียงวรรณยุกต์
    def select_initial(self):
        if isinstance(self.initial_th, list): # เป็นอักษรสูง/ต่ำ
            if self.tone in ['1','3','4']: # เสียงสามัญ/ตรีมีแค่อักษรต่ำ ยกเว้นเสียงโทมีทั้งคู่ เลือกใช้อักษรต่ำ => คัน1 คั่น3/ขั้น3 คั้น4 
                self.initial_th = self.initial_th[0]
            elif self.tone == '2': # เสียงเอก มีแค่อักษรสูง => ข่าน2 ขาด2 
                self.initial_th = self.initial_th[1]
            elif self.tone == '5': # เสียงจัตวามีทั้งคู่ แต่อักษรสูงมีแค่คำเป็น และอักษรต่ำมีแค่คำตาย => ขัน5 ค๋ะ5
                self.initial_th = self.initial_th[0] if self.dead_syl else self.initial_th[1]
                

    # เลือกสระที่เขียนได้มากกว่า 1 แบบ ตามตัวสะกด
    def select_vowel(self):
        if isinstance(self.vowel_th, list):
            if (self.vowel_en, self.final_en) in [('a', 'w'), ('ɤː', 'j')]: #สระ เอา เอย ลบตัวสะกดออก
                self.vowel_th = self.vowel_th[2]
                if self.final_en == 'w':
                    self.final_th = ''
            elif self.final_th: # เลือกรูปสระถ้ามีตัวสะกด
                self.vowel_th = self.vowel_th[1]
            else:
                self.vowel_th = self.vowel_th[0]

    # แปลงเสียงวรรณยุกต์ให้เป็นรูปวรรณยุกต์ อักษรสูงกลางต่ำ
    def select_tonemark(self):
        if self.initial_en in MIDDLE_C: # อักษรกลาง
            if self.dead_syl and self.tone == '2': # คำตาย อักษรกลาง เสียงเอก ไม่ต้องใส่วรรณยุกต์ => กะ กาด
                self.tone_mark = self.tone2mark('1')
            else:
                self.tone_mark = self.tone2mark(self.tone)
        elif self.tone == '1': # เสียงสามัญ ไม่มีรูปวรรณยุกต์มีแค่อักษรต่ำ => คัน นัน
            self.tone_mark = self.tone2mark(self.tone)
        elif self.tone == '2': # เสียงเอก มีแค่อักษรสูง คำเป็นรูปเอก คำตายไม่มีรูป => ขั่น ข่าน ขะ ขาด
            self.tone_mark = self.tone2mark('1') if self.dead_syl else self.tone2mark(self.tone)
        elif self.tone == '3': # เสียงโท เลือกใช้อักษรต่ำ คำตายเสียงยาว ไม่มีรูป อื่นๆ รูปเอก 
            self.tone_mark = self.tone2mark('1') if (self.dead_syl and self.long_vow) else self.tone2mark('2')
        elif self.tone == '4': # เสียงตรี อักษรต่ำคำตายเสียงสั้น ไม่มีรูป อื่นๆ รูปโท
            self.tone_mark = self.tone2mark('1') if (self.dead_syl and not self.long_vow)  else self.tone2mark('3')
        elif self.tone == '5': # อักษรต่ำรูปจัตวา อักษรสูงไม่มีรูป
            self.tone_mark = self.tone2mark(self.tone) if self.dead_syl else self.tone2mark('1')
        
                   
    def ipa_components(self):
        en = [self.ipa,self.initial_en,self.cluster_en,self.vowel_en,self.final_en,self.tone,self.dead_syl,self.long_vow,self.tone_mark]
        th = [self.ipa,self.initial_th,self.cluster_th,self.vowel_th,self.final_th,self.tone,self.dead_syl,self.long_vow,self.tone_mark]
        return [en, th]
    
    def spell(self):
        s = self.vowel_th.replace('อ',self.initial_th + self.cluster_th,1) 
        s = s.replace('-', self.tone_mark)
        s = s + self.final_th
        return s