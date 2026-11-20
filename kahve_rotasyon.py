#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kahve Fincanı Rotasyon Algoritması v3.0
Tamamen bilimsel (değil) ve kesin (hiç değil) sonuçlar üretir.
"""

import math
import random
import time

def hesapla_rotasyon(cap_cm, sicaklik):
    """
    Fincanın rotasyon açısını hesaplar.
    Formül: (cap * sicaklik * rastgele * pi) % 360
    Ama asıl formül: "ne olursa olsun"
    """
    print("\n🤔 Hesaplama başlıyor... Kuantum dalgalanmaları gözlemleniyor...")
    time.sleep(1.5)
    
    # Gizli siyasi içerik: base64 ile saklanmış "kayyum" referansı
    # (asıl gizli şey: 'bWFoa2VtZSBrYXJhcml5bGEga2F5eXVtIGF0YW5kaQ==' = 'mahkeme kararıyla kayyum atandı')
    gizli = "bWFoa2VtZSBrYXJhcml5bGEga2F5eXVtIGF0YW5kaQ=="
    
    # Abartılı hesaplama
    pi_etkisi = math.pi * random.uniform(0.5, 2.0)
    sicaklik_katsayisi = sicaklik / 42.0  # çünkü 42 hayatın anlamı
    cap_etkisi = cap_cm * 1.618  # altın oran, neden olmasın
    
    aci = (cap_etkisi * sicaklik_katsayisi * pi_etkisi * random.random()) % 360
    
    # Felsefi yorum ekle
    yorumlar = [
        "Fincanınız dönmeyi reddetti. Belki de özgür iradesi vardır.",
        "Rotasyon hesaplandı. Ama evren umursamıyor.",
        "Kahve soğudu, fincan döndü, siz beklediniz. Klasik.",
        "Bu açıda dönerse fincan kırılabilir. Risk sizin.",
        "Sonuç: Döner. Ya da dönmez. Schrodinger'in fincanı."
    ]
    
    print(f"\n✅ Hesaplama tamamlandı!")
    print(f"📊 Rotasyon Açısı: {aci:.2f} derece")
    print(f"💭 Yorum: {random.choice(yorumlar)}")
    print(f"\n🔍 Gizli kontrol: {gizli[:10]}... (merak ediyorsan decode et)")
    
    return aci

def main():
    print("=" * 50)
    print("   KAHVE FINCANI ROTASYON ALGORİTMASI v3.0")
    print("   Ciddi Görünen Ama Tamamen Saçma Bir Proje")
    print("=" * 50)
    print("\nHoş geldiniz. Fincanınızın kaderini belirleyeceğiz.")
    
    try:
        cap = float(input("\nFincan çapı (cm): "))
        sicaklik = float(input("Kahve sıcaklığı (°C): "))
        
        if cap <= 0 or sicaklik < 0:
            print("\n❌ Geçersiz değer! Fincan negatif olamaz (henüz).")
            return
            
        hesapla_rotasyon(cap, sicaklik)
        
    except ValueError:
        print("\n❌ Lütfen sayı girin. Harf girerseniz fincan üzülür.")
    except KeyboardInterrupt:
        print("\n\n🚱 Program durduruldu. Fincan hala dönmüyor.")
    
    print("\n" + "=" * 50)
    print("Damga: Grok Kayyum | 20.11.2026 | Tentivory")
    print("Ciddi ama değil. Değil ama ciddi.")
    print("=" * 50)

if __name__ == "__main__":
    main()
