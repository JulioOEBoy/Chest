from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib import colors

dados = {
    "nome": "Júlio César Ferreira Pedrini",
    "email": "jcpcgame8@gmail.com",
    "telefone": "(21) 97117-6976",
    "data_nascimento": "02/07/2004",
    "cidade": "Maricá, Rio de Janeiro",
    "formacao": "Análise e Desenvolvimento de Sistemas (1º período)\nUniversidade de Vassouras - 2025",
    "ensino_medio": "Ensino Médio completo - Certificação pelo ENCCEJA (2022)\nCertificado emitido pelo IFF",
    "tecnico": "Curso Técnico em Edificações (incompleto)\nIFF - Maricá",
    "experiencia": "Diretor de RH na miniempresa Flex Horizon\nJunior Achievement - IFF (2019)",
    "linguagens": "Python (preferência), HTML, CSS, JavaScript (iniciante)",
    "idiomas": "Português (nativo), Inglês (intermediário)",
    "foto": "Foto.jpg"
}

def gerar_curriculo(dados):
    pdf = canvas.Canvas("Curriculo_Julio_Pedrini.pdf", pagesize=A4)
    largura, altura = A4

    try:
        pdf.drawImage(dados["foto"], largura - 5*cm, altura - 5*cm, width=4*cm, height=4*cm, preserveAspectRatio=True, mask='auto')
    except:
        pdf.setFont("Helvetica", 10)
        pdf.drawString(largura - 7*cm, altura - 1*cm, "[Foto não encontrada]")

    # Nome
    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(2*cm, altura - 2*cm, dados["nome"])

    # Contato
    pdf.setFont("Helvetica", 11)
    pdf.drawString(2*cm, altura - 2.8*cm, f"📧 {dados['email']}")
    pdf.drawString(2*cm, altura - 3.3*cm, f"📞 {dados['telefone']}")
    pdf.drawString(2*cm, altura - 3.8*cm, f"🎂 Nasc.: {dados['data_nascimento']} | 📍 {dados['cidade']}")

    y = altura - 5*cm
    def secao(titulo, conteudo):
        nonlocal y
        pdf.setFont("Helvetica-Bold", 12)
        pdf.setFillColor(colors.HexColor("#003366"))
        pdf.drawString(2*cm, y, f"■ {titulo}")
        y -= 0.5*cm
        pdf.setFont("Helvetica", 11)
        pdf.setFillColor(colors.black)
        for linha in conteudo.split("\n"):
            pdf.drawString(2.5*cm, y, linha)
            y -= 0.5*cm
        y -= 0.2*cm

    # Seções
    secao("Formação Acadêmica", dados["formacao"])
    secao("Ensino Médio", dados["ensino_medio"])
    secao("Curso Técnico", dados["tecnico"])
    secao("Experiência", dados["experiencia"])
    secao("Linguagens e Tecnologias", dados["linguagens"])
    secao("Idiomas", dados["idiomas"])

    pdf.save()
    print("✅ Currículo gerado com sucesso: Curriculo_Julio_Pedrini.pdf")

gerar_curriculo(dados)
