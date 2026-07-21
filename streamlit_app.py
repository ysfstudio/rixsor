<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Rixsor — لوحة التحكم الذكية</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=JetBrains+Mono:wght@500;600&family=Tajawal:wght@400;500;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>

<!-- ===== HERO ===== -->
<header class="hero">
  <div class="sticker-field" aria-hidden="true">
    <svg class="sticker s-check" style="--x:8%; --y:22%; --delay:0s" viewBox="0 0 48 48"><circle cx="24" cy="24" r="21" fill="#17B8A6"/><path d="M14 25l7 7 13-15" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>
    <svg class="sticker s-bulb" style="--x:86%; --y:18%; --delay:.6s" viewBox="0 0 48 48"><path d="M24 6c-8 0-13 6-13 13 0 5 3 8 5 11 1 2 2 4 2 6h12c0-2 1-4 2-6 2-3 5-6 5-11 0-7-5-13-13-13z" fill="#FFC857"/><rect x="19" y="36" width="10" height="5" rx="2" fill="#8a6d1f"/></svg>
    <svg class="sticker s-gear" style="--x:12%; --y:74%; --delay:1.1s" viewBox="0 0 48 48"><path fill="#7C5CFF" d="M24 4l3 6 6-3 1 7 7 1-3 6 3 6-7 1-1 7-6-3-3 6-3-6-6 3-1-7-7-1 3-6-3-6 7-1 1-7 6 3z"/><circle cx="24" cy="24" r="8" fill="#fff"/></svg>
    <svg class="sticker s-spark" style="--x:90%; --y:70%; --delay:.3s" viewBox="0 0 48 48"><path d="M24 4l4 16 16 4-16 4-4 16-4-16-16-4 16-4z" fill="#FF6B6B"/></svg>
    <svg class="sticker s-note" style="--x:50%; --y:8%; --delay:.9s" viewBox="0 0 48 48"><rect x="8" y="6" width="32" height="36" rx="4" fill="#fff" stroke="#7C5CFF" stroke-width="3"/><line x1="14" y1="16" x2="34" y2="16" stroke="#7C5CFF" stroke-width="3" stroke-linecap="round"/><line x1="14" y1="24" x2="34" y2="24" stroke="#17B8A6" stroke-width="3" stroke-linecap="round"/><line x1="14" y1="32" x2="26" y2="32" stroke="#FF6B6B" stroke-width="3" stroke-linecap="round"/></svg>
    <svg class="sticker s-rocket" style="--x:50%; --y:90%; --delay:1.4s" viewBox="0 0 48 48"><path d="M24 4c6 4 9 12 9 20 0 4-2 8-4 10l-1-8-4-3-4 3-1 8c-2-2-4-6-4-10 0-8 3-16 9-20z" fill="#FF6B6B"/><circle cx="24" cy="20" r="3.5" fill="#fff"/><path d="M17 30l-5 8 8-3" fill="#7C5CFF"/><path d="M31 30l5 8-8-3" fill="#7C5CFF"/></svg>
  </div>

  <p class="eyebrow">لوحتك الشخصية للتنظيم والإبداع</p>
  <h1 class="wordmark">Rixsor</h1>
  <p class="tagline">مساحة صغيرة ومرتّبة… ليومك، أفكارك، وتركيزك.</p>
</header>

<!-- ===== MAIN GRID ===== -->
<main class="grid">

  <!-- To-Do -->
  <section class="card card-todo" aria-labelledby="todo-title">
    <div class="card-head">
      <span class="card-icon">✅</span>
      <h2 id="todo-title">المهام اليومية</h2>
      <span class="counter-pill" id="todoCount">0</span>
    </div>
    <form id="todoForm" class="todo-form">
      <input type="text" id="todoInput" placeholder="أضف مهمة جديدة… واضغط Enter" autocomplete="off" maxlength="120">
      <button type="submit" aria-label="إضافة المهمة">+</button>
    </form>
    <ul id="todoList" class="todo-list"></ul>
    <p class="empty-hint" id="todoEmpty">لا توجد مهام بعد — أضف أول مهمة لك ✨</p>
  </section>

  <!-- Quick Notes -->
  <section class="card card-notes" aria-labelledby="notes-title">
    <div class="card-head">
      <span class="card-icon">📝</span>
      <h2 id="notes-title">ملاحظات سريعة</h2>
      <span class="save-state" id="noteSaveState">محفوظ</span>
    </div>
    <textarea id="notesArea" placeholder="اكتب أي فكرة تخطر ببالك… تُحفظ تلقائياً في متصفحك."></textarea>
  </section>

  <!-- Sidebar widgets -->
  <aside class="widgets">
    <section class="card card-clock" aria-label="الساعة">
      <span class="card-icon">🕒</span>
      <div id="clockTime" class="clock-time">--:--:--</div>
      <div id="clockDate" class="clock-date">—</div>
    </section>

    <section class="card card-quote" aria-label="عبارة تحفيزية">
      <span class="card-icon">💡</span>
      <p id="quoteText" class="quote-text">جاري التحميل…</p>
      <button id="quoteBtn" class="ghost-btn">عبارة أخرى</button>
    </section>

    <section class="card card-counter" aria-label="عداد التركيز">
      <span class="card-icon">🎯</span>
      <h3>عداد التركيز</h3>
      <div class="counter-value" id="counterValue">0</div>
      <div class="counter-controls">
        <button id="counterMinus" aria-label="إنقاص">−</button>
        <button id="counterReset" aria-label="تصفير">↺</button>
        <button id="counterPlus" aria-label="زيادة">+</button>
      </div>
    </section>
  </aside>
</main>

<footer class="footer">
  <p>Rixsor — كل شيء يُحفظ محلياً في متصفحك، بلا تسجيل دخول وبلا تعقيد.</p>
</footer>

<script src="{{ url_for('static', filename='script.js') }}"></script>
</body>
</html>
