from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# ... (kode ModernDictionary class sama seperti sebelumnya) ...

# HTML sebagai string langsung di Python
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kamus Modern 2025</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        /* CSS SAMA PERSIS seperti sebelumnya */
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
        /* ... (semua CSS dari sebelumnya) ... */
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
                <div class="menu" id="menuContainer">
                    <!-- Menu akan di-generate oleh JavaScript -->
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
                <div class="links-list" id="linksContainer">
                    <!-- Links akan di-generate oleh JavaScript -->
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
        // Data menu dan links
        const menuItems = [
            {"name": "Beranda", "icon": "🏠", "id": "home"},
            {"name": "Kamus", "icon": "📚", "id": "dictionary"},
            {"name": "Favorit", "icon": "⭐", "id": "favorites"},
            {"name": "Riwayat", "icon": "🕒", "id": "history"},
            {"name": "Kategori", "icon": "📁", "id": "categories"},
            {"name": "Belajar", "icon": "🎓", "id": "learn"},
            {"name": "Quiz", "icon": "❓", "id": "quiz"},
            {"name": "Pengaturan", "icon": "⚙️", "id": "settings"},
            {"name": "Bantuan", "icon": "❔", "id": "help"},
            {"name": "Tentang", "icon": "ℹ️", "id": "about"}
        ];
        
        const externalLinks = [
            {"name": "Kamus Online", "url": "https://kbbi.kemdikbud.go.id", "icon": "🌐"},
            {"name": "Translate", "url": "https://translate.google.com", "icon": "🔤"},
            {"name": "Sinonim", "url": "https://www.thesaurus.com", "icon": "🔄"},
            {"name": "Grammar", "url": "https://www.grammarly.com", "icon": "📝"},
            {"name": "Belajar Bahasa", "url": "https://www.duolingo.com", "icon": "🎯"},
            {"name": "AI Assistant", "url": "https://chat.openai.com", "icon": "🤖"},
            {"name": "E-Book", "url": "https://www.gutenberg.org", "icon": "📖"},
            {"name": "Podcast", "url": "https://www.spotify.com", "icon": "🎧"},
            {"name": "Forum", "url": "https://www.reddit.com/r/indonesia", "icon": "💬"},
            {"name": "Cloud Save", "url": "https://drive.google.com", "icon": "☁️"}
        ];

        // Generate menu dan links
        function initializeUI() {
            // Generate menu
            const menuContainer = document.getElementById('menuContainer');
            menuItems.forEach((item, index) => {
                const menuItem = document.createElement('div');
                menuItem.className = `menu-item ${index === 0 ? 'active' : ''}`;
                menuItem.innerHTML = `
                    <span class="menu-icon">${item.icon}</span>
                    ${item.name}
                `;
                menuContainer.appendChild(menuItem);
            });

            // Generate links
            const linksContainer = document.getElementById('linksContainer');
            externalLinks.forEach(link => {
                const linkItem = document.createElement('a');
                linkItem.href = link.url;
                linkItem.target = '_blank';
                linkItem.className = 'link-item';
                linkItem.innerHTML = `
                    <span class="link-icon">${link.icon}</span>
                    ${link.name}
                `;
                linksContainer.appendChild(linkItem);
            });
        }

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

        // Initialize UI ketika page load
        document.addEventListener('DOMContentLoaded', initializeUI);

        // Enter key support
        document.getElementById('searchInput').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                searchWord();
            }
        });

        // Tab switching
        document.addEventListener('click', function(e) {
            if (e.target.closest('.menu-item')) {
                document.querySelectorAll('.menu-item').forEach(i => i.classList.remove('active'));
                e.target.closest('.menu-item').classList.add('active');
            }
        });
    </script>
</body>
</html>
'''

# Inisialisasi kamus
dictionary = ModernDictionary()

@app.route('/')
def index():
    return HTML_TEMPLATE

# ... (routes lainnya tetap sama) ...
@app.route('/search', methods=['POST'])
def search():
    word = request.json.get('word', '').strip()
    if not word:
        return jsonify({"error": "Kata tidak boleh kosong"})
    
    if len(word) > 50:
        return jsonify({"error": "Kata terlalu panjang"})
        
    result = dictionary.search_word(word)
    return jsonify(result)

@app.route('/favorites', methods=['GET', 'POST'])
def manage_favorites():
    if request.method == 'POST':
        word = request.json.get('word', '').strip()
        if word and word not in dictionary.favorites:
            dictionary.favorites.append(word)
        return jsonify({"success": True, "favorites": dictionary.favorites})
    else:
        return jsonify({"favorites": dictionary.favorites})

@app.route('/history')
def get_history():
    return jsonify({"history": dictionary.search_history[-10:]})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
