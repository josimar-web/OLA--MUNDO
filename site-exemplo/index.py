projeto = input("DIGITE A DESCRICAÇAO DO PROJETO: ")
horas_estimadas = input("Digite o total de horas estimadas: ")
valor_horas = input("Digite o valor hora trabalhado: ")
prazo = input("Digite o prazo estimado: ")

valor_total = int(horas_estimadas) * int(valor_horas)


print(valor_total)


from pdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.image("templete.PNG", x=0, y=0)
pdf.set_font("Arial")
pdf.text(115, 145, projeto)
pdf.text(115, 160, horas_estimadas)
pdf.text(115, 175, valor_horas)
pdf.text(115, 190, prazo)
pdf.text(115, 205, str(valor_total))


pdf.output("Orçamento.pdf")
print("Orçamento gerado com sucesso")

