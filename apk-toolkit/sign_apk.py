# -*- coding: utf-8 -*-
import subprocess
import os
import sys

# Giriş ve çıktı klasörleri
build_output_dir = "build_output"
final_output_dir = "final_output"
os.makedirs(final_output_dir, exist_ok=True)

# Dosya yolları
unsigned_apk = os.path.join(build_output_dir, "output.apk")  # build_output'dan alıyoruz
aligned_apk = os.path.join(final_output_dir, "output-aligned.apk")
signed_apk = os.path.join(final_output_dir, "signed.apk")
keystore_path = os.path.abspath("keys/my-release-key.keystore")

alias = "app"

# Araç yolları
apksigner_path = r"C:\apk-toolkit\tools\apksigner.bat"
zipalign_path = r"C:\apk-toolkit\tools\zipalign.exe"

# Kontroller
if not os.path.exists(unsigned_apk):
    print(f"❌ HATA: {unsigned_apk} dosyası bulunamadı!")
    print("Lütfen önce APK'yı build edin (build_apk.py kullanarak)")
    sys.exit(1)

if not os.path.exists(keystore_path):
    print(f"❌ HATA: Keystore dosyası bulunamadı: {keystore_path}")
    sys.exit(1)

try:
    print("\n🔹 Zipalign işlemi başlatılıyor...")
    subprocess.run([zipalign_path, "-f", "-v", "4", unsigned_apk, aligned_apk], check=True)
    print("✅ Zipalign işlemi başarılı!")

    print("\n🔹 APK imzalanıyor...")
    subprocess.run([
        apksigner_path, "sign",
        "--ks", keystore_path,
        "--ks-key-alias", alias,
        "--out", signed_apk,
        aligned_apk
    ], check=True)
    print(f"✅ APK başarıyla imzalandı: {signed_apk}")

    print("\n🔹 İmza doğrulaması yapılıyor...")
    subprocess.run([apksigner_path, "verify", "-v", signed_apk], check=True)
    print("✅ İmza geçerli.")

except subprocess.CalledProcessError as e:
    print(f"\n❌ HATA: İşlem sırasında hata oluştu! Hata kodu: {e.returncode}")
    sys.exit(1)
except FileNotFoundError as e:
    print(f"\n❌ HATA: Araç bulunamadı: {str(e)}")
    sys.exit(1)
except Exception as e:
    print(f"\n❌ Beklenmeyen hata: {str(e)}")
    sys.exit(1)