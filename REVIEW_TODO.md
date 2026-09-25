# Howard Liao CISO 專案改版待確認清單 (REVIEW_TODO.md)

本文件依據國際獵頭（Executive Search）與 CISO 職缺背景調查（Background Check, Kroll / HireRight）之高階標準，彙整全站修改處及待 Howard Liao Ph.D.（廖倫豪 博士）本人親自確認之重要事項。

---

## 優先級說明
- **P0（最高優先級，必須確認）**：涉及年資、學歷重疊、職稱、預算與量化指標之客觀真實性，直接攸關背景調查（Red Flags）是否能無瑕疵通過。
- **P1（重要優先級，建議補齊）**：涉及案例佐證、董事會報告制度、進行中證照及推薦語，強化董事會與提名委員會信任度。
- **P2（技術與 SEO 選項）**：涉及搜尋引擎索引公開與技術品質設定。

---

## 🔴 P0 級待確認事項（可信度與背景調查紅旗修復）

### [P0-01] 職涯總年資起算點與算術一致性
- **檔案位置**：`index.html` (Hero, Profile, Experience), `build_trilingual_1_5x_resumes.py`
- **原本文字**：`27+ 年` / `27+ Years Leadership`
- **問題分析**：經歷時間線自 2002 年 Sybase 起算至 2026 年應為 **24 年**。若寫「27+ 年」易被背景調查機構以「2026 - 2002 = 24」直接判定數字不實；除非職涯係自 1998 年（Sybase 實習/兼職）起算。
- **目前修正**：全站已修改為客觀可驗證之「**24 年企業 IT 領導實績（職涯始於 2002 年）**」。
- **待確認事項**：請 Howard 確認官方履歷之正式起算年份是否鎖定為 **2002 年**？（若確定自 1998 年起算，則需補齊 1998–2002 之可查證在職或實習機構證明）。

---

### [P0-02] Sybase 早期職稱與大學學歷在學期間重疊
- **檔案位置**：`index.html` (Experience Milestone 7: Sybase)
- **原本文字**：`2002.08 – 2008.02 | IT Manager，管理 10–15 人`
- **問題分析**：Howard 大學學士學歷為中興大學應用數學系（2000.09 – 2004.06 在學）。大學在學期間（大三至大四）全職擔任跨國外商 Sybase 之「IT Manager（管理 10–15 人）」，在獵頭背景調查與外商董事會眼中為高度敏感之紅旗。
- **目前修正**：已將該條目職稱修正為「**資深系統工程師 / 技術專員 (Senior Systems Engineer / Technical Specialist)**」，並在程式碼標記 TODO。
- **待確認事項**：請 Howard 提供 2002.08 在 Sybase 的真實職稱（如：系統工程師、兼職技術顧問或實習專員）與實際工作形式，以確保與勞健保/在職證明 100% 吻合。

---

### [P0-03] 資安長 (CISO) 與科技副總年資口徑
- **檔案位置**：`index.html` (Hero, Profile, Experience)
- **原本文字**：`10+ 年 CISO／科技副總` 與 `15+ 年資安`
- **問題分析**：履歷時間線中，CISO 職稱始於 2025.05（現職），IT Director 職稱始於 2018（泓晏科技）。若在 Executive Summary 寫「10+ 年 CISO」，在第三方背景調查時將因缺乏 10 年前的「CISO / VP」在職證明而判定失真。
- **目前修正**：全面改為可嚴謹驗證之「**8+ 年於上市櫃與跨國企業擔任 IT Director 級科技領導實績，並自 2025 年起擔任集團資安長 (Group CISO)**」。
- **待確認事項**：請 Howard 確認此專業敘述是否符合實際履歷架構？

---

### [P0-04] 年度管理預算口徑（現職規模 vs 前職高峰）
- **檔案位置**：`index.html` (KPI Bento Card 1), `build_trilingual_1_5x_resumes.py`
- **原本文字**：`$14M+ IT & 資安資本治理`
- **問題分析**：現職盛欣/盛碁管轄之全集團預算為 **$10–12M**；$14M+ 是隆中網絡時期（2022–2025）之多雲與資安預算高峰。直接寫 $14M+ 容易與現職敘述產生口徑衝突。
- **目前修正**：修正為標註分明之「**$10–12M（現職規模 | 前職高峰：$14M+）**」。
- **待確認事項**：請 Howard 確認首頁指標維持「現職規模」並附註「前職高峰」的呈現方式。

---

### [P0-05] 核心量化指標基準期與零停機 SLA
- **檔案位置**：`index.html` (KPI Bento Cards 2, 3, 4)
- **原本文字**：`100% Zero Outage`、`-30% 雲端年度 TCO`、`-30% 重大資安事件`、`-30% MTTR`
- **問題分析**：
  1. 四個指標皆為恰好「-30%」，獵頭與審計委員會容易質疑為行銷修飾數值，缺乏基準期（Baseline Period）與量測工具依據。
  2. 電信級或雲端 SLA 在高可用業界標準通常寫「99.99% 或 99.999%」，單寫「100% Zero Outage」在審查時需具備明確的監控紀錄佐證。
- **目前修正**：
  - 「100% Zero Outage」改為「**關鍵服務可用性保證 SLA [TODO: ___]%（連續 [TODO: ___] 個月零 P1 重大停機）**」。
  - 雲端 TCO、重大事件與 MTTR 保留 -30%，並於程式碼中標記 TODO。
- **待確認事項**：
  1. 請 Howard 提供 GKE 核心服務的確切可用性數值（如 99.99%）及連續幾個月（如 18 或 24 個月）無 P1 停機。
  2. 請補上 -30% 比較的基準年份（如 2023 vs 2024）及計算量測方式（如 FinOps 保留執行個體調優、Datadog/Jira 工單統計）。

---

### [P0-06] 博士論文國家圖書館典藏代碼、畢業年份與措辭修正
- **檔案位置**：`index.html` (Speaking & Papers Item 5)
- **原本文字**：`典藏代碼: 106IKTC0183002 | 2014.10`、`擔任學術研究指導學者`
- **問題分析**：
  1. 國家圖書館系統編號 `106IKTC0183002` 中的「106」代表民國 106 年（西元 2017 年），與學歷博士畢業年份 2013.06 及刊載 2014.10 存在年份矛盾。
  2. 原文寫「擔任學術研究指導學者」，在中文學術慣例中容易被誤解為自己是指導教授，對博士候選人而言極易被判定為誤導。
- **目前修正**：
  - 已徹底刪除「擔任學術研究指導學者」措辭。
  - 保留博士論文名稱與國圖收錄，並標註代碼確認 TODO。
- **待確認事項**：請 Howard 確認國圖代碼 106IKTC0183002 之正式建檔緣由或提供論文正式典藏連結。

---

### [P0-07] 碩士與博士學歷在職進修（Part-time）註記
- **檔案位置**：`index.html` (Credentials - Education), `build_trilingual_1_5x_resumes.py`
- **原本文字**：`中興大學 碩士 2004–2006`、`朝陽科大 博士 2009–2013`
- **問題分析**：
  - 碩士期間（2004–2006）與光男企業協理全職工作（2004–2014）完全重疊。
  - 博士期間（2009–2013）亦與光男企業協理全職工作重疊。
  - 若未註明為在職專班/在職進修，獵頭背景調查時將比對勞保投保紀錄與全日制學生身分，可能引發全職狀態存疑。
- **目前修正**：學歷欄位明確加註「**(在職進修 / Part-time / 社会人大学院)**」，凸顯邊全職高管邊攻讀博碩士的堅毅特質。
- **待確認事項**：請 Howard 確認碩博士學制是否為在職專班/在職進修形式。

---

## 🟡 P1 級待確認事項（架構升級、旗艦案例與高階實踐補齊）

### [P1-01] 現職公司名稱公開去識別化確認
- **檔案位置**：`index.html` (Experience Milestone 1)
- **原本文字**：`(高雄、上海、台北 / 盛欣、盛碁網絡/中國 波克/台北 芬格國際有限公司) 上市櫃公司 關聯集團`
- **目前修正**：改為高管標準「**跨國數位科技與娛樂平台集團 (Multinational Digital Tech & Entertainment Platform Group)**」，淡化單一實體內部細節。
- **待確認事項**：請 Howard 確認公開作品集網站是否維持去識別化集團稱謂，或是需要顯示特定法定公司名稱？

---

### [P1-02] 旗艦案例 3：ISO/IEC 42001 AI 治理落地佐證文件
- **檔案位置**：`index.html` (Flagship Case Studies - Case 3)
- **目前進度**：已完成「情境 → 決策行動 → 可驗證成果」之完整論述。
- **待確認事項**：外部佐證連結目前留有 `<!-- TODO(Howard): 補上證書影本或第三方審查報告連結 -->`，請 Howard 提供 ISO 42001 證書影本或公開治理政策報告之連結。

---

### [P1-03] 去識別化重大資安事件應變案例（Incident Response Case Study）
- **檔案位置**：`index.html` (Governance Standards Section)
- **目前進度**：已建立「去識別化大型第三方供應鏈安全威脅之快速隔離處置與復原」架構卡片。
- **待確認事項**：請 Howard 提供 1 個真實處理過、去識別化的事件範例（例如：Log4j / 第三方套件漏洞處置、RTO 復原時間、根因分析報告）。

---

### [P1-04] 董事會報告機制之對象與頻率（Board Reporting Cadence）
- **檔案位置**：`index.html` (Governance Standards Section)
- **目前進度**：已建立「每季董事會與審計委員會常態定期報告機制」卡片。
- **待確認事項**：請 Howard 確認向董事會/審計委員會報告之固定頻率（如：每季定期報告 + 重大資安事件 2 小時即時通報）與匯報對象（董事長 / 審計委員會 / 獨立董事）。

---

### [P1-05] 證照發證單位、證號與卓越獎頒發機構
- **檔案位置**：`index.html` (Credentials Section)
- **原本文字**：`ISO 27001 主任稽核員`、`ISO 42001 主任稽核員`、`雲端架構卓越獎`
- **待確認事項**：
  1. 請 Howard 提供 ISO 27001 與 ISO 42001 主任稽核員之發證機構名稱（如：BSI / SGS / DNV / TÜV）與證書證號。
  2. 請確認「雲端架構卓越獎」之確切頒發單位（如：Google Cloud 官方或大會主辦單位）。

---

### [P1-06] 進行中高階證照（Certifications in Progress）
- **檔案位置**：`index.html` (Credentials Section)
- **目前進度**：已新增 CISM（Certified Information Security Manager）與 CISSP（Certified Information Systems Security Professional）之 In Progress 標記。
- **待確認事項**：請 Howard 提供預計考試或取得時程（如：2026 Q4 或 2027 Q1）。

---

### [P1-07] 目標高管職位定位與外派彈性（Target Roles）
- **檔案位置**：`index.html` (Governance Standards Section)
- **目前進度**：列出 Group CISO / 資訊安全處長 / 數位信任副總，地點設定為台北、台灣北部 / 開放亞太跨國出差。
- **待確認事項**：請 Howard 確認是否有特定的產業偏好（如金融金控、高科技製造、數位跨國平台）或外派意願。

---

### [P1-08] 高階推薦人背書（Executive Endorsements）
- **檔案位置**：`index.html` (Governance Standards Section)
- **目前進度**：目前標註為「依評鑑階段提供」。
- **待確認事項**：請 Howard 確認是否具備已獲授權、可公開引述的一句話推薦語（來自上市公司董事長、CEO、外部審計師或同業 C-Level）。

---

### [P1-09] 履歷下載格式由 .docx 轉為正式 PDF
- **檔案位置**：`index.html` (Resume Download Banner)
- **目前進度**：目前提供繁中、英文、日文之最新校驗 Word (.docx) 原檔下載。
- **待確認事項**：待 Howard 確認所有經歷數字後，可協助產出對應之正式 PDF 檔案（`Howard_Liao_CISO_EN.pdf`、`_ZH.pdf`、`_JA.pdf`）。

---

### [P1-10] MongoDB.local Taipei 外部活動佐證連結更新
- **檔案位置**：`index.html` (Speaking & Media Item 2)
- **原本連結**：`https://www.mongodb.com/community/forums/t/mongodb-local-taipei-2024/281699` (HTTP 404 失效)
- **目前修正**：已暫時更新為官方活動有效首頁 `https://www.mongodb.com/events/mongodb-local` (HTTP 200)，避免訪客或背調人員點擊出現 404。
- **待確認事項**：請 Howard 確認是否有 2024 當年度台北大會的具體議程報導或簡報存檔連結以供替換。

---

## 🟢 P2 級待確認事項（SEO 與搜尋引擎索引選項）

### [P2-01] 搜尋引擎索引開放選項（Search Engine Indexing Option）
- **檔案位置**：`index.html` (`<meta name="robots">`)
- **現行設定**：目前遵循高階隱私保護，嚴格設定為 `<meta name="robots" content="noindex, nofollow, noarchive, nosnippet, noimageindex">`。
- **未來選項說明**：
  若 Howard 日後希望讓 Google、Bing 搜尋引擎公開索引您的 CISO 官方網站，可依下列步驟開放：
  1. 將 `<meta name="robots" content="noindex, nofollow...">` 移除，改為 `<meta name="robots" content="index, follow">`。
  2. 在 `robots.txt` 中將 `Disallow: /` 改為 `Allow: /`。
  3. 加入 Canonical 標籤 `<link rel="canonical" href="https://howardliao.github.io/Howard_CISO/">`。
  4. 提交 `sitemap.xml` 至 Google Search Console 進行認證。
