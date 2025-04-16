from fpdf import FPDF
from PIL import Image

class PDF(FPDF):
    def header(self):
        pass

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

# Adiciona a foto
photo_path = "1690003392890 (1) (1).jpg"
try:
    pdf.image(photo_path, x=10, y=10, w=30, h=30)
except RuntimeError as e:
    print(f"Erro ao adicionar imagem: {e}")

pdf.set_font("Arial", size=12)
pdf.set_xy(45, 10)
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "JÚLIO CÉSAR FERREIRA PEDRINI", ln=True)

pdf.set_font("Arial", '', 10)
pdf.set_x(45)
pdf.cell(0, 10, "Estudante de Análise e Desenvolvimento de Sistemas", ln=True)

pdf.set_xy(10, 45)
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "CONTATO", ln=True)

pdf.set_font("Arial", '', 10)
pdf.cell(0, 8, "📧 jcpcgame8@gmail.com", ln=True)
pdf.cell(0, 8, "📞 (21) 97117-6976", ln=True)
pdf.cell(0, 8, "📍 Maricá - RJ", ln=True)
pdf.cell(0, 8, "🗓️ Nascimento: 02/07/2004", ln=True)

pdf.ln(5)
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "FORMAÇÃO ACADÊMICA", ln=True)

pdf.set_font("Arial", '', 10)
pdf.multi_cell(0, 8, "📚 Universidade de Vassouras (Polo Maricá)\nCurso: Análise e Desenvolvimento de Sistemas (1º período)\n\n🎓 Ensino Médio – Certificado pelo ENCCEJA (emitido pelo IFF - Instituto Federal Fluminense)")

pdf.ln(2)
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "EXPERIÊNCIAS", ln=True)

pdf.set_font("Arial", '', 10)
pdf.multi_cell(0, 8, "💼 Diretor de RH – Miniempresa Flex Horizon (Projeto Junior Achievement – 2019)\nAtuação com gestão de equipe, recrutamento e dinâmica de grupo durante o projeto no IFF.")

pdf.ln(2)
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "CURSOS E CONHECIMENTOS", ln=True)

pdf.set_font("Arial", '', 10)
pdf.multi_cell(0, 8, "💻 Técnico em Edificações (não concluído – Ensino Médio integrado)\n🧠 Programação em Python (nível iniciante/intermediário)\n🌐 Inglês Intermediário\n🛠️ Interesse por desenvolvimento de sistemas, tecnologia e inovação.")

pdf.ln(2)
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "INFORMAÇÕES ADICIONAIS", ln=True)

pdf.set_font("Arial", '', 10)
pdf.multi_cell(0, 8, "✨ Proativo, comunicativo e com facilidade para trabalho em equipe.\n🔍 Busca por oportunidades de estágio e desenvolvimento na área de TI.")

pdf.output("Curriculo_Julio_Pedrini.pdf")
