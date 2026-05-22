# personal-site

Yen-Jui Huang（Reay Huang）的個人網站 — **LR 驗船師 · PMP®**，配色與版面參考 [Lloyd's Register](https://www.lr.org/en/)（深藍、青綠、白底卡片），以靜態 HTML 分享筆記與研究。

## 本機預覽

```bash
open index.html
# 或
python3 -m http.server 8080
```

## 目錄結構

```
personal-site/
├── index.html              # 首頁（全幅 Hero 帶）
├── about.html              # 關於我
├── assets/css/style.css    # LR 風格配色
├── notes/                  # 專業筆記
│   └── maritime/           # 海事法規與檢驗
└── research/               # 研究資料
```

## 品牌色（參考 lr.org）

| 用途 | 色碼 |
|------|------|
| 深藍（文字／頁尾） | `#070D19` |
| Hero 背景 | `#0D4665` |
| 青綠（強調／按鈕） | `#00C5B7` |
| 淺藍區塊 | `#EEF5FB` |

## 新增筆記

複製 `notes/maritime/class-survey-basics.html`，修改後在 `notes/index.html` 加入卡片連結。

## 聲明

頁尾已註明為個人網站，不代表 Lloyd's Register 官方立場。請勿上傳客戶機密或未公開缺陷資訊。
