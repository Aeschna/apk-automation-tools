# -*- coding: utf-8 -*-

import sys
import subprocess
import os
import glob

# APK dosyalarını input_apks klasöründe bul
APK_DIR = os.path.join(os.getcwd(), "input_apks")
if not os.path.exists(APK_DIR):
    print(f"❌ {APK_DIR} klasörü bulunamadı!")
    sys.exit(1)

apk_files = [f for f in glob.glob(os.path.join(APK_DIR, "*.apk")) if os.path.isfile(f)]

if not apk_files:
    print(f"❌ {APK_DIR} klasöründe APK dosyası bulunamadı.")
    sys.exit(1)

# Kullanıcıdan seçim
print("\nBulunan APK dosyaları:")
for idx, apk in enumerate(apk_files, start=1):
    apk_name = os.path.basename(apk)
    print(f"{idx}. {apk_name}")

choice = input("\n👉 İşlem yapmak istediğiniz APK dosyasının numarasını girin: ")
try:
    apk_choice = apk_files[int(choice) - 1]
except (IndexError, ValueError):
    print("❌ Geçersiz seçim.")
    sys.exit(1)

apk_path = apk_choice
output_dir = "decoded_apk"

# decode işlemi
try:
    # Önceki decode sonuçlarını temizle
    if os.path.exists(output_dir):
        import shutil
        shutil.rmtree(output_dir)
    
    # apktool'un tam yolunu belirt
    subprocess.run(["java", "-jar", "C:\\Windows\\apktool.jar", "d", apk_path, "-o", output_dir], check=True)
    print(f"\n✅ APK başarıyla decode edildi: {output_dir} klasörüne çıkarıldı.")
except subprocess.CalledProcessError as e:
    print(f"\n❌ HATA: APK decode edilemedi! Hata kodu: {e.returncode}")
except FileNotFoundError:
    print("\n❌ HATA: Apktool bulunamadı veya Java yüklü değil!")
except Exception as e:
    print(f"\n❌ Beklenmeyen hata: {str(e)}")