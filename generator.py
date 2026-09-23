import os

AUDIO_DIR = "audio"
OUTPUT_FILE = "index.html"

# Pega todos os arquivos de áudio suportados na pasta
audio_extensions = (".mp3", ".wav", ".ogg", ".flac", ".m4a")
files = []

if os.path.exists(AUDIO_DIR):
    files = sorted([f for f in os.listdir(AUDIO_DIR) if f.lower().endswith(audio_extensions)])

# Monta o HTML dinamicamente
html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prévias de Músicas</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background-color: #0f172a;
            color: #f8fafc;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 50px 20px;
            margin: 0;
        }}
        h1 {{
            margin-bottom: 30px;
            font-size: 1.8rem;
        }}
        .container {{
            width: 100%;
            max-width: 500px;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }}
        .btn {{
            background-color: #1e293b;
            color: #38bdf8;
            border: 1px solid #334155;
            padding: 14px 20px;
            border-radius: 8px;
            text-decoration: none;
            font-size: 1rem;
            font-weight: 500;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: background 0.2s, border-color 0.2s;
        }}
        .btn:hover {{
            background-color: #334155;
            border-color: #38bdf8;
        }}
        .empty {{
            color: #94a3b8;
            text-align: center;
        }}
    </style>
</head>
<body>

    <h1>Prévias de Músicas</h1>

    <div class="container">
"""

if files:
    for file in files:
        # Nome limpo para exibir no botão (retira a extensão)
        name_without_ext = os.path.splitext(file)[0]
        html_content += f'        <a class="btn" href="audio/{file}" download><span>🎵 {name_without_ext}</span> 📥 Baixar/Ouvir</a>\n'
else:
    html_content += '        <p class="empty">Nenhuma prévia encontrada na pasta.</p>\n'

html_content += """    </div>

</body>
</html>
"""

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"index.html gerado com sucesso para {len(files)} arquivos!")
