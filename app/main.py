from flask import Flask, jsonify

from py_zipkin import Encoding #import Zipkin package
from py_zipkin.zipkin import zipkin_span #import Zipkin package
from transport import http_transport #import Zipkin transport
import requests

app = Flask(__name__)

@zipkin_span(service_name='findCustomer', span_name='findCustomer')
@app.route("/findCustomer/<string:nome>/<string:cpf>/<string:cartao>", methods=['GET'])
def findCustomer(nome, cpf, cartao):
    with zipkin_span(
            service_name="findCustomer", #You can change it as you need
            span_name="get", #You can change it as you need
            transport_handler=http_transport, #zipkin transport, will use it to upload trace data to OCI APM
            encoding = Encoding.V2_JSON,
            binary_annotations = {"get":"customer information for BOT"}, #Custom tag
            sample_rate=100 # this is optional and can be used to set custom sample rates
    ):
        nomeCompleto = "Cristiano Hoshikawa";
        plano = "Plano Super";
        return jsonify({'nomeCompleto': nomeCompleto, 'plano': plano});

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8082)
