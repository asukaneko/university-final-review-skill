#!/usr/bin/env python3
"""Generate a standalone HTML test-card review interface from CSV.

The expected CSV columns are flexible. Recommended columns:
    ID,Front,Back,Chapter,Topic,Difficulty,CardType,Tags

Aliases are supported for common Chinese and lowercase headers:
    正面 -> Front, 背面 -> Back, 章节 -> Chapter, 主题 -> Topic,
    难度 -> Difficulty, 卡片类型 -> CardType, 标签 -> Tags

Usage:
    python scripts/generate_test_cards_html.py \
        --input examples/test_cards.sample.csv \
        --output output/test_cards.html \
        --title "Operating Systems Test Cards"

The output is a self-contained HTML file with CSS and JavaScript embedded.
It works offline and stores study progress in browser localStorage.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

HEADER_ALIASES = {
    "id": "ID",
    "编号": "ID",
    "front": "Front",
    "question": "Front",
    "prompt": "Front",
    "正面": "Front",
    "题干": "Front",
    "问题": "Front",
    "back": "Back",
    "answer": "Back",
    "背面": "Back",
    "答案": "Back",
    "解析": "Back",
    "chapter": "Chapter",
    "章节": "Chapter",
    "topic": "Topic",
    "主题": "Topic",
    "知识点": "Topic",
    "difficulty": "Difficulty",
    "难度": "Difficulty",
    "cardtype": "CardType",
    "card_type": "CardType",
    "type": "CardType",
    "卡片类型": "CardType",
    "类型": "CardType",
    "tags": "Tags",
    "标签": "Tags",
}

DEFAULT_FIELDS = ["ID", "Front", "Back", "Chapter", "Topic", "Difficulty", "CardType", "Tags"]


def normalize_header(header: str) -> str:
    compact = header.strip().replace(" ", "").replace("-", "_")
    return HEADER_ALIASES.get(compact.lower(), HEADER_ALIASES.get(compact, header.strip()))


def read_cards(csv_path: Path) -> list[dict[str, str]]:
    with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise ValueError("CSV has no header row.")
        normalized = [normalize_header(name) for name in reader.fieldnames]
        cards: list[dict[str, str]] = []
        for index, row in enumerate(reader, 1):
            card: dict[str, str] = {field: "" for field in DEFAULT_FIELDS}
            for old_name, new_name in zip(reader.fieldnames, normalized):
                value = row.get(old_name, "")
                card[new_name] = str(value).strip() if value is not None else ""
            if not card["ID"]:
                card["ID"] = f"CARD-{index:03d}"
            if not card["Front"] and not card["Back"]:
                continue
            cards.append(card)
    if not cards:
        raise ValueError("CSV contains no usable cards. At least Front or Back is required.")
    return cards


def unique_values(cards: list[dict[str, str]], key: str) -> list[str]:
    values = {card.get(key, "").strip() for card in cards if card.get(key, "").strip()}
    return sorted(values, key=lambda item: item.lower())


def build_html(cards: list[dict[str, str]], title: str, language: str) -> str:
    payload = json.dumps(cards, ensure_ascii=False)
    chapters = json.dumps(unique_values(cards, "Chapter"), ensure_ascii=False)
    difficulties = json.dumps(unique_values(cards, "Difficulty"), ensure_ascii=False)
    types = json.dumps(unique_values(cards, "CardType"), ensure_ascii=False)
    page_title = html.escape(title)
    lang = "zh-CN" if language == "zh-CN" else "en"
    labels = {
        "zh-CN": {
            "subtitle": "主动回忆 · 翻卡复习 · 错题强化",
            "search": "搜索题干、答案、主题或标签",
            "chapter": "章节",
            "difficulty": "难度",
            "type": "类型",
            "all": "全部",
            "showAnswer": "显示答案",
            "hideAnswer": "隐藏答案",
            "again": "不会",
            "hard": "困难",
            "good": "掌握",
            "easy": "熟练",
            "shuffle": "随机排序",
            "reset": "重置筛选",
            "wrongOnly": "只看错题/困难",
            "export": "导出学习记录",
            "progress": "学习进度",
            "cards": "卡片",
            "reviewed": "已复习",
            "accuracy": "掌握率",
            "empty": "没有符合筛选条件的卡片。",
            "front": "正面",
            "back": "背面",
            "shortcuts": "快捷键：空格翻卡，1 不会，2 困难，3 掌握，4 熟练，←/→ 切换。",
        },
        "en": {
            "subtitle": "Active recall · Flip-card review · Weak-point repair",
            "search": "Search front, back, topic, or tags",
            "chapter": "Chapter",
            "difficulty": "Difficulty",
            "type": "Type",
            "all": "All",
            "showAnswer": "Show answer",
            "hideAnswer": "Hide answer",
            "again": "Again",
            "hard": "Hard",
            "good": "Good",
            "easy": "Easy",
            "shuffle": "Shuffle",
            "reset": "Reset filters",
            "wrongOnly": "Weak cards only",
            "export": "Export progress",
            "progress": "Progress",
            "cards": "Cards",
            "reviewed": "Reviewed",
            "accuracy": "Mastery",
            "empty": "No cards match the current filters.",
            "front": "Front",
            "back": "Back",
            "shortcuts": "Shortcuts: Space flips, 1 Again, 2 Hard, 3 Good, 4 Easy, ←/→ navigate.",
        },
    }[lang]
    L = json.dumps(labels, ensure_ascii=False)
    return f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{page_title}</title>
  <style>
    :root {{
      --bg: #eef4fb;
      --bg2: #f8fbff;
      --panel: rgba(255, 255, 255, 0.86);
      --text: #142033;
      --muted: #637083;
      --primary: #2563eb;
      --primary2: #0f766e;
      --accent: #f59e0b;
      --danger: #dc2626;
      --border: rgba(37, 99, 235, 0.14);
      --shadow: 0 22px 60px rgba(15, 23, 42, 0.12);
      --radius: 22px;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", "Microsoft YaHei", sans-serif;
      color: var(--text);
      background:
        radial-gradient(circle at 8% 5%, rgba(37, 99, 235, .20), transparent 30%),
        radial-gradient(circle at 90% 10%, rgba(15, 118, 110, .16), transparent 28%),
        linear-gradient(135deg, var(--bg), var(--bg2));
      min-height: 100vh;
    }}
    .app {{ max-width: 1180px; margin: 0 auto; padding: 28px 18px 44px; }}
    header {{
      display: grid; grid-template-columns: 1.4fr .9fr; gap: 18px; align-items: stretch; margin-bottom: 18px;
    }}
    .hero, .stats, .toolbar, .card-panel, .list-panel {{
      background: var(--panel); border: 1px solid var(--border); border-radius: var(--radius);
      box-shadow: var(--shadow); backdrop-filter: blur(18px);
    }}
    .hero {{ padding: 26px; position: relative; overflow: hidden; }}
    .hero:after {{ content:""; position:absolute; right:-60px; top:-70px; width:190px; height:190px; border-radius:50%; background:rgba(37,99,235,.11); }}
    h1 {{ margin: 0 0 8px; font-size: clamp(28px, 4vw, 46px); line-height: 1.03; letter-spacing: -0.04em; }}
    .subtitle {{ color: var(--muted); font-size: 16px; }}
    .stats {{ padding: 18px; display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; }}
    .stat {{ background: #fff; border: 1px solid var(--border); border-radius: 18px; padding: 14px; }}
    .stat .num {{ font-size: 26px; font-weight: 800; color: var(--primary); }}
    .stat .label {{ color: var(--muted); font-size: 13px; margin-top: 2px; }}
    .toolbar {{ padding: 16px; display: grid; grid-template-columns: 1.8fr repeat(3, 1fr); gap: 10px; margin-bottom: 18px; }}
    input, select, button {{ font: inherit; }}
    input, select {{
      width: 100%; border: 1px solid rgba(99,112,131,.24); border-radius: 14px; padding: 12px 13px;
      background: rgba(255,255,255,.92); color: var(--text); outline: none;
    }}
    input:focus, select:focus {{ border-color: var(--primary); box-shadow: 0 0 0 3px rgba(37,99,235,.12); }}
    .actions {{ display: flex; gap: 10px; flex-wrap: wrap; margin: -4px 0 18px; }}
    button {{
      border: 0; border-radius: 999px; padding: 11px 15px; cursor: pointer; color: white; background: var(--primary);
      box-shadow: 0 10px 20px rgba(37,99,235,.16); font-weight: 700;
    }}
    button.secondary {{ background: #334155; }}
    button.ghost {{ background: #fff; color: var(--text); border: 1px solid var(--border); box-shadow: none; }}
    button.warn {{ background: var(--accent); }}
    button.danger {{ background: var(--danger); }}
    button.good {{ background: var(--primary2); }}
    main {{ display: grid; grid-template-columns: minmax(0, 1fr) 340px; gap: 18px; align-items: start; }}
    .card-panel {{ padding: 22px; min-height: 500px; }}
    .meta {{ display:flex; gap: 8px; flex-wrap: wrap; margin-bottom: 16px; }}
    .pill {{ border-radius: 999px; background: rgba(37,99,235,.10); color: #1d4ed8; padding: 7px 10px; font-size: 12px; font-weight: 800; }}
    .pill.green {{ background: rgba(15,118,110,.10); color: #0f766e; }}
    .pill.orange {{ background: rgba(245,158,11,.13); color: #b45309; }}
    .flip-card {{ min-height: 330px; perspective: 1400px; margin-bottom: 16px; cursor: pointer; }}
    .flip-inner {{ position: relative; min-height: 330px; transform-style: flat; }}
    .flip-card:hover .face {{ box-shadow: 0 18px 34px rgba(37,99,235,.14); }}
    .face {{
      position: absolute; inset: 0; border-radius: 24px; padding: 30px; background: linear-gradient(180deg, #fff, #f8fbff);
      border: 1px solid rgba(37,99,235,.16); display:flex; flex-direction: column; justify-content: center; align-items: center;
      text-align: center; overflow: auto; transform-origin: center center; will-change: transform, opacity; transition:
        opacity .34s ease,
        transform .46s cubic-bezier(.18,.72,.24,1),
        box-shadow .25s ease;
    }}
    .face.front {{ opacity: 1; transform: rotateY(0deg) scale(1); z-index: 2; box-shadow: inset 0 1px 0 rgba(255,255,255,.9); }}
    .face.back {{ opacity: 0; transform: rotateY(-88deg) scale(.96); z-index: 1; pointer-events: none; background: linear-gradient(180deg, #f7fffc, #fff); }}
    .flip-card.revealed .face.front {{ opacity: 0; transform: rotateY(88deg) scale(.96); z-index: 1; pointer-events: none; }}
    .flip-card.revealed .face.back {{ opacity: 1; transform: rotateY(0deg) scale(1); z-index: 2; pointer-events: auto; }}
    .face-label {{ color: var(--muted); font-size: 13px; font-weight: 800; text-transform: uppercase; letter-spacing: .08em; margin-bottom: 14px; }}
    .content {{ max-width: 760px; margin: 0 auto; font-size: clamp(18px, 2.2vw, 26px); line-height: 1.6; white-space: pre-wrap; text-wrap: pretty; }}
    @media (prefers-reduced-motion: reduce) {{
      .face {{ transition: opacity .12s linear; transform: none !important; }}
      .face.back {{ opacity: 0; }}
      .flip-card.revealed .face.front {{ opacity: 0; }}
      .flip-card.revealed .face.back {{ opacity: 1; }}
    }}
    .review-buttons {{ display:grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin: 14px 0; }}
    .nav {{ display:flex; justify-content: space-between; gap: 10px; margin-top: 14px; }}
    .progressbar {{ height: 10px; background: rgba(99,112,131,.18); border-radius: 999px; overflow:hidden; margin-top: 12px; }}
    .progressbar span {{ display:block; height:100%; width:0%; background: linear-gradient(90deg, var(--primary), var(--primary2)); transition: width .25s; }}
    .list-panel {{ padding: 14px; max-height: 700px; overflow: auto; }}
    .list-title {{ font-weight: 900; margin: 4px 4px 12px; }}
    .item {{ border: 1px solid rgba(99,112,131,.16); background: #fff; border-radius: 16px; padding: 12px; margin-bottom: 10px; cursor:pointer; }}
    .item.active {{ border-color: var(--primary); box-shadow: 0 0 0 3px rgba(37,99,235,.10); }}
    .item .front {{ font-weight: 750; line-height: 1.35; }}
    .item .small {{ color: var(--muted); font-size: 12px; margin-top: 6px; }}
    .empty {{ padding: 60px 18px; text-align:center; color: var(--muted); }}
    .shortcuts {{ color: var(--muted); font-size: 13px; margin-top: 12px; }}
    @media (max-width: 900px) {{
      header, main, .toolbar {{ grid-template-columns: 1fr; }}
      .stats {{ grid-template-columns: repeat(2, 1fr); }}
      .review-buttons {{ grid-template-columns: repeat(2, 1fr); }}
    }}
    @media print {{ .toolbar, .actions, .list-panel, .review-buttons, .nav, .shortcuts {{ display:none; }} body {{ background:white; }} .app {{ max-width:none; }} .card-panel, .hero, .stats {{ box-shadow:none; }} }}
  </style>
</head>
<body>
  <div class="app">
    <header>
      <section class="hero">
        <h1>{page_title}</h1>
        <div class="subtitle" id="subtitle"></div>
        <div class="shortcuts" id="shortcuts"></div>
      </section>
      <section class="stats">
        <div class="stat"><div class="num" id="totalCards">0</div><div class="label" id="cardsLabel"></div></div>
        <div class="stat"><div class="num" id="reviewedCards">0</div><div class="label" id="reviewedLabel"></div></div>
        <div class="stat"><div class="num" id="masteryRate">0%</div><div class="label" id="accuracyLabel"></div></div>
        <div class="stat"><div class="num" id="position">0/0</div><div class="label" id="progressLabel"></div></div>
      </section>
    </header>

    <section class="toolbar">
      <input id="search" type="search" autocomplete="off">
      <select id="chapter"></select>
      <select id="difficulty"></select>
      <select id="cardType"></select>
    </section>

    <section class="actions">
      <button class="ghost" id="shuffleBtn"></button>
      <button class="ghost" id="wrongOnlyBtn"></button>
      <button class="ghost" id="resetBtn"></button>
      <button class="secondary" id="exportBtn"></button>
    </section>

    <main>
      <section class="card-panel" id="cardPanel"></section>
      <aside class="list-panel"><div class="list-title" id="listTitle"></div><div id="cardList"></div></aside>
    </main>
  </div>

<script>
const CARDS = {payload};
const CHAPTERS = {chapters};
const DIFFICULTIES = {difficulties};
const TYPES = {types};
const L = {L};
const STORAGE_KEY = 'test-card-progress:' + location.pathname + ':' + {json.dumps(title, ensure_ascii=False)};
let progress = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{{}}');
let filtered = [...CARDS];
let index = 0;
let revealed = false;
let weakOnly = false;

function $(id) {{ return document.getElementById(id); }}
function esc(s) {{ return String(s || '').replace(/[&<>"']/g, m => ({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[m])); }}
function optionList(values, label) {{ return '<option value="">' + esc(L.all + ' · ' + label) + '</option>' + values.map(v => '<option value="' + esc(v) + '">' + esc(v) + '</option>').join(''); }}
function save() {{ localStorage.setItem(STORAGE_KEY, JSON.stringify(progress)); }}
function scoreOf(id) {{ return progress[id]?.score || 0; }}
function isWeak(card) {{ return progress[card.ID] && progress[card.ID].score <= 2; }}
function textOf(card) {{ return [card.ID, card.Front, card.Back, card.Chapter, card.Topic, card.Difficulty, card.CardType, card.Tags].join(' ').toLowerCase(); }}

function initLabels() {{
  $('subtitle').textContent = L.subtitle;
  $('shortcuts').textContent = L.shortcuts;
  $('search').placeholder = L.search;
  $('chapter').innerHTML = optionList(CHAPTERS, L.chapter);
  $('difficulty').innerHTML = optionList(DIFFICULTIES, L.difficulty);
  $('cardType').innerHTML = optionList(TYPES, L.type);
  $('shuffleBtn').textContent = L.shuffle;
  $('wrongOnlyBtn').textContent = L.wrongOnly;
  $('resetBtn').textContent = L.reset;
  $('exportBtn').textContent = L.export;
  $('cardsLabel').textContent = L.cards;
  $('reviewedLabel').textContent = L.reviewed;
  $('accuracyLabel').textContent = L.accuracy;
  $('progressLabel').textContent = L.progress;
  $('listTitle').textContent = L.cards;
}}

function applyFilters() {{
  const q = $('search').value.trim().toLowerCase();
  const ch = $('chapter').value;
  const diff = $('difficulty').value;
  const typ = $('cardType').value;
  filtered = CARDS.filter(card =>
    (!q || textOf(card).includes(q)) &&
    (!ch || card.Chapter === ch) &&
    (!diff || card.Difficulty === diff) &&
    (!typ || card.CardType === typ) &&
    (!weakOnly || isWeak(card))
  );
  index = Math.min(index, Math.max(filtered.length - 1, 0));
  revealed = false;
  render();
}}

function renderStats() {{
  const reviewed = Object.keys(progress).filter(id => progress[id].reviews > 0).length;
  const mastered = Object.keys(progress).filter(id => progress[id].score >= 3).length;
  $('totalCards').textContent = filtered.length;
  $('reviewedCards').textContent = reviewed;
  $('masteryRate').textContent = reviewed ? Math.round(mastered / reviewed * 100) + '%' : '0%';
  $('position').textContent = filtered.length ? (index + 1) + '/' + filtered.length : '0/0';
}}

function setRevealed(value) {{
  revealed = value;
  const flipCard = $('flipCard');
  const flipBtn = $('flipBtn');
  if (flipCard) flipCard.classList.toggle('revealed', revealed);
  if (flipBtn) flipBtn.textContent = revealed ? L.hideAnswer : L.showAnswer;
}}

function updateCurrentProgressMeta() {{
  const card = filtered[index];
  const p = card ? (progress[card.ID] || {{reviews:0, score:0}}) : {{reviews:0, score:0}};
  const reviewMeta = $('reviewMeta');
  if (reviewMeta) reviewMeta.textContent = 'reviews: ' + (p.reviews || 0);
  renderStats();
  renderList();
}}

function render() {{
  renderStats();
  const panel = $('cardPanel');
  if (!filtered.length) {{
    panel.innerHTML = '<div class="empty">' + esc(L.empty) + '</div>';
    $('cardList').innerHTML = '';
    return;
  }}
  const card = filtered[index];
  const p = progress[card.ID] || {{reviews:0, score:0}};
  panel.innerHTML = `
    <div class="meta">
      <span class="pill">${{esc(card.ID)}}</span>
      <span class="pill green">${{esc(card.Chapter || '—')}}</span>
      <span class="pill orange">${{esc(card.Difficulty || '—')}}</span>
      <span class="pill">${{esc(card.CardType || '—')}}</span>
    </div>
    <div class="flip-card ${{revealed ? 'revealed' : ''}}" id="flipCard">
      <div class="flip-inner">
        <div class="face front"><div class="face-label">${{esc(L.front)}}</div><div class="content">${{esc(card.Front)}}</div></div>
        <div class="face back"><div class="face-label">${{esc(L.back)}}</div><div class="content">${{esc(card.Back)}}</div></div>
      </div>
    </div>
    <button id="flipBtn">${{revealed ? esc(L.hideAnswer) : esc(L.showAnswer)}}</button>
    <div class="review-buttons">
      <button class="danger" data-score="1">1 · ${{esc(L.again)}}</button>
      <button class="warn" data-score="2">2 · ${{esc(L.hard)}}</button>
      <button class="good" data-score="3">3 · ${{esc(L.good)}}</button>
      <button data-score="4">4 · ${{esc(L.easy)}}</button>
    </div>
    <div class="meta"><span class="pill">${{esc(card.Topic || '')}}</span><span class="pill">${{esc(card.Tags || '')}}</span><span class="pill" id="reviewMeta">reviews: ${{p.reviews || 0}}</span></div>
    <div class="progressbar"><span style="width:${{Math.round((index + 1) / filtered.length * 100)}}%"></span></div>
    <div class="nav"><button class="ghost" id="prevBtn">←</button><button class="ghost" id="nextBtn">→</button></div>
  `;
  $('flipBtn').onclick = () => setRevealed(!revealed);
  $('flipCard').onclick = () => setRevealed(!revealed);
  $('prevBtn').onclick = () => move(-1);
  $('nextBtn').onclick = () => move(1);
  document.querySelectorAll('[data-score]').forEach(btn => btn.onclick = () => grade(Number(btn.dataset.score)));
  renderList();
}}

function renderList() {{
  $('cardList').innerHTML = filtered.map((card, i) => `
    <div class="item ${{i === index ? 'active' : ''}}" data-i="${{i}}">
      <div class="front">${{esc(card.Front).slice(0, 120)}}${{card.Front.length > 120 ? '…' : ''}}</div>
      <div class="small">${{esc(card.Chapter || '—')}} · ${{esc(card.Topic || '—')}} · score ${{scoreOf(card.ID)}}</div>
    </div>
  `).join('');
  document.querySelectorAll('.item').forEach(el => el.onclick = () => {{ index = Number(el.dataset.i); revealed = false; render(); }});
}}

function move(delta) {{
  if (!filtered.length) return;
  index = (index + delta + filtered.length) % filtered.length;
  revealed = false;
  render();
}}

function grade(score) {{
  const card = filtered[index];
  progress[card.ID] = {{reviews: (progress[card.ID]?.reviews || 0) + 1, score, lastReviewed: new Date().toISOString()}};
  save();
  if (score === 1) {{
    setRevealed(true);
    updateCurrentProgressMeta();
    return;
  }}
  move(1);
}}

function shuffle() {{
  for (let i = filtered.length - 1; i > 0; i--) {{
    const j = Math.floor(Math.random() * (i + 1));
    [filtered[i], filtered[j]] = [filtered[j], filtered[i]];
  }}
  index = 0; revealed = false; render();
}}

function resetFilters() {{
  $('search').value = ''; $('chapter').value = ''; $('difficulty').value = ''; $('cardType').value = ''; weakOnly = false; applyFilters();
}}

function exportProgress() {{
  const rows = [['ID','Reviews','Score','LastReviewed']];
  CARDS.forEach(c => {{ const p = progress[c.ID] || {{}}; rows.push([c.ID, p.reviews || 0, p.score || 0, p.lastReviewed || '']); }});
  const csv = rows.map(r => r.map(v => '"' + String(v).replaceAll('"','""') + '"').join(',')).join('\\n');
  const blob = new Blob([csv], {{type:'text/csv;charset=utf-8'}});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob); a.download = 'test-card-progress.csv'; a.click(); URL.revokeObjectURL(a.href);
}}

['search','chapter','difficulty','cardType'].forEach(id => $(id).addEventListener('input', applyFilters));
$('shuffleBtn').onclick = shuffle;
$('wrongOnlyBtn').onclick = () => {{ weakOnly = !weakOnly; applyFilters(); }};
$('resetBtn').onclick = resetFilters;
$('exportBtn').onclick = exportProgress;
document.addEventListener('keydown', e => {{
  if (['INPUT','SELECT'].includes(document.activeElement.tagName)) return;
  if (e.code === 'Space') {{ e.preventDefault(); setRevealed(!revealed); }}
  if (e.key === 'ArrowLeft') move(-1);
  if (e.key === 'ArrowRight') move(1);
  if (['1','2','3','4'].includes(e.key)) grade(Number(e.key));
}});
initLabels();
applyFilters();
</script>
</body>
</html>
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a standalone HTML test-card interface from CSV.")
    parser.add_argument("--input", "-i", required=True, type=Path, help="Input CSV file.")
    parser.add_argument("--output", "-o", required=True, type=Path, help="Output HTML file.")
    parser.add_argument("--title", default="Test Cards Review", help="Page title.")
    parser.add_argument("--language", choices=["en", "zh-CN"], default="en", help="Interface language.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cards = read_cards(args.input)
    html_text = build_html(cards, args.title, args.language)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(html_text, encoding="utf-8")
    print(f"Generated {args.output} with {len(cards)} cards")


if __name__ == "__main__":
    main()
