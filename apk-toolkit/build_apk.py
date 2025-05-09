# -*- coding: utf-8 -*-
import sys
import subprocess
import os

if len(sys.argv) != 2:
    print("Kullanim: python build_apk.py decoded_folder")
    sys.exit(1)

decoded_folder = sys.argv[1]
output_dir = "build_output"
output_apk = os.path.join(output_dir, "output.apk")

# Klasör yoksa oluştur
os.makedirs(output_dir, exist_ok=True)

# apktool'ün tam yolunu belirtin
apktool_path = "C:\\Windows\\apktool.bat"  # Veya apktool'un yüklü olduğu yol

try:
    subprocess.run([apktool_path, "b", decoded_folder, "-o", output_apk], check=True)
    print(f"\n✅ APK başarıyla build edildi: {output_apk}")
except subprocess.CalledProcessError as e:
    print(f"\n❌ HATA: APK derlenemedi! Hata kodu: {e.returncode}")
except FileNotFoundError:
    print("\n❌ HATA: apktool komut dosyası bulunamadı. Yolun doğru olduğundan emin olun.")
except Exception as e:
    print(f"\n❌ Beklenmeyen hata: {str(e)}")