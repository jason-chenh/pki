cfssl gencert -ca=../cfssl_certs_and_keys/ca.pem -ca-key=../cfssl_certs_and_keys/ca-key.pem \
  -config=ca-config.json -profile=server \
  nginx-backend-csr.json |cfssl-json -bare ../cfssl_certs_and_keys/nginx-backend

cfssl gencert -ca=../cfssl_certs_and_keys/ca.pem -ca-key=../cfssl_certs_and_keys/ca-key.pem \
  -config=ca-config.json -profile=client \
  nginx-client-csr.json |cfssl-json -bare ../cfssl_certs_and_keys/nginx-client

cfssl gencert -ca=../cfssl_certs_and_keys/ca.pem -ca-key=../cfssl_certs_and_keys/ca-key.pem \
  -config=ca-config.json -profile=server \
  grafana-csr.json |cfssl-json -bare ../cfssl_certs_and_keys/grafana

cfssl gencert -ca=../cfssl_certs_and_keys/ca.pem -ca-key=../cfssl_certs_and_keys/ca-key.pem \
  -config=ca-config.json -profile=server \
  elasticsearch-csr.json |cfssl-json -bare ../cfssl_certs_and_keys/elasticsearch

cfssl gencert -ca=../cfssl_certs_and_keys/ca.pem -ca-key=../cfssl_certs_and_keys/ca-key.pem \
  -config=ca-config.json -profile=server \
  kibana-csr.json |cfssl-json -bare ../cfssl_certs_and_keys/kibana

cfssl gencert -ca=../cfssl_certs_and_keys/ca.pem -ca-key=../cfssl_certs_and_keys/ca-key.pem \
  -config=ca-config.json -profile=server \
  gitlab-csr.json |cfssl-json -bare ../cfssl_certs_and_keys/gitlab
