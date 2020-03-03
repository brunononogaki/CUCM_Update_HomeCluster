import requests, urllib3
urllib3.disable_warnings()

# Coletando informacoes do servidor
username = input('CUCM Username: ')
password = input('CUCM Password: ')
url = 'https://' + ipaddress + ':8443/axl/'


homecluster = input("Habilitar ou desabilitar o Home Cluster (t/f): ")

#Abrindo o arquito txt
with open ('lista_usuarios.txt') as arquivo:
    for linha in arquivo:
        usuario = linha.rstrip("\n")

        data = """
        <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
        <SOAP-ENV:Body>
        <axl:updateUser xmlns:axl="http://www.cisco.com/AXL/API/1.0" sequence="1">
	        <userid>"""+usuario+"""</userid>
			<homeCluster>"""+homecluster+"""</homeCluster>
        </axl:updateUser>
        </SOAP-ENV:Body>
        </SOAP-ENV:Envelope>
        """

        p = requests.post(url,verify=False,auth=(username, password),data=data)

        if p.status_code == 200:
            print("Sucesso! Usuario {} teve o home cluster alterado para {} com sucesso".format(usuario,homecluster))
        else:
            print("Erro! Usuario {} nao teve o home cluster alterado para {}.".format(usuario,homecluster))

input("pressione enter para encerrar...")
arquivo.close()
