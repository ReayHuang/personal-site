# personal-site

Yen-Jui Huang（Reay Huang）的個人網站 — **LR 驗船師 · PMP®**，配色與版面參考 [Lloyd's Register](https://www.lr.org/en/)（深藍、青綠、白底卡片），以靜態 HTML 分享筆記與研究。

## 本機預覽

```bash
open index.html          # 英文首頁（預設）
open index.zh.html       # 繁中首頁
# 或
python3 -m http.server 8080
```

## 目錄結構

```
personal-site/
├── index.html              # 英文首頁（預設，全幅 Hero 帶）
├── index.zh.html           # 繁中首頁
├── index.en.html           # 轉址至 index.html（保留舊連結相容）
├── about.html              # 關於我（繁中）
├── about.en.html           # About（英文）
├── assets/css/style.css    # LR 風格配色
├── notes/                  # 專業筆記
│   ├── index.html          # 海事筆記列表（繁中）
│   ├── index.en.html       # Maritime Note listing（英文）
│   └── maritime/           # 海事法規與檢驗
└── research/               # 研究資料
    ├── index.html          # 管理筆記列表（繁中）
    └── index.en.html       # Management Note listing（英文）
```

## 雙語版本

| 語言 | 首頁 | 關於我 | 列表頁命名 |
|------|------|--------|------------|
| 英文（預設） | `index.html` | `about.en.html` | `*.en.html` |
| 繁中 | `index.zh.html` | `about.html` | `*.html` |

訪客進入 `/` 或 `index.html` 即為英文首頁；語言切換連結位於各頁頂部導覽列。

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
