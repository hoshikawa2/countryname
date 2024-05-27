from flask import Flask, request, jsonify
import requests
app = Flask(__name__)
@app.route('/enviar_dados', methods=['POST'])
def enviar_dados():    
    body = request.data

    #TRATAMENTO DO XML PASSADO DE REST PARA SOAP NO OIC
    print(body)
    body_string = body.decode('utf-8')
    body_string = body_string.replace("[", "<")
    body_string = body_string.replace("]", ">")
    body_string = body_string.replace("<root>", '')
    body_string = body_string.replace("</root>", '')
    body_string = body_string.replace("\n", "")
    body_string = body_string.replace("\t", "")
    body = body_string.encode('utf-8')
    print(body)

    #CHAMADA SOAP PADRAO
    headers = {'Content-Type': 'text/xml'}
    url = 'http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?op=CountryName'
    response = requests.post(url, data=body, headers=headers)
    print(response.text)

    #RETORNO REST COM XML
    return response.text, 200, {'Content-Type': 'application/xml'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
