# APK Processing Automation Tools

This repository contains Python scripts for automating APK decoding, building, and signing operations.

## Features

- APK decoding (using apktool)
- Building APKs from decoded files
- APK signing and verification
- User-friendly menu system
- Error handling and detailed logging

## Installation

1. Requirements:
   - Python 3.x
   - Java JDK
   - Apktool
   - Android SDK (for zipalign and apksigner)

2. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/apk-tools.git
   cd apk-tools
   ```

3. Install required tools:
   - Place apktool in `C:\Windows\` or `tools/` directory
   - Install Android SDK tools (`zipalign`, `apksigner`) in `C:\apk-toolkit\tools\`

## Usage

### 1. Decode APK
```bash
python decode_apk.py
```
- Lists APKs in `input_apks/` folder
- Decodes selected APK to `decoded_apk/` directory

### 2. Build APK
```bash
python build_apk.py decoded_apk
```
- Builds APK from decoded files
- Output: `build_output/output.apk`

### 3. Sign APK
```bash
python sign_apk.py
```
- Signs `build_output/output.apk`
- Output: `final_output/signed.apk`
- Automatically verifies signature

## Directory Structure

```
apk-tools/
├── input_apks/          # Original APKs
├── decoded_apk/         # Decoded files
├── build_output/        # Built APKs
├── final_output/        # Signed APKs
├── keys/                # Keystore files
├── tools/               # Tools (optional)
│
├── decode_apk.py        # Decoding script
├── build_apk.py         # Building script
├── sign_apk.py          # Signing script
└── README.md            # This file
```

## Configuration

- **Keystore**: Uses `keys/my-release-key.keystore`
  - Alias: `app`
  - Edit `sign_apk.py` to use a different keystore

- **Tool Paths**:
  - Apktool: `C:\Windows\apktool.bat` or `tools/apktool.bat`
  - Zipalign: `C:\apk-toolkit\tools\zipalign.exe`
  - Apksigner: `C:\apk-toolkit\tools\apksigner.bat`

## Troubleshooting

1. **Missing AndroidManifest.xml error**:
   - Verify decoding process completed successfully
   - Check existence of `decoded_apk/AndroidManifest.xml`

2. **Apktool not found error**:
   - Verify apktool is in the correct location
   - Create `tools/` directory and place apktool there

3. **Signing errors**:
   - Verify keystore file path is correct
   - Adjust `--min-sdk-version` parameter in `sign_apk.py` if needed

## Contributing

Bug reports and pull requests are welcome. Please open an issue to discuss your proposal first.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
