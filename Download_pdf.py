import requests
from PyPDF2 import PdfFileReader, PdfFileWriter


collegiate = 1

while collegiate < 888:
    coll_url = f"{collegiate:03}"
    url = 'http://matricula.ufba.br/{}_alocacao_vagas.pdf'.format(collegiate)
    resp = requests.get(url)
    if resp.status_code == 200:
        print("reading collegiate no {}".format(coll_url))
        with open("C:\\Users\\goesp\\Desktop\\PDF Python\\Collegiate_{}.pdf".format(coll_url), "wb") as f:
            f.write(resp.content)

    collegiate += 1
