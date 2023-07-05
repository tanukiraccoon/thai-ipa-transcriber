from src.ipa_transcriber import IPA

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