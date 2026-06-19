import streamlit as st

musicas = {
    "Gustavo Mioto": {
        "Despedida de casal": "https://www.youtube.com/watch?v=bX053n3_AYA&list=RDbX053n3_AYA&start_radio=1",
        "Impressionando os anjos": "https://www.youtube.com/watch?v=TK_j5NhE7Jg&list=RDTK_j5NhE7Jg&start_radio=1",
    },
    "Cristiano araujo": {
        "caso indefinido": "https://www.youtube.com/watch?v=2iUAbkwfxcY&list=RD2iUAbkwfxcY&start_radio=1",
        "maus bocados": "https://www.youtube.com/watch?v=5M3o0Kr121E&list=RD5M3o0Kr121E&start_radio=1",
    },
    "hungria": {
        "detalhes": "https://www.youtube.com/watch?v=vBNO9vjCMYo&list=RDvBNO9vjCMYo&start_radio=1"
            
    },
}

st.sidebar.image('logo.png')
artista = st.sidebar.selectbox('selecione o artista', musicas.keys())
musicas_artistas =  musicas[artista]
st.title(artista)
video,sobre = st.tabs(['video','sobre'])
with video:
    for musica in musicas_artistas.items():
        titulo, link = musica
        st.subheader(titulo)
        st.video(link)


with sobre:
    if artista == "Gustavo Mioto":
     st.markdown("""
# Gustavo Mioto 🎤

![Gustavo Mioto](https://portalaquivale.com.br/wp-content/uploads/2025/09/5-curiosidades-sobre-gustavo-mioto_1_34134.webp)

## Sobre

**Gustavo Pieroni Mioto** é um cantor e compositor brasileiro de música sertaneja, nascido em **12 de março de 1997**, em **Votuporanga, São Paulo**.

Ele começou sua carreira ainda jovem e conquistou grande destaque nacional com músicas como:

- Impressionando os Anjos  
- Com ou Sem Mim  
- Relógio  
- Solteiro Não Trai  
- Anti-Amor  

## Carreira

Gustavo Mioto é conhecido por misturar o sertanejo tradicional com um estilo moderno, conquistando milhões de fãs no Brasil.

## Redes e Site Oficial

🌐 Site Oficial: https://www.gustavomioto.com.br  

📷 Instagram: https://www.instagram.com/gustavomioto/

---

> Um dos principais nomes do sertanejo da nova geração brasileira.
""")
    elif artista == 'Cristiano araujo':
        st.markdown("""
# 🎤 Cristiano Araújo

![Cristiano Araújo]("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSSgl2pWySs156P2e9PLgPkzbIDlgp-x05CkxHFo1eNpQ&s=10")

## 📌 Sobre Cristiano Araújo

**Cristiano Araújo** foi um cantor e compositor brasileiro de música sertaneja, conhecido por seu grande sucesso no cenário musical brasileiro.

- **Nome completo:** Cristiano Melo Araújo  
- **Nascimento:** 24 de janeiro de 1986  
- **Cidade natal:** Goiânia, Goiás, Brasil  
- **Falecimento:** 24 de junho de 2015  
- **Gênero musical:** Sertanejo Universitário  

## 🎵 Principais músicas

- 🎶 É Com Ela Que Eu Estou  
- 🎶 Cê Que Sabe  
- 🎶 Caso Indefinido  
- 🎶 Maus Bocados  
- 🎶 Hoje Eu Tô Terrível  

## ⭐ Curiosidades

Cristiano começou a cantar ainda criança e se tornou um dos maiores nomes do sertanejo universitário no Brasil.

Seu falecimento em 2015 causou grande comoção nacional, deixando um legado marcante na música brasileira.

---

### 🖼 Outra imagem

<img src="https://i.scdn.co/image/ab6761610000e5eb8c4e1f7a9d8b5b6a2c2f5f10" width="300">

### 💙 Legado

Mesmo após sua partida, suas músicas continuam sendo ouvidas por milhões de fãs e fazem parte da história do sertanejo brasileiro.
""")
    elif artista == "hungria":
        st.markdown("""
# 🎤 Hungria Hip Hop

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTFyKBn0NJT98VEbgTkyzqHc-uLgyMUc5J3Ip4eQCkiYw&s=10")

## 📌 Sobre Hungria

**Hungria Hip Hop** é um cantor, compositor e rapper brasileiro conhecido por suas músicas que misturam rap, hip hop e elementos do pop, conquistando milhões de fãs no Brasil.

- **Nome verdadeiro:** Gustavo da Hungria Neves  
- **Nascimento:** 26 de maio de 1991  
- **Cidade natal:** Brasília, Distrito Federal, Brasil  
- **Gênero musical:** Rap, Hip Hop, Trap, Pop  

## 🎵 Principais músicas

- 🎶 Lembranças  
- 🎶 Dubai  
- 🎶 Amor e Fé  
- 🎶 Temporal  
- 🎶 Beijo com Trap  
- 🎶 Coração de Aço  

## 🚀 Carreira

Hungria começou sua carreira ainda jovem e ganhou destaque nacional através da internet, principalmente com videoclipes que alcançaram milhões de visualizações no YouTube.

Seu estilo mistura letras sobre superação, conquistas, vida pessoal e ostentação.

---

### 🖼 Outra imagem

<img src="https://i.scdn.co/image/ab6761610000e5eb2d1d7b0f9a8e34b64f8f3d1a" width="300">

## ⭐ Curiosidades

- É um dos rappers brasileiros com maior audiência nas plataformas digitais.  
- Seus clipes frequentemente ultrapassam dezenas de milhões de visualizações.  
- Possui uma base de fãs muito forte em todo o Brasil.

---

### 💙 Legado

Hungria se tornou uma referência do rap nacional, inspirando novos artistas e levando a música urbana brasileira para um público cada vez maior.
""")







