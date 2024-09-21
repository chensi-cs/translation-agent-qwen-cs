import translation_agent as ta
source_lang, target_lang, country = "English", "Simplified Chinese", "China"
source_text= "Hunan Province in China is renowned for its beautiful landscapes. It has majestic mountains like Zhangjiajie. The province is also rich in history and culture. Hunan cuisine is spicy and famous worldwide. Changsha, the capital city, is a vibrant place with modern architecture and historical sites. Hunan is home to many talented people and has made significant contributions to China's development in various fields. It is a place full of charm and vitality."
print(f"Source text:\n\n{source_text}\n------------\n")
translation = ta.translate(source_lang, target_lang, source_text, country)
print(f"Translation:\n\n{translation}")