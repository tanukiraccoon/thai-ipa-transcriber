import unittest
from thai-ipa-transcriber import IPA

CASES ={
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
class TestSpelling(unittest.TestCase):

    def test_general(self):
        for case in CASES:
            ipa = IPA(case)
            self.assertEqual(ipa.spell(), CASES[case])

if __name__ == '__main__':
    unittest.main()