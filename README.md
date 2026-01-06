# ChiChin Liu - 個人講師網站

專業講師個人網站，提供優質的教學服務和課程資訊。

## 網站特色

- 響應式設計，支援手機、平板和桌面瀏覽
- 現代化的使用者介面
- 流暢的動畫效果
- 直覺的導航系統
- 互動式聯絡表單

## 網站結構

### 主要區塊

1. **首頁 (Hero Section)**
   - 吸引人的標題和副標題
   - 快速導航按鈕

2. **關於我 (About)**
   - 個人簡介
   - 教學經驗統計
   - 專業領域展示

3. **課程介紹 (Courses)**
   - 程式設計基礎
   - 資料科學入門
   - 網頁開發全端
   - 客製化課程

4. **學生評價 (Testimonials)**
   - 真實學生回饋
   - 五星評價展示

5. **聯絡我 (Contact)**
   - 聯絡資訊
   - 互動式表單
   - 即時表單驗證

## 技術架構

- **HTML5**: 語意化標籤，SEO 友善
- **CSS3**:
  - CSS Grid 和 Flexbox 佈局
  - CSS 變數管理主題色彩
  - 平滑過渡動畫
  - 響應式媒體查詢
- **JavaScript**:
  - 原生 JavaScript (無框架)
  - 平滑滾動
  - 表單驗證
  - 交互動畫
  - Intersection Observer API

## 如何使用

### 本地預覽

1. 下載或克隆此儲存庫
2. 在瀏覽器中開啟 `index.html`
3. 無需安裝任何依賴，直接可用

### 自訂內容

#### 修改個人資訊

編輯 `index.html` 中的以下部分：

- 導航欄名稱：`.nav-brand`
- 主標題：`.hero-title`
- 關於我內容：`#about` 區塊
- 聯絡資訊：`#contact` 區塊

#### 調整樣式

編輯 `styles.css` 中的 CSS 變數：

```css
:root {
    --primary-color: #2563eb;    /* 主要顏色 */
    --secondary-color: #3b82f6;  /* 次要顏色 */
    --text-dark: #1f2937;        /* 深色文字 */
    --text-light: #6b7280;       /* 淺色文字 */
}
```

#### 添加新課程

在 `index.html` 的 `.courses-grid` 中添加新的 `.course-card`：

```html
<div class="course-card">
    <div class="course-icon">🎓</div>
    <h3>課程名稱</h3>
    <p>課程描述</p>
    <ul class="course-features">
        <li>特色一</li>
        <li>特色二</li>
        <li>特色三</li>
    </ul>
    <div class="course-price">價格</div>
</div>
```

## 部署

### GitHub Pages

1. 將專案推送到 GitHub
2. 到儲存庫設定 > Pages
3. 選擇分支和根目錄
4. 儲存後即可獲得網站連結

### 其他平台

此網站為純靜態網站，可部署到：
- Netlify
- Vercel
- Firebase Hosting
- AWS S3

## 瀏覽器支援

- Chrome (最新版本)
- Firefox (最新版本)
- Safari (最新版本)
- Edge (最新版本)

## 授權

此專案為個人作品集網站範本，可自由使用和修改。

## 聯絡方式

如有任何問題或建議，歡迎聯繫：
- Email: contact@chichinliu.com
- GitHub: [@chichinliu](https://github.com/chichinliu)
