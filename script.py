from PIL import Image, ImageDraw
import os

# ===== CONFIG =====
pasta_origem = "."          # pasta atual
pasta_saida = "saida"
tamanho_final = 64
extensoes_validas = (".png", ".jpg", ".jpeg", ".webp")

# ==================

os.makedirs(pasta_saida, exist_ok=True)

for arquivo in os.listdir(pasta_origem):
    if arquivo.lower().endswith(extensoes_validas):

        caminho = os.path.join(pasta_origem, arquivo)
        img = Image.open(caminho).convert("RGBA")

        # Deixa quadrado
        menor = min(img.size)
        img = img.crop((
            (img.width - menor) // 2,
            (img.height - menor) // 2,
            (img.width + menor) // 2,
            (img.height + menor) // 2
        ))

        # Redimensiona
        img = img.resize((tamanho_final, tamanho_final), Image.LANCZOS)

        # Máscara circular
        mask = Image.new("L", (tamanho_final, tamanho_final), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, tamanho_final, tamanho_final), fill=255)

        img.putalpha(mask)

        nome_saida = os.path.join(pasta_saida, arquivo.split(".")[0] + ".png")
        img.save(nome_saida)

        print(f"Processado: {arquivo}")

print("\nConcluído! Arquivos salvos na pasta 'saida'")