#!/usr/bin/env python3
"""Apply English UI and data labels to onboard-certificates.en.html from zh template."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EN = ROOT / "notes/maritime/onboard-certificates.en.html"
text = EN.read_text(encoding="utf-8")

sec_map = {
    "1 通用｜適用相關公約的船舶": "1 General | Ships subject to relevant conventions",
    "2 客船｜Passenger ships": "2 Passenger ships",
    "3 貨船｜Cargo ships": "3 Cargo ships",
    "4 NLS bulk｜有毒液體散裝": "4 NLS bulk | Noxious liquid substances in bulk",
    "5 化學船": "5 Chemical tanker",
    "6 氣體船": "6 Gas carrier",
    "7 高速船": "7 High-speed craft",
    "8 危險貨物": "8 Dangerous goods",
    "9 包裝危險品": "9 Packaged dangerous goods",
    "10 INF cargo｜核燃料/放射性貨物": "10 INF cargo | Nuclear fuel / radioactive materials",
    "11 核動力船": "11 Nuclear ship",
    "12 極地水域": "12 Polar waters",
    "13 低閃點燃料": "13 Low-flashpoint fuels",
    "非強制｜Other non-mandatory": "Non-mandatory | Other non-mandatory",
}

for zh, en in sec_map.items():
    text = text.replace(f"sec:'{zh}'", f"sec:'{en}'")

purpose_zh = """    function purposeFor(item){
      const title = item.title.toLowerCase();
      const tags = item.tags.map(tag => tag.toLowerCase());
      const hasTag = tag => tags.some(t => t.includes(tag));

      if(/tonnage/.test(title)) return '確認船舶總噸位與淨噸位，作為適用門檻、收費、檢驗與證書要求判斷的基礎。';
      if(/load line/.test(title)) return '證明船舶乾舷、載重線標誌與相關水密安全條件已依載重線規定完成核定。';
      if(/exemption/.test(title)) return '記錄主管機關允許船舶免除特定要求的範圍、條件與法定依據。';
      if(/coating/.test(title)) return '保存保護塗層的規格、施工、檢查與維護資料，支援結構防腐與後續檢驗。';
      if(/emergency towing/.test(title)) return '讓船舶在失去動力或緊急狀況時，有可立即採用的船舶專屬拖帶安排。';
      if(/construction drawings|ship construction file|ship structure access|technical file|eedi|eexi|engine parameters/.test(title)) return '保存設計、建造、改裝或計算依據，使後續檢驗、維護與符合性判斷可追溯。';
      if(/noise/.test(title)) return '確認船上噪音量受控，保障船員工作與休息環境符合噪音規範。';
      if(/stability|loading information/.test(title)) return '提供船長判斷裝載、吃水、縱傾與破損穩性的依據，避免營運中失去穩性安全。';
      if(/damage control/.test(title)) return '協助船員在進水或破損時快速判斷水密分隔、關閉裝置與控制措施。';
      if(/manoeuvring/.test(title)) return '提供船長與駕駛台人員掌握船舶操縱性能、停止距離與特殊推進狀況。';
      if(/maintenance/.test(title)) return '規劃與記錄關鍵安全設備的維護要求，確保設備在需要時可正常使用。';
      if(/training|drill|muster|emergency instructions|recovery of persons/.test(title)) return '讓船員清楚緊急職責、訓練內容與應變程序，提升事故時的反應一致性。';
      if(/fire/.test(title)) return '支援防火、滅火與消防應變，確保船上人員能快速取得消防配置與操作資訊。';
      if(/helicopter/.test(title)) return '規範直升機設施的安全操作、檢查與緊急程序，降低特殊作業風險。';
      if(/lifeboat|life-saving|survival/.test(title)) return '確認救生設備、釋放回收系統或求生資訊符合要求，保障棄船與救助能力。';
      if(/radio|ais|vdr|lrit/.test(title)) return '證明航行通訊、識別、紀錄或追蹤設備經測試並可支援安全航行與事故調查。';
      if(/charts|nautical publications|iamsar|code of signals/.test(title)) return '確保航程規劃、航行安全、通訊與搜救資訊使用的是船上可取得的有效資料。';
      if(/pilot ladder|navigational activities/.test(title)) return '保存航行與引水相關作業紀錄，提供船上管理、事故追溯與查驗依據。';
      if(/cargo|grain|dangerous goods|msds|securing|inf/.test(title)) return '確保貨物資訊、積載、繫固或危險性已被船方掌握，降低貨物作業與航行風險。';
      if(/safety management|document of compliance/.test(title)) return '證明公司與船舶安全管理系統依 ISM Code 建立、執行並經驗證。';
      if(/security|issc|csr|synopsis/.test(title)) return '維持船舶保安與船舶歷史資料的可查性，支援 ISPS 查驗與船舶識別。';
      if(/oil pollution|iopp|oil record|sopep|sewage|garbage|air pollution|ozone|nitrogen oxides|fuel oil|bunker delivery|sox|egc|seemp|energy efficiency|carbon intensity/.test(title)) return '用來證明或記錄船舶防污染、排放控制、能源效率與相關應急安排符合 MARPOL 要求。';
      if(/anti-fouling|ballast water|bwms/.test(title)) return '控制船體防污系統與壓艙水管理風險，降低有害物質或外來生物造成的環境影響。';
      if(/masters|officers|ratings|hours of rest/.test(title)) return '證明船員資格與休息時間符合 STCW 要求，支援安全值班與人員適任性查核。';
      if(/passenger/.test(title)) return '針對客船或載客責任確認安全、營運限制、搜救合作或旅客責任保障已備妥。';
      if(/insurance|financial security|liability|wreck|bunker oil/.test(title) || hasTag('liability')) return '證明船舶對污染、殘骸移除或旅客損害等責任具備法定保險或財務擔保。';
      if(/polar/.test(title)) return '確認船舶在極地水域營運時，具備符合 Polar Code 的船舶能力、限制與操作程序。';
      if(/gas carrier|chemical|certificate of fitness|nls|procedures and arrangements/.test(title)) return '證明特定貨種船舶的構造、設備、操作程序與貨物控制符合專用 Code 或 MARPOL 要求。';
      if(/special purpose|offshore|diving|submersible|dynamically supported|modu|wing-in-ground|high-speed|nuclear/.test(title) || hasTag('special')) return '針對特殊船型、特殊作業或非一般營運模式，確認其安全條件與操作限制已被主管機關接受。';

      if(hasTag('certificate') || /certificate|statement|declaration|document of approval/.test(title)) return '用來證明船舶、設備、公司或安排已完成主管機關要求的檢驗、核准或符合性確認。';
      if(hasTag('record') || /record|logbook/.test(title)) return '用來留下操作、測試、排放、訓練或事件的可追溯紀錄，供船上管理、稽核與查驗。';
      if(hasTag('plan') || /plan|procedure|instructions/.test(title)) return '用來規範船員在正常或緊急情況下的操作步驟，確保船上有一致且可查核的做法。';
      if(hasTag('manual') || /manual|booklet|file/.test(title)) return '用來把設備、貨物、安全或操作資訊放在船上，供船員日常執行與查驗時查閱。';
      if(hasTag('report') || /report/.test(title)) return '用來保存測試、測量或符合性評估結果，證明相關設備或狀態曾被確認。';
      return '提供船上法定查核所需的關鍵資訊，使船員、公司、船旗國與檢查人員能確認適用要求。';
    }"""

purpose_en = """    function purposeFor(item){
      const title = item.title.toLowerCase();
      const tags = item.tags.map(tag => tag.toLowerCase());
      const hasTag = tag => tags.some(t => t.includes(tag));

      if(/tonnage/.test(title)) return 'Confirms gross and net tonnage as the basis for applicability thresholds, fees, surveys, and certificate requirements.';
      if(/load line/.test(title)) return 'Certifies that freeboard, load line marks, and related watertight safety conditions have been approved under the Load Line regime.';
      if(/exemption/.test(title)) return 'Records the scope, conditions, and legal basis of exemptions granted by the Administration.';
      if(/coating/.test(title)) return 'Preserves coating specifications, application, inspection, and maintenance data to support structural corrosion control and follow-up surveys.';
      if(/emergency towing/.test(title)) return 'Provides a ship-specific towing arrangement that can be used immediately in an emergency or blackout situation.';
      if(/construction drawings|ship construction file|ship structure access|technical file|eedi|eexi|engine parameters/.test(title)) return 'Retains design, construction, modification, or calculation evidence so later surveys, maintenance, and compliance checks remain traceable.';
      if(/noise/.test(title)) return 'Confirms onboard noise levels are controlled and support compliance with the noise code for crew work and rest areas.';
      if(/stability|loading information/.test(title)) return 'Gives the master the basis to judge loading, draft, trim, and damage stability and avoid unsafe operational conditions.';
      if(/damage control/.test(title)) return 'Helps the crew identify watertight subdivisions, closing arrangements, and control measures after flooding or damage.';
      if(/manoeuvring/.test(title)) return 'Provides bridge personnel with manoeuvring performance, stopping distances, and special propulsion conditions.';
      if(/maintenance/.test(title)) return 'Defines and records maintenance requirements for key safety systems so equipment remains ready for use.';
      if(/training|drill|muster|emergency instructions|recovery of persons/.test(title)) return 'Ensures crew understand emergency duties, drills, and response procedures for consistent action in an incident.';
      if(/fire/.test(title)) return 'Supports fire prevention, firefighting, and emergency response by making fire arrangements and operating information available onboard.';
      if(/helicopter/.test(title)) return 'Defines safe operation, inspection, and emergency procedures for helicopter facilities and related special operations.';
      if(/lifeboat|life-saving|survival/.test(title)) return 'Confirms life-saving appliances, release/recovery systems, or survival information meet requirements for abandonment and rescue.';
      if(/radio|ais|vdr|lrit/.test(title)) return 'Demonstrates that communication, identification, recording, or tracking equipment has been tested and supports safe navigation and investigation.';
      if(/charts|nautical publications|iamsar|code of signals/.test(title)) return 'Ensures voyage planning, navigation safety, communications, and SAR information are available in valid onboard form.';
      if(/pilot ladder|navigational activities/.test(title)) return 'Preserves records of navigation and pilot-transfer operations for onboard management, incident follow-up, and inspection.';
      if(/cargo|grain|dangerous goods|msds|securing|inf/.test(title)) return 'Ensures cargo information, stowage, securing, or hazard data are known to the ship and reduce cargo-handling and voyage risks.';
      if(/safety management|document of compliance/.test(title)) return 'Demonstrates that the company and ship SMS are established, implemented, and verified under the ISM Code.';
      if(/security|issc|csr|synopsis/.test(title)) return 'Maintains ship security and historical ship identity information to support ISPS verification and identification.';
      if(/oil pollution|iopp|oil record|sopep|sewage|garbage|air pollution|ozone|nitrogen oxides|fuel oil|bunker delivery|sox|egc|seemp|energy efficiency|carbon intensity/.test(title)) return 'Proves or records pollution prevention, emission control, energy efficiency, and related emergency arrangements under MARPOL.';
      if(/anti-fouling|ballast water|bwms/.test(title)) return 'Controls anti-fouling and ballast water management risks and reduces harmful substances or invasive species impacts.';
      if(/masters|officers|ratings|hours of rest/.test(title)) return 'Demonstrates seafarer certification and rest-hour compliance under STCW for safe watchkeeping and manning checks.';
      if(/passenger/.test(title)) return 'Covers passenger-ship safety, operating limits, SAR cooperation, or passenger liability arrangements as applicable.';
      if(/insurance|financial security|liability|wreck|bunker oil/.test(title) || hasTag('liability')) return 'Demonstrates statutory insurance or financial security for pollution, wreck removal, or passenger claims.';
      if(/polar/.test(title)) return 'Confirms polar ship capability, limitations, and operating procedures required under the Polar Code.';
      if(/gas carrier|chemical|certificate of fitness|nls|procedures and arrangements/.test(title)) return 'Demonstrates that construction, equipment, procedures, and cargo control meet the relevant cargo Code or MARPOL requirements.';
      if(/special purpose|offshore|diving|submersible|dynamically supported|modu|wing-in-ground|high-speed|nuclear/.test(title) || hasTag('special')) return 'Covers special ship types or operations where safety conditions and operating limits must be accepted by the Administration.';

      if(hasTag('certificate') || /certificate|statement|declaration|document of approval/.test(title)) return 'Certifies that the ship, equipment, company, or arrangement has been surveyed, approved, or found in compliance by the Administration.';
      if(hasTag('record') || /record|logbook/.test(title)) return 'Creates a traceable record of operations, tests, discharges, drills, or events for onboard management, audit, and inspection.';
      if(hasTag('plan') || /plan|procedure|instructions/.test(title)) return 'Defines the steps crew should follow in normal or emergency situations so onboard practice is consistent and auditable.';
      if(hasTag('manual') || /manual|booklet|file/.test(title)) return 'Places equipment, cargo, safety, or operating information onboard for daily use and inspection.';
      if(hasTag('report') || /report/.test(title)) return 'Retains test, measurement, or compliance assessment results showing that equipment or conditions were verified.';
      return 'Provides key onboard information so crew, company, flag State, and inspectors can confirm applicable requirements.';
    }"""

if purpose_zh not in text:
    raise SystemExit("purposeFor block not found")
text = text.replace(purpose_zh, purpose_en)

replacements = [
    ('<html lang="zh-Hant">', '<html lang="en">'),
    ('content="依 IMO MSC.1/Circ.1646（2022）整理船上應攜帶證書與文件可搜尋資料庫，含英文原名、中文翻譯、目的摘要、適用條件與法規引用。"',
     'content="Searchable database of certificates and documents required to be carried on board ships under IMO MSC.1/Circ.1646 (2022), with purpose summaries, applicability notes, and regulatory references."'),
    ('content="MSC.1/Circ.1646 船上應攜帶證書與文件清單｜Reay\'s Note"', 'content="MSC.1/Circ.1646 On-board Certificates and Documents | Reay\'s Note"', 2),
    ('content="快速掌握船舶航行與營運時船上應備證書、手冊、計畫、紀錄與保險文件；含可搜尋的 127 項證書資料庫與實務查核流程。"',
     'content="A practical guide to certificates, manuals, plans, records, reports, and insurance documents required during ship operation, including a searchable database of 127 items and a step-down verification workflow."'),
    ('content="zh_TW"', 'content="en_US"'),
    ('onboard-certificates.html', 'onboard-certificates.en.html', 4),
    ('onboard-certificates.en.html', 'onboard-certificates.html', 2),
    ('family=Noto+Sans+TC', 'family=Source+Sans+Pro:wght@400;600;700&family=Noto+Sans+TC'),
    ('--sans:-apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans TC","Microsoft JhengHei",Arial,sans-serif;',
     '--sans:"Source Sans Pro",-apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans TC",Arial,sans-serif;'),
    ('MSC.1/Circ.1646 船上應攜帶證書與文件清單｜Reay\'s Note</title>',
     'MSC.1/Circ.1646 On-board Certificates and Documents | Reay\'s Note</title>'),
    ('<a href="../index.html">← 海事筆記</a>', '<a href="../index.en.html">← Maritime Notes</a>'),
    ('<a href="../../index.zh.html">首頁</a>', '<a href="../../index.html">Home</a>'),
    ('<a href="../../about.html">關於我</a>', '<a href="../../about.en.html">About</a>'),
    ('<a href="../../research/index.html">管理筆記</a>', '<a href="../../research/index.en.html">Management Notes</a>'),
    ('<a href="onboard-certificates.en.html" lang="en" hreflang="en" class="is-soon" tabindex="-1" aria-disabled="true" title="英文版製作中">EN</a>',
     '<a href="onboard-certificates.en.html" lang="en" hreflang="en" aria-current="true">EN</a>'),
    ('<a href="onboard-certificates.html" lang="zh-Hant" hreflang="zh-Hant" aria-current="true">繁中</a>',
     '<a href="onboard-certificates.html" lang="zh-Hant" hreflang="zh-Hant">繁中</a>'),
    ('<h1>船上應攜帶證書與文件清單</h1>',
     '<h1>On-board Certificates and Documents</h1>'),
    ('<span>📅 更新：2026-06-30</span>', '<span>📅 Updated: 2026-06-30</span>'),
    ('<span>⏱ 閱讀約 18 分鐘</span>', '<span>⏱ About 18 min read</span>'),
    ('<span>🏷 MSC.1/Circ.1646 / 船上證書 / PSC / SOLAS / MARPOL</span>',
     '<span>🏷 MSC.1/Circ.1646 / On-board certificates / PSC / SOLAS / MARPOL</span>'),
    ('<p class="subtitle">快速掌握船舶航行與營運時，船上通常應備有哪些證書、手冊、計畫、紀錄、報告與保險文件。內容依 IMO MSC.1/Circ.1646（2022）版本整理，協助先判斷文件目的、適用船型與查核方向。</p>',
     '<p class="subtitle">A practical index of certificates, manuals, plans, records, reports, and insurance documents normally required on board during ship operation. Based on IMO MSC.1/Circ.1646 (2022), it helps you judge document purpose, ship-type applicability, and inspection focus before going to the source instruments.</p>'),
    ('<span class="pill">🗓️ 27 Jun 2022 文件發佈</span>', '<span class="pill">🗓️ 27 Jun 2022 publication</span>'),
    ('href="#database">快速前往證書資料庫</a>', 'href="#database">Go to certificate database</a>'),
    ('data-share-copy="複製連結"', 'data-share-copy="Copy link"', 2),
    ('data-share-copied="已複製"', 'data-share-copied="Copied"', 2),
    ('data-toast-copied="連結已複製到剪貼簿"', 'data-toast-copied="Link copied to clipboard"', 2),
    ('data-share-email-body="我在 Reay 的海事筆記看到這篇，覺得可能對你有幫助：&#10;&#10;MSC.1/Circ.1646 船上應攜帶證書與文件清單｜Reay\'s Note&#10;https://reayhuang.com/notes/maritime/onboard-certificates.html"',
     'data-share-email-body="I thought you might find this useful from Reay\'s maritime notes:&#10;&#10;MSC.1/Circ.1646 On-board Certificates and Documents | Reay\'s Note&#10;https://reayhuang.com/notes/maritime/onboard-certificates.en.html"', 2),
    ('data-share-title="MSC.1/Circ.1646 船上應攜帶證書與文件清單｜Reay\'s Note"', 'data-share-title="MSC.1/Circ.1646 On-board Certificates and Documents | Reay\'s Note"', 2),
    ('<p class="article-share__label" id="share-hero-label">分享此篇</p>', '<p class="article-share__label" id="share-hero-label">Share this note</p>'),
    ('<h2>閱讀前先抓住 4 個原則</h2>', '<h2>Four principles before you start</h2>'),
    ('<b>不是所有船都全數適用</b><span>依船型、GT、船齡、航線、公約適用性、貨種與設備判斷。</span>',
     '<b>Not every item applies to every ship</b><span>Filter by ship type, GT, age, trading pattern, convention status, cargo, and equipment.</span>'),
    ('<b>只整理 IMO instruments</b><span>Flag/Class/Port/Charterer 額外要求需另查。</span>',
     '<b>IMO instruments only</b><span>Flag, class, port, and charterer requirements are outside this list.</span>'),
    ('<b>電子證書與電子紀錄可被接受</b><span>需依 IMO 電子證書與 MARPOL 電子紀錄指引。</span>',
     '<b>Electronic certificates and records are acceptable</b><span>They must follow the relevant IMO guidelines and remain accessible onboard.</span>'),
    ('<b>PSC 查驗仍回到公約條文</b><span>本通函是清單導覽，不取代原始公約要求。</span>',
     '<b>PSC still relies on convention text</b><span>This circular is an index, not a substitute for the underlying instruments.</span>'),
    ('<a href="#overview">概覽</a>', '<a href="#overview">Overview</a>'),
    ('<a href="#logic">查核邏輯</a>', '<a href="#logic">Workflow</a>'),
    ('<a href="#database">證書資料庫</a>', '<a href="#database">Database</a>'),
    ('<a href="#shiptype">船型提醒</a>', '<a href="#shiptype">Ship types</a>'),
    ('<a href="#notes">注意事項</a>', '<a href="#notes">Notes</a>'),
    ('<h2>一頁掌握文件定位</h2>', '<h2>What this list is for</h2>'),
    ('<p class="lead">本文件是 IMO 對船舶航行與營運時應在船上備妥的文件與證書清單，核心價值是把各公約要求的證書、手冊、計畫、紀錄與報告集中列成索引。FAL.2/Circ.133、MEPC.1/Circ.902、MSC.1/Circ.1646、LEG.2/Circ.4 分別由 IMO 不同委員會以各自 circular 編號發布，但內容對應的是同一份 2022 年清單。實務查核時，建議用「通用要求 → 船型 → 貨種 → 設備 → 紀錄保存」的順序。</p>',
     '<p class="lead">This is IMO\'s consolidated index of certificates and documents required to be carried on board ships. FAL.2/Circ.133, MEPC.1/Circ.902, MSC.1/Circ.1646, and LEG.2/Circ.4 are issued by different IMO bodies but refer to the same 2022 list. In practice, work through general requirements first, then ship type, cargo, equipment, and record-keeping.</p>'),
    ('<h3>整理項目</h3><p>涵蓋證書、手冊、計畫、紀錄、測試報告與保險文件。</p>',
     '<h3>Indexed items</h3><p>Certificates, manuals, plans, records, test reports, and insurance documents.</p>'),
    ('<h3>主要適用章節</h3><p>從全船通用、客船、貨船，到化學船、氣體船、極地與低閃點燃料。</p>',
     '<h3>Main sections</h3><p>From all ships and passenger/cargo ships to chemical tankers, gas carriers, polar waters, and low-flashpoint fuels.</p>'),
    ('<h3>主要公約族群</h3><p>SOLAS、MARPOL、STCW、BWM、AFS、CLC/Bunkers/WRC 等。</p>',
     '<h3>Convention families</h3><p>SOLAS, MARPOL, STCW, BWM, AFS, CLC/Bunkers/WRC, and more.</p>'),
    ('<h3>新版清單</h3><p>用於取代 2017 版 circular 清單，適合作為文件更新基準。</p>',
     '<h3>2022 edition</h3><p>Replaces the 2017 circular list and is a useful baseline for document updates.</p>'),
    ('<h3>✅ 適合用來做什麼</h3><p>建立船上證書 index、交船/接船文件檢查表、內部 audit 準備、LR/Flag/ISM/ISPS 文件盤點前的第一層導覽。</p>',
     '<h3>✅ Good uses</h3><p>Building an onboard certificate index, delivery/redelivery checklists, internal audit prep, and a first-pass review before LR/Flag/ISM/ISPS document checks.</p>'),
    ('<h3>⚠️ 不適合直接當成唯一依據</h3><p>不要只用這份清單判斷缺失。最後仍要回到對應公約、Code、Flag Administration 指示、Class Rules、PSC inspection practice 與船舶實際設備。</p>',
     '<h3>⚠️ Not a stand-alone compliance basis</h3><p>Do not use this list alone to judge deficiencies. Always return to the governing convention, code, flag Administration instruction, class rules, PSC practice, and the ship\'s actual configuration.</p>'),
    ('<h2>建議查核流程：由大到小篩選</h2>', '<h2>Recommended workflow: filter from broad to narrow</h2>'),
    ('<p class="lead">這份通函不是「全部打勾」的清單，而是「逐層篩選」的清單。以下流程可以避免把不適用文件誤判成缺失。</p>',
     '<p class="lead">This is not a universal tick-all list. It is a layered filter. The workflow below helps avoid treating non-applicable documents as deficiencies.</p>'),
    ('<h3>確認船舶基本屬性</h3><p>船型、GT、國際航線、公約締約國、建造日期與改裝日期。</p>',
     '<h3>Confirm ship particulars</h3><p>Ship type, GT, trading pattern, convention status, build date, and major conversion dates.</p>'),
    ('<h3>先套用通用項目</h3><p>證書、船舶安全/防污/保安/船員與記錄類文件。</p>',
     '<h3>Apply general items first</h3><p>Certificates plus safety, pollution-prevention, security, crew, and record-type documents.</p>'),
    ('<h3>再依船型加項</h3>', '<h3>Add ship-type items</h3>'),
    ('<h3>依貨種與營運加項</h3>', '<h3>Add cargo and operation items</h3>'),
    ('<h3>依設備加項</h3>', '<h3>Add equipment-driven items</h3>'),
    ('<h3>確認形式與有效性</h3><p>Valid、approved、endorsed、on board、accessible、updated，電子文件需符合指引。</p>',
     '<h3>Check form and validity</h3><p>Valid, approved, endorsed, on board, accessible, updated; electronic documents must follow the relevant guidelines.</p>'),
    ('<h2>公約主題地圖</h2>', '<h2>Convention map</h2>'),
    ('<p class="lead">把清單轉成查核思維：看到文件名稱時先辨識它屬於哪一類要求。</p>',
     '<p class="lead">Use this map to recognise which regulatory family a document belongs to before you inspect it.</p>'),
    ('<th>主題</th><th>常見文件類型</th><th>實務查核焦點</th>',
     '<th>Theme</th><th>Typical document types</th><th>Practical inspection focus</th>'),
    ('<td>有效期限、附錄 Form、船上張貼/可取得、設備測試報告、替代設計與豁免。</td>',
     '<td>Validity, attached forms, onboard availability/posting, equipment test reports, alternative design and exemptions.</td>'),
    ('<td>GT 門檻、貨種、排放控制區、BDN/sample 保存、CII/EEXI/SEEMP 更新。</td>',
     '<td>GT thresholds, cargo type, emission control areas, BDN/sample retention, CII/EEXI/SEEMP updates.</td>'),
    ('<td>正本可得性、職務相符、休息時間紀錄完整性。</td>',
     '<td>Availability of originals, rank competence, completeness of rest-hour records.</td>'),
    ('<td>ISM/ISPS 認證、CSR 連續性、SSP 與保安紀錄保存。</td>',
     '<td>ISM/ISPS certification, CSR continuity, SSP and security record retention.</td>'),
    ('<td>只在特定船型、貨物或航區適用，容易因「偶爾營運」被漏掉。</td>',
     '<td>Applies only to specific ship types, cargoes, or areas and is often missed when operation is occasional.</td>'),
    ('<td>GT/載客/載油門檻、締約國、證書格式與簽發/認可機構。</td>',
     '<td>GT/passenger/oil thresholds, contracting States, certificate format, and issuing/recognised authority.</td>'),
    ('<h2>證書與文件快速搜尋表</h2>', '<h2>Searchable certificate and document table</h2>'),
    ('<p class="lead">可用關鍵字搜尋 certificate、manual、record、SOLAS、MARPOL、IGF、Polar、BWMS 等。按分類鈕可快速縮小範圍。</p>',
     '<p class="lead">Search by certificate, manual, record, SOLAS, MARPOL, IGF, Polar, BWMS, and more. Use the filter buttons to narrow the list quickly.</p>'),
    ('placeholder="搜尋：例如 SEEMP、Cargo Ship Safety、MARPOL Annex VI、gas carrier、record book..."',
     'placeholder="Search: e.g. SEEMP, Cargo Ship Safety, MARPOL Annex VI, gas carrier, record book..."'),
    ('data-filter="all">全部</button>', 'data-filter="all">All</button>'),
    ('data-filter="Record">紀錄</button>', 'data-filter="Record">Records</button>'),
    ('data-filter="Liability">保險</button>', 'data-filter="Liability">Insurance</button>'),
    ('data-filter="Special">特殊船/貨</button>', 'data-filter="Special">Special</button>'),
    ('<span>分類：</span>', '<span>Tags:</span>'),
    ('<th style="width:11%">章節</th>', '<th style="width:11%">Section</th>'),
    ('<th style="width:31%">證書/文件</th>', '<th style="width:31%">Certificate / document</th>'),
    ('<th>適用性摘要</th>', '<th>Applicability summary</th>'),
    ('<div id="empty" class="empty">找不到符合條件的項目。請換一個關鍵字或改用「全部」。</div>',
     '<div id="empty" class="empty">No matching items. Try another keyword or switch back to All.</div>'),
    ('<h2>船型/貨種容易漏看的提醒</h2>', '<h2>Ship-type and cargo reminders</h2>'),
    ('<p class="lead">實務上最常出錯的不是「不知道有這份文件」，而是「沒有判斷它什麼時候才適用」。</p>',
     '<p class="lead">The most common mistake is not ignorance of a document, but failing to judge when it actually applies.</p>'),
    ('<summary>油輪 / 化學船 / 氣體船</summary>', '<summary>Oil / chemical / gas tankers</summary>'),
    ('<summary>新環保/能源效率文件</summary>', '<summary>New environmental / energy-efficiency documents</summary>'),
    ('<summary>特殊航區與特殊燃料</summary>', '<summary>Special areas and special fuels</summary>'),
    ('<summary>紀錄類文件</summary>', '<summary>Record-type documents</summary>'),
    ('<li>500 GT and over：Cargo Ship Safety Construction / Equipment 等。</li>',
     '<li>500 GT and over: Cargo Ship Safety Construction / Equipment, etc.</li>'),
    ('<li>300 GT and over 且裝有 radio installation：Cargo Ship Safety Radio Certificate。</li>',
     '<li>300 GT and over with a radio installation: Cargo Ship Safety Radio Certificate.</li>'),
    ('<li>油輪、散裝船需額外注意 ESP、Ship Structure Access Manual、CAS、ODMC、COW、STS、VOC 等。</li>',
     '<li>Oil tankers and bulk carriers also need ESP, Ship Structure Access Manual, CAS, ODMC, COW, STS, VOC, and related items.</li>'),
    ('<li>除了 section 1 通用項目，還需 Passenger Ship Safety Certificate、decision support system、SAR cooperation plan、operational limitations list。</li>',
     '<li>In addition to section 1 general items: Passenger Ship Safety Certificate, decision support system, SAR cooperation plan, and operational limitations list.</li>'),
    ('<li>載客超過 12 人時，需留意 passenger liability insurance certificate。</li>',
     '<li>Licensed to carry more than 12 passengers: passenger liability insurance certificate.</li>'),
    ('<li>SEEMP、IEEC、Statement of Compliance - Fuel Oil Consumption and CII、EEXI Technical File 是近年船隊管理常見重點。</li>',
     '<li>SEEMP, IEEC, fuel-oil consumption / CII statements, and EEXI Technical Files are common fleet-management focus areas.</li>'),
    ('<li>EGCS 船舶需 SOx Emission Compliance Certificate 與 EGC System Technical Manual。</li>',
     '<li>Ships with EGCS need the SOx Emission Compliance Certificate and EGC System Technical Manual.</li>'),
    ('<li>Polar waters：Polar Ship Certificate 與 PWOM。</li>',
     '<li>Polar waters: Polar Ship Certificate and PWOM.</li>'),
    ('<li>使用 gas 或 low-flashpoint fuels：IGF Code 相關 maintenance / emergency / operational procedures 與 fuel handling manual。</li>',
     '<li>Ships using gas or low-flashpoint fuels: IGF Code maintenance, emergency, and operational procedures plus fuel-handling manual.</li>'),
    ('<li>Record books 不只要在船上，還要可讀、更新、保存期限符合要求。</li>',
     '<li>Record books must be onboard, readable, up to date, and retained for the required period.</li>'),
    ('<li>常見：Oil/Garbage/Ballast/Cargo Record Book、hours of rest、VDR/AIS/LRIT test reports、pilot ladder records、navigational activities records。</li>',
     '<li>Common examples: oil/garbage/ballast/cargo record books, hours of rest, VDR/AIS/LRIT test reports, pilot ladder records, and navigational activity records.</li>'),
    ('<h2>使用這份 HTML 筆記的注意事項</h2>', '<h2>Important notes on using this page</h2>'),
    ('<p class="lead">此頁是工作用視覺化整理，不是官方文件本身；正式判定仍須以最新 IMO instruments、Flag Administration、Class/RO 指示與船舶實際配置為準。</p>',
     '<p class="lead">This page is a working visual note, not an official instrument. Formal decisions must follow the latest IMO instruments, flag Administration guidance, class/RO instructions, and the ship\'s actual configuration.</p>'),
    ('<h3>資料範圍</h3><p>僅整理 IMO instruments 下要求船上攜帶的文件，不包含其他國際組織、政府機關、港口、租家或公司 SMS 額外要求。</p>',
     '<h3>Scope</h3><p>Covers only documents required under IMO instruments to be carried on board. It does not include other organisations, authorities, ports, charterers, or company SMS extras.</p>'),
    ('<h3>電子文件</h3><p>電子證書與電子紀錄需符合 IMO 相關 Guidelines，並確保船上可展示、可驗證、可讀取。</p>',
     '<h3>Electronic documents</h3><p>Electronic certificates and records must follow the relevant IMO guidelines and remain demonstrable, verifiable, and readable onboard.</p>'),
    ('<h3>PSC / 缺失判斷</h3><p>PSC 或正式缺失判斷時，應回到對應公約、Code、Flag circular、RO instructions 及具體條文。</p>',
     '<h3>PSC / deficiency decisions</h3><p>For PSC or formal deficiency decisions, return to the governing convention, code, flag circular, RO instruction, and specific regulation.</p>'),
    ('<p class="article-share__label" id="share-end-label">覺得有用？分享給同事</p>',
     '<p class="article-share__label" id="share-end-label">Found this useful? Share it</p>'),
    ('<strong>MSC.1/Circ.1646 船上應攜帶證書與文件清單｜Reay\'s Note</strong>',
     '<strong>MSC.1/Circ.1646 On-board Certificates and Documents | Reay\'s Note</strong>'),
    ('<span class="small">整理：Reay Huang · Maritime Survey / Learning Note</span>',
     '<span class="small">Compiled by Reay Huang · Maritime Survey / Learning Note</span>'),
    ('本頁為學習、內訓與驗船準備用途的視覺化整理，不代表 Lloyd\'s Register、IMO 或其他機構之正式意見；<span class="disclaimer-tail">正式接船、PSC 查驗、缺失判定與文件合規，仍應以最新 IMO instruments、船旗國主管機關指示、船級社規範與船舶實際配置為準。</span>',
     'This page is a visual working note for learning, internal training, and survey preparation. It does not represent the official position of Lloyd\'s Register, IMO, or any other body; <span class="disclaimer-tail">formal delivery, PSC inspection, deficiency decisions, and document compliance must still follow the latest IMO instruments, flag Administration instructions, class rules, and the ship\'s actual configuration.</span>'),
    ('<span class="summary-label">目的</span>', '<span class="summary-label">Purpose</span>'),
    ('<span class="summary-label muted">條件</span>', '<span class="summary-label muted">Applicability</span>'),
    ("item.sec.split('｜')[0]", "item.sec.split('|')[0]"),
]

for item in replacements:
    if len(item) == 2:
        old, new = item
        count = None
    else:
        old, new, count = item
    if count is None:
        if text.count(old) != text.count(new) and old not in text:
            raise SystemExit(f"Missing replacement: {old[:60]}")
        text = text.replace(old, new)
    else:
        text = text.replace(old, new, count)

# Translate Chinese trigger fragments commonly used in items
trigger_map = {
    "總噸位與淨噸位依 Tonnage 1969 決定的船舶。": "Ships whose gross and net tonnage are determined under Tonnage 1969.",
    "依 Load Line Convention / 1988 LL Protocol 完成檢驗與標誌的船舶。": "Ships surveyed and marked under the Load Line Convention / 1988 LL Protocol.",
    "取得 Load Line exemption 的船舶。": "Ships granted a Load Line exemption.",
    "依 SOLAS 1974 或 SOLAS Protocol 1988 取得豁免時，須另發豁免證書。": "Where an exemption is granted under SOLAS 1974 or the 1988 SOLAS Protocol, a separate exemption certificate is required.",
    "適用於所有船舶 dedicated seawater ballast tanks、150 m 以上 bulk carrier 的 double-side skin spaces，以及 crude oil tanker cargo oil tanks 等。": "Applies to dedicated seawater ballast tanks on all ships, double-side skin spaces on bulk carriers of 150 m and above, crude oil tanker cargo oil tanks, etc.",
    "所有船舶需有 ship-specific emergency towing procedure，供緊急情況使用。": "All ships must carry a ship-specific emergency towing procedure for emergency use.",
    "2007-01-01 或以後建造船舶，需保存 as-built drawings 與後續結構變更圖。": "Ships built on or after 1 January 2007 must retain as-built drawings and subsequent structural alteration drawings.",
    "適用於 150 m 以上 oil tankers，以及符合特定結構型式與日期門檻的 150 m 以上 bulk carriers；排除 ore carriers and combination carriers。": "Applies to oil tankers of 150 m and above and certain bulk carriers of 150 m and above; excludes ore carriers and combination carriers.",
    "新船 1,600 GT and above，排除部分特殊船舶；報告需在船上並可供船員取得。": "New ships of 1,600 GT and above, subject to exclusions; the report must be onboard and available to the crew.",
    "客船不論大小、貨船 24 m and over；含完整/破損穩性與相關 loading information。": "Passenger ships regardless of size and cargo ships of 24 m and over; includes intact/damage stability and related loading information.",
    "客船與貨船需展示防水艙區、開口、關閉裝置與糾正傾側配置等資訊。": "Passenger and cargo ships must display watertight subdivision, openings, closing arrangements, and corrective list information.",
    "試航記錄的停止時間、航向與距離等操船資訊需供船長或指定人員使用。": "Trial-recorded stopping time, heading, and distance data must be available to the master or designated personnel.",
    "如採用 alternative design/arrangements，需攜帶經主管機關核准之符合性文件副本。": "Where alternative design or arrangements are used, an approved copy of the compliance evaluation must be carried.",
    "涵蓋 fire protection systems、fire-fighting systems and appliances；油輪與大型客船有補充要求。": "Covers fire protection systems and fire-fighting systems and appliances; additional requirements apply to tankers and large passenger ships.",
    "Fire drills 需依 SOLAS III/19.3、III/19.5 執行並記錄。": "Fire drills must be conducted and recorded in accordance with SOLAS III/19.3 and III/19.5.",
    "以船上工作語言撰寫，置於 mess room/recreation room 或船員艙房；可用影音部分替代。": "Prepared in the ship's working language and placed in the mess/recreation room or crew accommodation; audio-visual material may replace part of the manual.",
    "消防控制圖/手冊需展示、更新，並於 deckhouse 外部有防風雨副本供岸方消防使用。": "Fire control plans/booklets must be displayed, kept up to date, and a weatherproof copy must be available externally for shore firefighting.",
    "提供船舶與貨物操作之 fire safety 資訊，可與 fire safety training manual 合併。": "Provides fire safety information for ship and cargo operations; may be combined with the fire safety training manual.",
    "如設有 helicopter facility，需有操作手冊、風險預防、程序與設備需求 checklist。": "Where a helicopter facility is provided, an operations manual, risk prevention, procedures, and equipment checklist are required.",
    "既有 lifeboat on-load release mechanism 換裝符合 LSA Code 時之接受聲明。": "Statement of acceptance when an existing lifeboat on-load release mechanism is replaced with an LSA Code-compliant system.",
    "所有船舶需於船橋、機艙、居住區等顯著處張貼；客船有語言要求。": "Must be posted conspicuously on the bridge, in the engine room, and in accommodation spaces; passenger ships have language requirements.",
    "所有船舶需有救回落水人員之 ship-specific plans/procedures。": "All ships must carry ship-specific plans and procedures for recovery of persons from the water.",
    "生命救生設備與最佳求生方法之易懂指引，必要時可分卷或用影音取代部分內容。": "Understandable guidance on lifesaving appliances and survival methods; may be split into volumes or partly replaced by audio-visual material.",
    "與無線電通信服務相關且對海上人命安全重要的事故需記錄。": "Records incidents related to radiocommunication services that are important to safety of life at sea.",
    "適用 SOLAS chapter I 的船舶需有主管機關簽發之 minimum safe manning document 或等同文件。": "Ships subject to SOLAS chapter I must carry a minimum safe manning document or equivalent issued by the Administration.",
    "VDR annual performance test 後，測試機構簽發之 compliance certificate 需留船。": "After the annual VDR performance test, the compliance certificate issued by the testing organisation must be kept onboard.",
    "AIS annual test 由 approved surveyor/testing/servicing facility 執行，測試報告需留船。": "AIS annual testing by an approved surveyor/testing/servicing facility; the test report must be kept onboard.",
    "預定航程用 charts/publications 需足夠且更新；ECDIS 可滿足 chart carriage requirements。": "Charts and publications for the intended voyage must be adequate and up to date; ECDIS may satisfy chart carriage requirements.",
    "LRIT conformance test 完成後，由 Administration 或 ASP 簽發測試報告。": "After LRIT conformance testing, a test report is issued by the Administration or ASP.",
    "需裝設無線電設備的船舶攜帶 International Code of Signals；所有船舶攜帶最新版 IAMSAR Vol. III。": "Ships fitted with radio installations carry the International Code of Signals; all ships carry the latest IAMSAR Volume III.",
    "Pilot ladders 需可識別並記錄投入使用日期與修理情形。": "Pilot ladders must be identifiable and their date of entry into service and repairs recorded.",
    "國際航行船舶需保存 navigational activities/incidents，包括 drills 與 pre-departure tests。": "Ships on international voyages must retain records of navigational activities/incidents, including drills and pre-departure tests.",
    "除 solid/liquid bulk cargoes 外，裝載/堆裝/繫固需依主管機關核准之 CSM。": "Except for solid/liquid bulk cargoes, loading/stowage/securing must follow an Administration-approved Cargo Securing Manual.",
    "載運油或油燃料船舶，於 bulk oil cargo loading 或 bunkering 前提供 MSDS。": "Ships carrying oil or oil fuel must provide MSDS before bulk oil cargo loading or bunkering.",
    "船舶 SMS 與公司系統經驗證符合 ISM Code 後簽發。": "Issued after the ship SMS and company system are verified against the ISM Code.",
    "公司符合 ISM Code 時簽發 DOC；副本需留船。": "Issued when the company complies with the ISM Code; a copy must be kept onboard.",
    "適用 SOLAS chapter I 的船舶需有 CSR，作為船舶歷史資訊的船上紀錄。": "Ships subject to SOLAS chapter I must carry a CSR as the onboard record of ship history.",
    "船上需有 approved SSP；保安訓練、威脅、事件、保安等級變更、SSAS 測試等紀錄需保存。": "An approved SSP must be onboard; records of security training, threats, incidents, security-level changes, and SSAS tests must be retained.",
    "證明船舶符合 SOLAS XI-2 與 ISPS Code Part A；可有 interim ISSC。": "Demonstrates compliance with SOLAS XI-2 and ISPS Code Part A; an interim ISSC may be issued.",
    "UNSP barge 可依 MARPOL Annex I/IV/VI 取得某些檢驗與發證豁免。": "UNSP barges may be granted certain survey and certification exemptions under MARPOL Annexes I/IV/VI.",
    "Oil tanker 150 GT and above；其他船舶 400 GT and above，且航行至其他 MARPOL 締約方管轄港口/設施。": "Oil tankers of 150 GT and above; other ships of 400 GT and above trading to MARPOL party ports/facilities.",
    "Oil tanker 150 GT and above 及其他船舶 400 GT and above 需 Part I；油輪另需 Part II。": "Oil tankers of 150 GT and above and other ships of 400 GT and above need Part I; oil tankers also need Part II.",
    "Oil tanker 150 GT and above；其他船舶 400 GT and above 需攜帶 approved SOPEP。": "Oil tankers of 150 GT and above and other ships of 400 GT and above must carry an approved SOPEP.",
    "需符合 MARPOL Annex IV 且航行至其他締約方港口/設施的船舶。": "Ships subject to MARPOL Annex IV and trading to other party ports/facilities.",
    "儲存在 holding tanks 的未處理污水以適度速率排放時，需主管機關批准速率。": "Where untreated sewage in holding tanks is discharged at a moderate rate, the discharge rate must be approved by the Administration.",
    "100 GT and above、或核准載 15 人以上船舶、固定/浮動平台需有垃圾管理計畫。": "Ships of 100 GT and above, ships certified to carry 15 or more persons, and fixed/floating platforms need a garbage management plan.",
    "400 GT and above、或核准載 15 人以上且航行至其他締約方港口/設施的船舶，以及固定/浮動平台。": "Ships of 400 GT and above, ships certified to carry 15 or more persons trading to other party ports/facilities, and fixed/floating platforms.",
    "以 EGC system 作為 MARPOL Annex VI regulation 14 替代符合方式的船舶。": "Ships using an EGC system as an alternative means of compliance with MARPOL Annex VI regulation 14.",
    "400 GT and above 船舶；5,000 GT and above 需包含 data collection/reporting 方法與 CII 相關內容。": "Ships of 400 GT and above; ships of 5,000 GT and above must include fuel-data collection/reporting and CII-related content.",
    "400 GT and above 國際航行船舶，以及相關平台/鑽井裝置依 MARPOL Annex VI regulation 6。": "International ships of 400 GT and above, and relevant platforms/rigs under MARPOL Annex VI regulation 6.",
    "400 GT and above 船舶，在前往其他締約方港口/設施前需依 survey 簽發。": "Ships of 400 GT and above must be issued following survey before proceeding to another party port/facility.",
    "5,000 GT and above 船舶需申報 fuel oil consumption；2023 年後相關船型另需 CII 評級符合聲明。": "Ships of 5,000 GT and above must report fuel-oil consumption; from 2023, relevant ship types also need a CII rating statement of compliance.",
    "受 MARPOL Annex VI regulation 6.1 約束且含可充填 ODS 系統的船舶。": "Ships subject to MARPOL Annex VI regulation 6.1 with rechargeable ODS systems.",
    "適用 MARPOL Annex VI 13.5.1，且 certified to both Tier II and Tier III 或 Tier II only 的 marine diesel engines；進入/離開 NOx Tier III ECA 或狀態變更時需記錄日期、時間與船位。": "Applies under MARPOL Annex VI 13.5.1 to marine diesel engines certified Tier II/Tier III or Tier II only; date, time, and position must be recorded when entering/leaving a NOx Tier III ECA or changing status.",
    "使用不同燃油符合 ECA 硫含量要求之船舶，需 fuel changeover written procedure 與記錄。": "Ships using different fuels to meet ECA sulphur limits need a written fuel changeover procedure and record.",
    "依 MARPOL Annex VI regulation 16.6.1 安裝之 incinerator，需保存製造商操作手冊。": "For incinerators installed under MARPOL Annex VI regulation 16.6.1, the manufacturer's operating manual must be kept.",
    "燃油交付之 BDN 與代表樣品需依 MARPOL Annex VI 要求留船。": "Bunker delivery notes and representative samples must be kept onboard under MARPOL Annex VI.",
    "適用 MARPOL Annex VI regulation 22.1 指定船型；含 attained EEDI 計算資料與計算過程。": "Applies to ship types under MARPOL Annex VI regulation 22.1; includes attained EEDI calculation data and methodology.",
    "適用 MARPOL Annex VI regulation 23.1 指定船型；含 attained EEXI 計算資料與過程。": "Applies to ship types under MARPOL Annex VI regulation 23.1; includes attained EEXI calculation data and methodology.",
    "每台船上 marine diesel engine 需有經主管機關核准並伴隨引擎全壽期的 NOx Technical File。": "Each marine diesel engine onboard must have an Administration-approved NOx Technical File kept with the engine for its lifetime.",
    "採 Engine Parameter Check method 驗證符合性時，引擎調整/修改需記錄。": "Where the Engine Parameter Check method is used, engine adjustments/modifications must be recorded.",
    "船長、船員或部員證書需依 STCW/STCW-F 要求簽發，並於任職船上保有正本可供查驗。": "Certificates for masters, officers, or ratings must be issued under STCW/STCW-F and originals kept onboard for inspection.",
    "船員每日休息時間紀錄需留船。": "Daily hours-of-rest records must be kept onboard.",
    "400 GT and above 國際航行船舶，排除固定/浮動平台、FSU、FPSO。": "International ships of 400 GT and above, excluding fixed/floating platforms, FSUs, and FPSOs.",
    "24 m or more 但 less than 400 GT 國際航行船舶，需 owner/agent 簽署聲明與支持文件。": "International ships of 24 m or more but less than 400 GT need an owner/agent declaration and supporting documents.",
    "400 GT and above 且適用 BWM 2004 的船舶，排除浮動平台、FSU、FPSO。": "Ships of 400 GT and above subject to BWM 2004, excluding floating platforms, FSUs, and FPSOs.",
    "每艘船需有經主管機關核准之 BWM plan，並於船上實施。": "Every ship must have an Administration-approved BWM plan and implement it onboard.",
    "每艘船需有 BWRB，可為電子系統或整合於其他紀錄；船上保存至少 2 年，公司保存至少 3 年。": "Every ship must have a BWRB, which may be electronic or integrated; kept onboard for at least 2 years and by the company for at least 3 years.",
    "裝有 BWMS 的船舶需攜帶型式認可證書副本供船上查驗。": "Ships fitted with a BWMS must carry a copy of the type-approval certificate for onboard inspection.",
    "GT greater than 1,000 的船舶，需依 Bunkers 2001 証明保險或財務擔保。": "Ships of GT greater than 1,000 must demonstrate insurance or financial security under Bunkers 2001.",
    "300 GT and above 船舶需依 Nairobi WRC 2007 簽發 wreck removal 保險/財務擔保證書。": "Ships of 300 GT and above need a wreck-removal insurance/financial security certificate under Nairobi WRC 2007.",
    "客船符合 SOLAS II-1、II-2、III、IV、V 及相關要求後簽發，Form P 永久附於證書。": "Issued to passenger ships complying with SOLAS II-1, II-2, III, IV, V and related requirements; Form P is permanently attached.",
    "所有客船需於 navigation bridge 提供緊急管理 decision support system。": "All passenger ships must provide an emergency-management decision support system on the navigation bridge.",
    "適用 SOLAS chapter I 的客船需有與適當 SAR service 合作之應急計畫。": "Passenger ships subject to SOLAS chapter I need a cooperation plan with the appropriate SAR service.",
    "適用 SOLAS chapter I 的客船需列出所有操作限制、豁免、區域/天氣/海況/載重/吃水/航速等限制。": "Passenger ships subject to SOLAS chapter I must list all operational limitations, exemptions, and restrictions on area, weather, sea state, load, draft, speed, etc.",
    "依 Special Trade Passenger Ships Agreement 1971 與 1973 Protocol 規定簽發。": "Issued under the Special Trade Passenger Ships Agreement 1971 and 1973 Protocol.",
    "Licensed to carry more than 12 passengers 的船舶，需依 PAL 1974/2002 Protocol 證明責任保險或財務擔保。": "Ships licensed to carry more than 12 passengers must demonstrate liability insurance or financial security under PAL 1974/2002 Protocol.",
    "500 GT and over 貨船，經 survey 符合 SOLAS I/10 與 II-1/II-2 相關結構要求後簽發。": "Cargo ships of 500 GT and over, issued after survey confirming structural compliance with SOLAS I/10 and II-1/II-2.",
    "500 GT and over 貨船，符合 SOLAS II-1、II-2、III、V 等設備要求；Form E 永久附於證書。": "Cargo ships of 500 GT and over complying with SOLAS II-1, II-2, III, V equipment requirements; Form E permanently attached.",
    "300 GT and over 且配有 radio installation 的貨船；Form R 永久附於證書。": "Cargo ships of 300 GT and over fitted with a radio installation; Form R permanently attached.",
    "可作為 Construction、Equipment、Radio certificates 的替代合併證書；Form C 永久附於證書。": "May replace separate Construction, Equipment, and Radio certificates; Form C permanently attached.",
    "2006-01-01 或以後建造之 500 GT and over oil tankers 與 20,000 GT and over bulk carriers。": "Oil tankers of 500 GT and over and bulk carriers of 20,000 GT and over built on or after 1 January 2006.",
    "Shipper 需在裝貨前以書面向船長/代表提供貨物資訊；散裝船需含貨物密度。": "The shipper must provide cargo information in writing to the master/representative before loading; bulk carriers need cargo density.",
    "裝卸固體散貨的船舶需提供 booklet 以避免船體結構過度應力；可併入 stability information。": "Ships loading/discharge solid bulk cargoes need a booklet to avoid excessive hull stresses; may be incorporated into stability information.",
    "依 Grain Code 裝載之船舶需有 authorization document，並隨附或併入 grain loading manual。": "Ships loading grain under the Grain Code need an authorization document and grain loading manual.",
    "Bulk carriers and oil tankers 需有 survey report file 與 supporting documents 符合 2011 ESP Code。": "Bulk carriers and oil tankers need a survey report file and supporting documents under the 2011 ESP Code.",
    "40,000 DWT and above、delivered on or before 1 June 1982，且 operating with dedicated clean ballast tanks 的 product carrier 需有操作手冊。": "Product carriers of 40,000 DWT and above delivered on or before 1 June 1982 and operating with dedicated clean ballast tanks need an operations manual.",
    "符合 CAS 要求並通過檢驗之油輪；CAS final report 與 review record 需留船。": "Oil tankers complying with CAS and passing survey; CAS final report and review record must be kept onboard.",
    "適用 MARPOL Annex I regulation 28 的油輪需提供核准型式之裝載/貨物分配與破損穩性資訊。": "Oil tankers subject to MARPOL Annex I regulation 28 must provide approved loading/cargo distribution and damage stability information.",
    "150 GT and above 油輪配有 ODMC 時，排放連續紀錄需至少保存 3 年。": "Oil tankers of 150 GT and above fitted with ODMC must retain continuous discharge records for at least 3 years.",
    "配有 ODMC 系統之油輪，需有主管機關核准操作手冊。": "Oil tankers fitted with an ODMC system need an Administration-approved operations manual.",
    "使用 crude oil washing systems 的油輪需有 Operations and Equipment Manual。": "Oil tankers using crude oil washing systems need an Operations and Equipment Manual.",
    "參與 oil tanker STS operations 的油輪需有主管機關核准 STS plan；STS 紀錄保存 3 年。": "Oil tankers involved in STS operations need an approved STS plan; STS records kept for 3 years.",
    "適用 MARPOL Annex VI regulation 15.1 的 crude oil tanker，需有並實施 VOC Management Plan。": "Crude oil tankers subject to MARPOL Annex VI regulation 15.1 need and must implement a VOC Management Plan.",
    "載運 2,000 tonnes 以上 bulk oil cargo 的船舶需有 CLC 1969 保險/財務擔保證書。": "Ships carrying more than 2,000 tonnes of bulk oil cargo need a CLC 1969 insurance/financial security certificate.",
    "載運 2,000 tonnes 以上 bulk oil cargo 的船舶需有 CLC 1992 保險/財務擔保證書。": "Ships carrying more than 2,000 tonnes of bulk oil cargo need a CLC 1992 insurance/financial security certificate.",
    "載運 NLS bulk 且航行至其他 MARPOL 締約方港口/終端的船舶；化學船 fitness certificate 可具同等效力。": "Ships carrying NLS in bulk and trading to other MARPOL party ports/terminals; a chemical-tanker fitness certificate may be equivalent.",
    "載運 NLS bulk 的船舶需有 Cargo Record Book，可為 official logbook 一部分或 approved electronic record book。": "Ships carrying NLS in bulk need a Cargo Record Book, which may be part of the official logbook or an approved electronic record book.",
    "認證可載運 NLS bulk 的船舶需有主管機關核准的 P&A Manual。": "Ships certified to carry NLS in bulk need an Administration-approved P&A Manual.",
    "150 GT and above 且認證可載運 NLS bulk 的船舶需有 approved SMPEP for NLS。": "Ships of 150 GT and above certified to carry NLS in bulk need an approved SMPEP for NLS.",
    "1986-07-01 前建造並適用 BCH Code 的化學船。": "Chemical tankers built before 1 July 1986 and subject to the BCH Code.",
    "1986-07-01 或以後建造並適用 IBC Code 的化學船。": "Chemical tankers built on or after 1 July 1986 and subject to the IBC Code.",
    "適用 Gas Carrier Code 的氣體船。": "Gas carriers subject to the Gas Carrier Code.",
    "1986-07-01 或以後建造並適用 IGC Code 的氣體船。": "Gas carriers built on or after 1 July 1986 and subject to the IGC Code.",
    "經核准的貨物操作手冊，包含 ESD system 與 PRV emergency isolating operations 程序。": "Approved cargo operations manuals, including procedures for ESD systems and PRV emergency isolating operations.",
    "符合 1994 HSC Code 或 2000 HSC Code 的 craft，完成 initial/renewal survey 後簽發。": "Craft complying with the 1994 or 2000 HSC Code, issued after initial/renewal survey.",
    "符合 HSC Code 1.2.2 至 1.2.7 操作要求的高速船。": "High-speed craft meeting HSC Code 1.2.2 to 1.2.7 operational requirements.",
    "載運 dangerous goods 的船舶需有文件證明結構與設備符合 SOLAS II-2/19；except solid dangerous goods in bulk, certification is not required for class 6.2, class 7 and dangerous goods in limited quantities。": "Ships carrying dangerous goods need documentary evidence of compliance with SOLAS II-2/19; except solid dangerous goods in bulk, certification is not required for class 6.2, class 7, and dangerous goods in limited quantities.",
    "包裝危險品運輸資訊與 container/vehicle packing certificate 需符合 IMDG Code，供港口主管機關指定人員/組織取得。": "Transport information and container/vehicle packing certificates for packaged dangerous goods must follow the IMDG Code and be available to designated port officials/organisations.",
    "包裝危險品或固體散裝危險品需有特殊清單/manifest 或 stowage plan，列明類別與位置。": "Packaged dangerous goods or solid dangerous goods in bulk require a special list/manifest or stowage plan showing class and location.",
    "載運 INF cargo 的船舶需符合 INF Code 並取得 fitness certificate。": "Ships carrying INF cargo must comply with the INF Code and hold a fitness certificate.",
    "核動力裝置需完整操作手冊，經主管機關核准並留船且持續更新。": "A complete operating manual for the nuclear power plant must be approved, kept onboard, and kept up to date.",
    "核動力船需依 SOLAS Chapter VIII 簽發取代貨船/客船 safety certificate 的核動力船證書。": "Nuclear ships need the nuclear cargo/passenger safety certificate issued under SOLAS Chapter VIII in place of conventional safety certificates.",
    "適用 Polar Code 的每艘船需有有效 Polar Ship Certificate，含設備補充紀錄。": "Every ship subject to the Polar Code needs a valid Polar Ship Certificate, including equipment supplement records.",
    "適用 Polar Code 的每艘船需有 PWOM。": "Every ship subject to the Polar Code needs a PWOM.",
    "使用 gases 或其他 low-flashpoint fuels 的船舶，需有 gas-related installations 維護資料、緊急程序、操作程序與 fuel handling manual。": "Ships using gases or other low-flashpoint fuels need maintenance data, emergency procedures, operational procedures, and a fuel-handling manual for gas-related installations.",
    "Special purpose ships 可依 1983/2008 SPS Code 簽發；效期通常依 SOLAS cargo ship 證書規定。": "Special purpose ships may be certificated under the 1983/2008 SPS Code; validity usually follows SOLAS cargo-ship certificate rules.",
    "Offshore supply vessels 符合 2006 Guidelines 時可簽發 Document of Compliance。": "Offshore supply vessels complying with the 2006 Guidelines may be issued a Document of Compliance.",
    "適用 OSV Chemical Code 的 offshore support vessel，經初次檢驗後簽發並適當背書。": "Offshore support vessels subject to the OSV Chemical Code, issued after initial survey and properly endorsed.",
    "符合 Code of Safety for Diving Systems 的 diving system，由主管機關或授權機構檢驗後簽發。": "Diving systems complying with the Code of Safety for Diving Systems, issued after survey by the Administration or authorised body.",
    "適用於載客 underwater excursions、乘客艙壓力接近一大氣壓之 submersible craft；附 Design and Construction Document。": "For passenger submersible craft on underwater excursions with passenger compartments near one atmosphere; includes Design and Construction Document.",
    "依 DSC Code 檢驗後簽發。": "Issued after survey under the DSC Code.",
    "依 1979/1989/2009 MODU Code 檢驗後簽發。": "Issued after survey under the 1979/1989/2009 MODU Code.",
    "符合 Guidelines for WIG craft 的 craft，完成 initial/renewal survey 後簽發。": "Craft complying with the Guidelines for WIG craft, issued after initial/renewal survey.",
    "Administration 簽發以證明符合 wing-in-ground craft guidelines。": "Issued by the Administration to demonstrate compliance with wing-in-ground craft guidelines.",
    "適用於 SOLAS II-1/3-12 不適用的 existing ships，應依 Code on Noise Levels on Board Ships 製作。": "For existing ships to which SOLAS II-1/3-12 does not apply, prepared under the Code on Noise Levels on Board Ships.",
}

for zh, en in trigger_map.items():
    text = text.replace(f"trigger:'{zh}'", f"trigger:'{en}'")

EN.write_text(text, encoding="utf-8")
print("Wrote", EN)
