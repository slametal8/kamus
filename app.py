<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kamus Modern 2025</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        :root {
            --primary: #6366f1;
            --secondary: #8b5cf6;
            --accent: #06d6a0;
            --dark: #1e293b;
            --light: #f8fafc;
            --gray: #64748b;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', system-ui, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: var(--dark);
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }

        .app-wrapper {
            display: grid;
            grid-template-columns: 280px 1fr 300px;
            gap: 24px;
            height: calc(100vh - 40px);
        }

        /* Sidebar Menu */
        .sidebar {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            border-radius: 24px;
            padding: 24px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
        }

        .logo {
            text-align: center;
            margin-bottom: 32px;
        }

        .logo h1 {
            font-size: 24px;
            font-weight: 700;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .menu-item {
            display: flex;
            align-items: center;
            padding: 16px;
            margin: 8px 0;
            border-radius: 16px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: 500;
        }

        .menu-item:hover {
            background: var(--primary);
            color: white;
            transform: translateX(8px);
        }

        .menu-item.active {
            background: var(--primary);
            color: white;
        }

        .menu-icon {
            margin-right: 12px;
            font-size: 18px;
        }

        /* Main Content */
        .main-content {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            border-radius: 24px;
            padding: 32px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            overflow-y: auto;
        }

        .search-section {
            margin-bottom: 32px;
        }

        .search-box {
            position: relative;
            max-width: 600px;
            margin: 0 auto;
        }

        .search-input {
            width: 100%;
            padding: 20px 60px 20px 24px;
            border: 2px solid #e2e8f0;
            border-radius: 16px;
            font-size: 18px;
            transition: all 0.3s ease;
            background: white;
        }

        .search-input:focus {
            outline: none;
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
        }

        .search-btn {
            position: absolute;
            right: 8px;
            top: 50%;
            transform: translateY(-50%);
            background: var(--primary);
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .search-btn:hover {
            background: var(--secondary);
            transform: translateY(-50%) scale(1.05);
        }

        .result-section {
            margin-top: 32px;
        }

        .word-card {
            background: white;
            padding: 24px;
            border-radius: 16px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            margin-bottom: 20px;
        }

        .word-header {
            display: flex;
            justify-content: between;
            align-items: center;
            margin-bottom: 16px;
        }

        .word-title {
            font-size: 32px;
            font-weight: 700;
            color: var(--dark);
        }

        .phonetic {
            color: var(--gray);
            font-style: italic;
            margin-left: 12px;
        }

        .meaning-section {
            margin: 20px 0;
        }

        .part-of-speech {
            font-weight: 600;
            color: var(--primary);
            margin-bottom: 12px;
            font-size: 18px;
        }

        .definition {
            margin: 8px 0;
            padding-left: 16px;
            border-left: 3px solid var(--accent);
        }

        /* Right Sidebar Links */
        .links-sidebar {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            border-radius: 24px;
            padding: 24px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
        }

        .links-title {
            font-size: 20px;
            font-weight: 600;
            margin-bottom: 24px;
            text-align: center;
            color: var(--dark);
        }

        .link-item {
            display: flex;
            align-items: center;
            padding: 16px;
            margin: 8px 0;
            background: white;
            border-radius: 12px;
            text-decoration: none;
            color: var(--dark);
            transition: all 0.3s ease;
            border: 1px solid #e2e8f0;
        }

        .link-item:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
            border-color: var(--primary);
        }

        .link-icon {
            margin-right: 12px;
            font-size: 20px;
        }

        /* Responsive Design */
        @media (max-width: 1024px) {
            .app-wrapper {
                grid-template-columns: 1fr;
                grid-template-rows: auto 1fr auto;
            }
            
            .sidebar, .links-sidebar {
                order: -1;
            }
        }

        /* Animations */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .fade-in {
            animation: fadeIn 0.5s ease;
        }

        /* Glass morphism effect */
        .glass {
            background: rgba(255, 255, 255, 0.25);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.18);
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="app-wrapper">
            <!-- Sidebar Menu -->
            <div class="sidebar">
                <div class="logo">
                    <h1>📚 KamusAI 2025</h1>
                </div>
                <div class="menu">
                    {% for item in menu_items %}
                    <div class="menu-item {% if loop.first %}active{% endif %}" data-tab="{{ item.id }}">
                        <span class="menu-icon">{{ item.icon }}</span>
                        {{ item.name }}
                    </div>
                    {% endfor %}
                </div>
            </div>

            <!-- Main Content -->
            <div class="main-content">
                <div class="search-section">
                    <div class="search-box">
                        <input type="text" class="search-input" placeholder="Ketik kata yang ingin dicari..." id="searchInput">
                        <button class="search-btn" onclick="searchWord()">
                            <i class="fas fa-search"></i> Cari
                        </button>
                    </div>
                </div>

                <div class="result-section" id="resultSection">
                    <div class="welcome-message">
                        <h2>Selamat Datang di Kamus Modern 2025! 🎉</h2>
                        <p>Ketik kata dalam bahasa Inggris di atas untuk melihat arti dan penjelasannya.</p>
                    </div>
                </div>
            </div>

            <!-- Right Sidebar Links -->
            <div class="links-sidebar">
                <h3 class="links-title">🔗 Link Cepat</h3>
                <div class="links-list">
                    {% for link in external_links %}
                    <a href="{{ link.url }}" target="_blank" class="link-item">
                        <span class="link-icon">{{ link.icon }}</span>
                        {{ link.name }}
                    </a>
                    {% endfor %}
                </div>

                <div class="quick-stats" style="margin-top: 32px; padding: 16px; background: #f1f5f9; border-radius: 12px;">
                    <h4 style="margin-bottom: 12px;">📊 Statistik</h4>
                    <p>Kata dicari: <span id="searchCount">0</span></p>
                    <p>Favorit: <span id="favoriteCount">0</span></p>
                </div>
            </div>
        </div>
    </div>

    <script>
        let searchCount = 0;
        let favoriteCount = 0;

        async function searchWord() {
            const word = document.getElementById('searchInput').value.trim();
            if (!word) return;

            const resultSection = document.getElementById('resultSection');
            resultSection.innerHTML = '<div class="loading">Memuat...</div>';

            try {
                const response = await fetch('/search', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ word: word })
                });

                const data = await response.json();
                displayResult(data);
                searchCount++;
                document.getElementById('searchCount').textContent = searchCount;
            } catch (error) {
                resultSection.innerHTML = '<div class="error">Terjadi kesalahan saat mencari kata.</div>';
            }
        }

        function displayResult(data) {
            const resultSection = document.getElementById('resultSection');
            
            if (data.error) {
                resultSection.innerHTML = `
                    <div class="word-card fade-in">
                        <div class="error-message">
                            <h3>❌ Kata tidak ditemukan</h3>
                            <p>${data.error}</p>
                        </div>
                    </div>
                `;
                return;
            }

            let html = '';
            data.forEach(entry => {
                html += `
                    <div class="word-card fade-in">
                        <div class="word-header">
                            <h2 class="word-title">${entry.word}</h2>
                            <button class="favorite-btn" onclick="addToFavorites('${entry.word}')">
                                <i class="far fa-star"></i> Favorit
                            </button>
                        </div>
                        ${entry.phonetics && entry.phonetics[0] ? 
                          `<div class="phonetic">/${entry.phonetics[0].text || ''}/</div>` : ''}
                `;

                entry.meanings.forEach(meaning => {
                    html += `
                        <div class="meaning-section">
                            <div class="part-of-speech">${meaning.partOfSpeech}</div>
                            ${meaning.definitions.slice(0, 3).map(def => `
                                <div class="definition">
                                    <strong>📖:</strong> ${def.definition}
                                    ${def.example ? `<br><em>"${def.example}"</em>` : ''}
                                </div>
                            `).join('')}
                        </div>
                    `;
                });

                html += `</div>`;
            });

            resultSection.innerHTML = html;
        }

        function addToFavorites(word) {
            fetch('/favorites', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ word: word })
            });
            favoriteCount++;
            document.getElementById('favoriteCount').textContent = favoriteCount;
            alert(`"${word}" ditambahkan ke favorit!`);
        }

        // Enter key support
        document.getElementById('searchInput').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                searchWord();
            }
        });

        // Tab switching
        document.querySelectorAll('.menu-item').forEach(item => {
            item.addEventListener('click', function() {
                document.querySelectorAll('.menu-item').forEach(i => i.classList.remove('active'));
                this.classList.add('active');
                // Implement tab functionality here
            });
        });
    </script>
</body>
</html>
