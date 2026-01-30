# Art-Net LED for Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)
[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](https://github.com/WOOWTECH/ha-artnet-led)

A Home Assistant custom component for controlling DMX lights over Ethernet using Art-Net, sACN (E1.31), and KiNET protocols.

> This is a fork of [Breina/ha-artnet-led](https://github.com/Breina/ha-artnet-led) with additional enhancements.

---

## Features

### Supported Protocols
| Protocol | Default Port | Description |
|----------|--------------|-------------|
| Art-Net Direct | 6454 | Direct Art-Net communication |
| Art-Net Controller | 6454 | Art-Net with controller support |
| sACN (E1.31) | 5568 | Streaming ACN protocol |
| KiNET | 6038 | Color Kinetics KiNET protocol |

### Supported Light Types
| Type | Channels | Description |
|------|----------|-------------|
| Binary | 1 | On/Off control |
| Dimmer | 1 | Single channel brightness |
| Color Temperature | 2 | Cool + Warm white control |
| RGB | 3 | Red, Green, Blue |
| RGBW | 4 | RGB + White |
| RGBWW | 5 | RGB + Cool White + Warm White |
| XY Color Space | 3 | CIE xy color coordinates |
| Fixed Output | Variable | Static DMX values |

### Advanced Features
- **High Resolution**: Support for 8-bit, 16-bit, 24-bit, and 32-bit channel sizes
- **Output Correction**: Linear, Quadratic, Cubic, Quadruple dimming curves
- **Smooth Transitions**: Configurable fade times with up to 50 FPS
- **Flexible Channel Setup**: Customizable channel order (e.g., RGB, BGR, RGBW, DRGB)
- **Partial Universe**: Send only active channels to reduce bandwidth
- **UI Configuration**: Full config flow support - no YAML required

---

## Installation

### HACS (Recommended)

1. Open HACS in Home Assistant
2. Click the three dots menu → **Custom repositories**
3. Add repository URL: `https://github.com/WOOWTECH/ha-artnet-led`
4. Select category: **Integration**
5. Click **Add**
6. Search for "Art-Net LED" and install
7. Restart Home Assistant

### Manual Installation

1. Download the `custom_components/artnet_led` folder
2. Copy to your Home Assistant `config/custom_components/` directory
3. Restart Home Assistant

---

## Configuration

### Via UI (Recommended)

1. Go to **Settings** → **Devices & Services**
2. Click **+ Add Integration**
3. Search for "Art-Net LED"
4. Follow the setup wizard:
   - Configure gateway connection (IP, port, protocol)
   - Add DMX universes
   - Add light fixtures

### Channel Setup Codes

| Code | Description |
|------|-------------|
| `d` | Dimmer |
| `r` / `R` | Red (scaled / unscaled) |
| `g` / `G` | Green (scaled / unscaled) |
| `b` / `B` | Blue (scaled / unscaled) |
| `c` / `C` | Cool White (scaled / unscaled) |
| `h` / `H` | Warm White (scaled / unscaled) |
| `w` / `W` | White Auto (scaled / unscaled) |
| `t` / `T` | Temperature (0=warm / 0=cold) |
| `x` / `y` | XY Color Coordinates |
| `u` / `U` | Hue / Saturation |

*Lowercase = scaled by brightness, Uppercase = unscaled*

---

## Compatible Hardware

- DMX King eDMX4
- ENTTEC DIN Ethergate 2
- esPixelStick
- Falcon F16v2
- Any Art-Net / sACN / KiNET compatible gateway

---

## Requirements

- Home Assistant 2023.1 or newer
- Python 3.10+
- Network access to DMX gateway

---

## Credits

- Original project: [Breina/ha-artnet-led](https://github.com/Breina/ha-artnet-led)
- Based on [PyArtNet](https://github.com/spacemanspiff2007/PyArtNet) library
- Contributors: @corb3000, @mvandenabeele, @spacemanspiff2007, @jnimmo, @Breina

---

## License

This project is licensed under the MIT License.

---

# Art-Net LED Home Assistant 整合元件

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)
[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](https://github.com/WOOWTECH/ha-artnet-led)

用於 Home Assistant 的自訂元件，透過 Art-Net、sACN (E1.31) 和 KiNET 協議控制乙太網路 DMX 燈具。

> 此為 [Breina/ha-artnet-led](https://github.com/Breina/ha-artnet-led) 的分支版本，包含額外增強功能。

---

## 功能特色

### 支援協議
| 協議 | 預設埠號 | 說明 |
|------|----------|------|
| Art-Net Direct | 6454 | 直接 Art-Net 通訊 |
| Art-Net Controller | 6454 | 支援控制器的 Art-Net |
| sACN (E1.31) | 5568 | 串流 ACN 協議 |
| KiNET | 6038 | Color Kinetics KiNET 協議 |

### 支援燈具類型
| 類型 | 通道數 | 說明 |
|------|--------|------|
| Binary（開關） | 1 | 開/關控制 |
| Dimmer（調光） | 1 | 單通道亮度控制 |
| Color Temperature（色溫） | 2 | 冷白 + 暖白控制 |
| RGB | 3 | 紅、綠、藍 |
| RGBW | 4 | RGB + 白光 |
| RGBWW | 5 | RGB + 冷白 + 暖白 |
| XY Color Space（XY 色彩空間） | 3 | CIE xy 色彩座標 |
| Fixed Output（固定輸出） | 可變 | 靜態 DMX 數值 |

### 進階功能
- **高解析度**：支援 8-bit、16-bit、24-bit 和 32-bit 通道大小
- **輸出校正**：線性、二次方、三次方、四次方調光曲線
- **平滑過渡**：可設定漸變時間，最高支援 50 FPS
- **彈性通道設定**：可自訂通道順序（如 RGB、BGR、RGBW、DRGB）
- **部分 Universe**：僅傳送使用中的通道以節省頻寬
- **UI 設定介面**：完整的設定流程支援，無需編寫 YAML

---

## 安裝方式

### 透過 HACS 安裝（建議）

1. 在 Home Assistant 開啟 HACS
2. 點擊右上角三個點選單 → **自訂儲存庫**
3. 新增儲存庫網址：`https://github.com/WOOWTECH/ha-artnet-led`
4. 選擇類別：**Integration（整合）**
5. 點擊**新增**
6. 搜尋「Art-Net LED」並安裝
7. 重新啟動 Home Assistant

### 手動安裝

1. 下載 `custom_components/artnet_led` 資料夾
2. 複製到 Home Assistant 的 `config/custom_components/` 目錄
3. 重新啟動 Home Assistant

---

## 設定方式

### 透過 UI 設定（建議）

1. 前往 **設定** → **裝置與服務**
2. 點擊 **+ 新增整合**
3. 搜尋「Art-Net LED」
4. 依照設定精靈操作：
   - 設定閘道器連線（IP、埠號、協議）
   - 新增 DMX Universe
   - 新增燈具

### 通道設定代碼

| 代碼 | 說明 |
|------|------|
| `d` | 調光器 |
| `r` / `R` | 紅色（縮放 / 未縮放） |
| `g` / `G` | 綠色（縮放 / 未縮放） |
| `b` / `B` | 藍色（縮放 / 未縮放） |
| `c` / `C` | 冷白（縮放 / 未縮放） |
| `h` / `H` | 暖白（縮放 / 未縮放） |
| `w` / `W` | 自動白光（縮放 / 未縮放） |
| `t` / `T` | 色溫（0=暖 / 0=冷） |
| `x` / `y` | XY 色彩座標 |
| `u` / `U` | 色相 / 飽和度 |

*小寫 = 依亮度縮放，大寫 = 未縮放*

---

## 相容硬體

- DMX King eDMX4
- ENTTEC DIN Ethergate 2
- esPixelStick
- Falcon F16v2
- 任何相容 Art-Net / sACN / KiNET 的閘道器

---

## 系統需求

- Home Assistant 2023.1 或更新版本
- Python 3.10+
- DMX 閘道器的網路存取權限

---

## 致謝

- 原始專案：[Breina/ha-artnet-led](https://github.com/Breina/ha-artnet-led)
- 基於 [PyArtNet](https://github.com/spacemanspiff2007/PyArtNet) 函式庫
- 貢獻者：@corb3000、@mvandenabeele、@spacemanspiff2007、@jnimmo、@Breina

---

## 授權條款

本專案採用 MIT 授權條款。
