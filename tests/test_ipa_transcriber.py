import unittest

from src.ipa_transcriber import ThaiIPA

IPA_CASES_1 ={
   "naːj1":"นาย",
   "saŋ5":"สัง",
   "kʰa4":"คะ",
   "pʰan1":"พัน",
   "heːŋ1":"เฮง",
   "pʰi4":"พิ",
   "tʰak4":"ทัก",
   "faŋ2":"ฝั่ง",
   "pʰuː3":"พู่",
   "tʰaw3":"เท่า",
   "sɯŋ3":"ซึ่ง",
   "miː1":"มี",
   "ʔaː1":"อา",
   "cʰiːp3":"ชีบ",
   "pen1":"เป็น",
   "kʰon1":"คน",
   "kʰaːj5":"ขาย",
   "kʰuːat2":"ขวด",
   "tʰuːk2":"ถูก",
   "tam1":"ตัม",
   "ruːat2":"หรวด",
   "pa2":"ปะ",
   "ti2":"ติ",
   "bat2":"บัด",
   "kaːn1":"กาน",
   "cap2":"จับ",
   "fᴐːŋ4":"ฟ้อง",
   "saːn5":"สาน",
   "tʰaːn5":"ถาน",
   "lak4":"ลัก",
   "naː1":"นา",
   "li4":"ลิ",
   "kaː1":"กา",
   "kʰun1":"คุน",
   "jiŋ5":"หยิง",
   "cʰat2":"ฉัด",
   "cʰa4":"ชะ",
   "daː1":"ดา",
   "cʰaːn1":"ชาน",
   "sa2":"สะ",
   "maː1":"มา",
   "tʰi4":"ทิ"
}

IPA_CASES_2 = {
    "pen1": "เป็น",
    "ma4": "มะ",
    "nut4": "นุด",
    "sut2": "สุด",
    "pra2": "ประ",
    "sɤːt2": "เสิด",
    "lɤːt3": "เลิด",
    "kʰun1": "คุน",
    "kʰaː3": "ค่า",
    "jaŋ1": "ยัง",
    "diː1": "ดี",
    "kwaː2": "กว่า",
    "fuːŋ5": "ฝูง",
    "sat2": "สัด",
    "deː1": "เด",
    "rat4": "รัด",
    "cʰaːn5": "ฉาน",
    "coŋ1": "จง",
    "faː2": "ฝ่า",
    "fan1": "ฟัน",
    "pʰat4": "พัด",
    "tʰa4": "ทะ",
    "naː1": "นา",
    "wi4": "วิ",
    "cʰaː1": "ชา",
    "kaːn1": "กาน",
    "jaː2": "หย่า",
    "laːŋ4": "ล้าง",
    "pʰlaːn5": "ผลาน",
    "rɯː1": "รือ",
    "kʰeːn2": "เข่น",
    "biː1": "บี",
    "tʰaː1": "ทา",
    "kʰraj1": "ครัย",
    "maj3": "มั่ย",
    "tʰɯː5": "ถือ",
    "tʰoːt3": "โทด",
    "kroːt2": "โกรด",
    "cʰɛːŋ3": "แช่ง",
    "sat4": "ซัด",
    "hɯt4": "ฮึด",
    "hat4": "ฮัด",
    "daː2": "ด่า",
    "hat2": "หัด",
    "ʔa2": "อะ",
    "pʰaj1": "พัย",
    "mɯːan5": "เหมือน",
    "kiː1": "กี",
    "laː1": "ลา",
    "ʔat2": "อัด",
    "cʰaː1": "ชา",
    "saj5": "สัย",
    "pa2": "ปะ",
    "ti2": "ติ",
    "bat2": "บัด",
    "pra2": "ประ",
    "pʰrɯt4": "พรึด",
    "kot2": "กด",
    "kam1": "กัม",
    "not2": "หนด",
    "caj1": "จัย",
    "pʰuːt3": "พูด",
    "caː1": "จา",
    "haj3": "ฮั่ย",
    "ca4": "จ๊ะ",
    "caː5": "จ๋า",
    "naː3": "น่า",
    "faŋ1": "ฟัง",
    "ʔɤːj1": "เอย"
}

class TestSpelling(unittest.TestCase):
    def setUpClass():
        print("Starting test case in TestSpelling...")

    def tearDownClass():
        print("Finished test case in TestSpelling.")
        
    def test_ipa_conversion_set1(self):
        print("Running test: test_ipa_conversion_set1")
        for case in IPA_CASES_1:
            ipa = ThaiIPA(case)
            self.assertEqual(ipa.spell(), IPA_CASES_1[case])
    def test_ipa_conversion_set2(self):
        print("Running test: test_ipa_conversion_set2")
        for case in IPA_CASES_2:
            ipa = ThaiIPA(case)
            self.assertEqual(ipa.spell(), IPA_CASES_2[case])

class TestThaiIPA(unittest.TestCase):
    def setUpClass():
        print("Starting test case in TestThaiIPA...")

    def tearDownClass():
        print("Finished test case in TestThaiIPA.")
        
    def test_variable_access(self):
        print("Running test: test_variable_access")
        i = ThaiIPA('pʰrɯk4')
        self.assertEqual(i.initial_en, 'pʰ')
        self.assertEqual(i.cluster_en, 'r')
        self.assertEqual(i.vowel_en, 'ɯ')
        self.assertEqual(i.final_en, 'k')
        self.assertEqual(i.tone, 4)
        self.assertFalse(i.is_long)
        self.assertTrue(i.is_dead)
        self.assertFalse(i.is_mid)
        self.assertFalse(i.is_open)

    def test_variable_assign(self):
        print("Running test: test_variable_assign")
        i = ThaiIPA('pʰrɯk4')
        i.initial_en = 'k'
        i.cluster_en = ''
        i.vowel_en = 'aː'
        i.final_en = 'j'
        i.tone = 1 
        self.assertEqual(i.initial_en, 'k')
        self.assertEqual(i.cluster_en, '')
        self.assertEqual(i.vowel_en, 'aː')
        self.assertEqual(i.final_en, 'j')
        self.assertEqual(i.tone, 1)
        self.assertTrue(i.is_long)
        self.assertFalse(i.is_dead)
        self.assertTrue(i.is_mid)
        self.assertFalse(i.is_open)
        self.assertEqual(i.spell(), 'กาย')

if __name__ == '__main__':
    unittest.main()