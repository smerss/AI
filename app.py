from transformers import pipeline
import sys

def ozetle(metin: str) -> str:
    """
    Verilen metni özetler.

    Args:
        metin: Özetlenecek metin.

    Returns:
        Özetlenmiş metin.
    """
    summarizer = pipeline("summarization", model="yeniguno/turkish-abstractive-summary-mt5")
    yanit = summarizer(metin, max_length=150, min_length=30, do_sample=False)
    return yanit[0]['summary_text']

if __name__ == '__main__':
    print("Lütfen özetlemek istediğiniz metni girin ve ardından girişi sonlandırmak için Ctrl+D (veya Windows'ta Ctrl+Z) tuşlarına basın:")

    girilen_metin = sys.stdin.read()

    if girilen_metin.strip():
        ozet = ozetle(girilen_metin)
        print("\\n" + "="*20 + "\\n")
        print("Özet:")
        print(ozet)
    else:
        print("Giriş metni boş. Özetleme yapılamadı.")