import requests

# Change this APM Endpoint url
apm_upload_endpoint_url="https://aaaac6cswfqmgaaaaaaaaaae3q.apm-agt.us-ashburn-1.oci.oraclecloud.com/20200101/observations/public-span?dataFormat=zipkin&dataFormatVersion=2&dataKey=KYXSMQC7DELJ2NSHIKFM6B3RUJRFFJNR"

def http_transport(encoded_span):
    result = requests.post(
        #Construct a URL that communicate with Application Performance Monitoring
        apm_upload_endpoint_url,
        data=encoded_span,
        headers={'Content-Type': 'application/json'},
    )
    return result