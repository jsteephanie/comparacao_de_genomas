# Leitura dos genomas
entrada_bacteria = open("16s_bacteria.fasta").read()
entrada_humano = open("18s_humano.fasta").read()

# Processamento da bactéria
cont_bacteria = {}
for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        cont_bacteria[i+j] = 0

entrada_bacteria = entrada_bacteria.replace("\n","")

for k in range(len(entrada_bacteria)-1):
    cont_bacteria[entrada_bacteria[k]+entrada_bacteria[k+1]] += 1

# Processamento do humano
cont_humano = {}
for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        cont_humano[i+j] = 0

entrada_humano = entrada_humano.replace("\n","")

for k in range(len(entrada_humano)-1):
    cont_humano[entrada_humano[k]+entrada_humano[k+1]] += 1

# HTML
saida = open("comparacao_genomas.html","w")

# Quadro de comparação: bactéria
saida.write("<div style='width:50%; float:left;'>")
saida.write("<h2>Bactéria</h2>")

i = 1
saida.write("<div style='margin-right: 450px; '>")
for k in cont_bacteria:
    saida.write(k + ": " + str(cont_bacteria[k]) + "<br>")
    i+=1
saida.write("</div>")

i = 1
for k in cont_bacteria:
    transparencia = cont_bacteria[k]/max(cont_bacteria.values())
    saida.write("<div style='width:100px; border:1px solid #111;color:#fff; height:100px; float:left; background-color:rgba(0, 0, 0, "+str(transparencia)+"')>"+k+"</div>")
    if i%4 == 0:
        saida.write("<div style= 'clear:both'></div>")
    i+=1
saida.write("</div>")

# Quadro de comparação: humano
saida.write("<div style='width:50%; float:left;'>")
saida.write("<h2>Humano</h2>")

i = 1
saida.write("<div style='margin-right: 20px;'>")
for k in cont_humano:
    saida.write(k + ": " + str(cont_humano[k]) + "<br>")
    i+=1
saida.write("</div>")

i = 1
for k in cont_humano:
    transparencia = cont_humano[k]/max(cont_humano.values())
    saida.write("<div style='width:100px; border:1px solid #111;color:#fff; height:100px; float:left; background-color:rgba(0, 0, 0, "+str(transparencia)+"')>"+k+"</div>")
    if i%4 == 0:
        saida.write("<div style= 'clear:both'></div>")
    i+=1
saida.write("</div>")

saida.close()
