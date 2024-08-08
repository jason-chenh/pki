### ASA基本网络配置
```shell
hostname asa
domain-name qytang.com
clock timezone GMT +8

dns domain-lookup outside
dns name-server 202.100.1.100

ntp server 202.100.1.1 source Outside prefer

access-list out extended permit ip any any
access-group out in interface Outside

```

### ASA Trustpoint配置
```shell
crypto key generate rsa label l2lvpn modulus 2048

crypto ca trustpoint msca
 enrollment terminal
 fqdn asa.qytang.com
 subject-name CN=asa.qytang.com, C=CN, L=Beijing, ST=Beijing, O=qytang, OU=qytangsec
 ip-address 202.100.3.10
 keypair l2lvpn

```
### 导入根证书
```shell
asa(config)# crypto ca authenticate msca
Enter the base 64 encoded CA certificate.
End with the word "quit" on a line by itself
-----BEGIN CERTIFICATE-----
MIIDbTCCAlWgAwIBAgIQJcRmBo8xZoBJaZs01icj9zANBgkqhkiG9w0BAQsFADBJ
MRMwEQYKCZImiZPyLGQBGRYDY29tMRYwFAYKCZImiZPyLGQBGRYGcXl0YW5nMRow
GAYDVQQDExFxeXRhbmctV0lOMjAxOS1DQTAeFw0yMzEwMjEwMTE1NDVaFw0yODEw
MjEwMTI1NDVaMEkxEzARBgoJkiaJk/IsZAEZFgNjb20xFjAUBgoJkiaJk/IsZAEZ
FgZxeXRhbmcxGjAYBgNVBAMTEXF5dGFuZy1XSU4yMDE5LUNBMIIBIjANBgkqhkiG
9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzw1aa1VGZC2w4sS5SfYzIV2p5G4qy6PnwfD3
NkmjBDliFH7+RQi1NSWedmCRUe+TJrfD3O44J35Ld5d72Ygv1NzF/8x1W6v3KrbB
QML5LEgHIZgVmLV3yhcg/U5QbhgS20sEPa91GamP8ndy2jBVdVtLqWC7owdKV0nS
7LixGjU4G0rgga4SomULrDatQV4hXvyP0n0zlBTfl1sen9oKoDpyb+/CNKpKOu88
ckd9u3FH/kxX1jQD74SmGemyB78dlLJPFYGRzBdtyV3Yl8DueWC1uhDkSJ5BclQk
ril0D6s8nOim+BcF2zTOHRVqP1n/+6g8MBn4Bw4dEbxpnU9f4QIDAQABo1EwTzAL
BgNVHQ8EBAMCAYYwDwYDVR0TAQH/BAUwAwEB/zAdBgNVHQ4EFgQUl5V0786RkOsg
wO7RB7UU3I+qf5gwEAYJKwYBBAGCNxUBBAMCAQAwDQYJKoZIhvcNAQELBQADggEB
ADFd/bqS4C8MFQzNMkFAjL0JF62GPA4CYMkwzt9tjL+bUcoS7gvyLWpWs55BDA7v
vWTY5UL7UI0GkcWsxfTUCIKtXmb3h7AqvxCKVTA/Xa1v3hqFdYFvqEK2Hp4s1JaC
CfEe5BsTQu/vr40MS2cr5q0HIr810E7UKviHCCvPUd11UWk2yDsyXZGa9aLKdxZ9
/PsfcKJKuBx/AaVXBZkyFyUzwfcrZ7UCurVF9eRw75KR1ErM3sZMyrg+eHa19RCH
NHn9WtpuBQc22A2BT+tz1K7LHRB6boV8nZbbMkAN06ul/Bi/bC3OSLh5m7n2aB6Y
uchIOFtZayghUGl5JSlcB6Q=
-----END CERTIFICATE-----

quit

INFO: Certificate has the following attributes:
Fingerprint:     dbc1e67d 061ff7f2 9f9b3a10 63fc7912
Do you accept this certificate? [yes/no]: yes

Trustpoint CA certificate accepted.

% Certificate successfully imported
```

### 查看证书
```shell
asa# show crypto ca certificates msca
CA Certificate
  Status: Available
  Certificate Serial Number: 25c466068f31668049699b34d62723f7
  Certificate Usage: Signature
  Public Key Type: RSA (2048 bits)
  Signature Algorithm: SHA256 with RSA Encryption
  Issuer Name:
    cn=qytang-WIN2019-CA
    dc=qytang
    dc=com
  Subject Name:
    cn=qytang-WIN2019-CA
    dc=qytang
    dc=com
  Validity Date:
    start date: 09:15:45 GMT Oct 21 2023
    end   date: 09:25:45 GMT Oct 21 2028
  Associated Trustpoints: msca

```

### 申请证书(使用模块"QYT IPSec (脱机申请)")
```shell
asa(config)# crypto ca enroll msca
% Start certificate enrollment ..
% The subject name in the certificate will be: CN=asa.qytang.com, C=CN, L=Beijing, ST=Beijing, O=qytang, OU=qytangsec

% The fully-qualified domain name in the certificate will be: asa.qytang.com

% Include the device serial number in the subject name? [yes/no]: no

% The IP address in the certificate is 202.100.3.10

Display Certificate Request to terminal? [yes/no]: yes
Certificate Request follows:
-----BEGIN CERTIFICATE REQUEST-----
MIIDKzCCAhMCAQAwgakxEjAQBgNVBAsTCXF5dGFuZ3NlYzEPMA0GA1UEChMGcXl0
YW5nMRAwDgYDVQQIEwdCZWlqaW5nMRAwDgYDVQQHEwdCZWlqaW5nMQswCQYDVQQG
EwJDTjEXMBUGA1UEAxMOYXNhLnF5dGFuZy5jb20xODAZBgkqhkiG9w0BCQgTDDIw
Mi4xMDAuMy4xMDAbBgkqhkiG9w0BCQIWDmFzYS5xeXRhbmcuY29tMIIBIjANBgkq
hkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtOoJrqepWK/ypILjG1pKQtptLa5sa/OR
jGuBaptU2x2+MEPWsvBQf+zqxO/2VkodYZQJ1i9iuEuEUfPIEDZMUNA5vUuTkj2x
imaPVcV4/TG6sDo8LceUXJu2XSjpRlCagUR9xmMDhs/nnx9g4mvD+LVZEAbTiw4E
9SCZKN1XYnIKMtYR8tSScF9nm+BYjg2HVVtd9UybkrL77jPRqSWgViPb/OHyczJL
aqjizyrMYwSIwD5h4cPGaEGLc8lf4bUtp5XBYQoLhhhbcAAZMJg2Ub/VXhnLH0zq
9cLXfcK58snTDapbY3gh4v5ZWV8xzPunnIukAdOTsac8XwTWL4FylwIDAQABoDww
OgYJKoZIhvcNAQkOMS0wKzAOBgNVHQ8BAf8EBAMCBaAwGQYDVR0RBBIwEIIOYXNh
LnF5dGFuZy5jb20wDQYJKoZIhvcNAQEFBQADggEBAEdF+uKWGRA4h+M1UTSmXQAW
xroFRyVxnYTu6a+uPbvkOHo1L1+T7i9wCvMuNHwJeSTcI53ldbjveWvu+m3AJ+/A
d8a4iVL6aAb4wUQVJeWxBbod89+dAO3MuHXqcELTjm9/BucxFqmPdEO1DSLm8973
r+beLCKxM2kLdD+AzjnwtK7a3XY9JDuP+mX/zufK0IiML4vA3c/4mgQOO46YfZ+h
QwxJNq07OJCHXsuEgymwykomVKmcTLVvt5CsFKR1kOi4ERjJ8P4qifDGCTCIRsyn
9PQLMoR/yjXLZKKVw9KgRQhIBUsu1CirFuYWSNNQmD7Kq8Wzd1D7lHO5Nc+P3ZY=
-----END CERTIFICATE REQUEST-----

```

### 导入申请的证书
```shell
asa(config)# crypto ca import msca certificate

% The fully-qualified domain name in the certificate will be: asa.qytang.com

% The IP address in the certificate is 202.100.3.10


Enter the base 64 encoded certificate.
End with the word "quit" on a line by itself

-----BEGIN CERTIFICATE-----
MIIGJjCCBQ6gAwIBAgITeAAAAC+Ua33uomi40gAAAAAALzANBgkqhkiG9w0BAQsF
ADBJMRMwEQYKCZImiZPyLGQBGRYDY29tMRYwFAYKCZImiZPyLGQBGRYGcXl0YW5n
MRowGAYDVQQDExFxeXRhbmctV0lOMjAxOS1DQTAeFw0yMzEwMjYwOTE0MDZaFw0y
NTEwMjUwOTE0MDZaMIGrMRswGQYJKoZIhvcNAQkIEwwyMDIuMTAwLjMuMTAxHTAb
BgkqhkiG9w0BCQITDmFzYS5xeXRhbmcuY29tMQswCQYDVQQGEwJDTjEQMA4GA1UE
CBMHQmVpamluZzEQMA4GA1UEBxMHQmVpamluZzEPMA0GA1UEChMGcXl0YW5nMRIw
EAYDVQQLEwlxeXRhbmdzZWMxFzAVBgNVBAMTDmFzYS5xeXRhbmcuY29tMIIBIjAN
BgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtOoJrqepWK/ypILjG1pKQtptLa5s
a/ORjGuBaptU2x2+MEPWsvBQf+zqxO/2VkodYZQJ1i9iuEuEUfPIEDZMUNA5vUuT
kj2ximaPVcV4/TG6sDo8LceUXJu2XSjpRlCagUR9xmMDhs/nnx9g4mvD+LVZEAbT
iw4E9SCZKN1XYnIKMtYR8tSScF9nm+BYjg2HVVtd9UybkrL77jPRqSWgViPb/OHy
czJLaqjizyrMYwSIwD5h4cPGaEGLc8lf4bUtp5XBYQoLhhhbcAAZMJg2Ub/VXhnL
H0zq9cLXfcK58snTDapbY3gh4v5ZWV8xzPunnIukAdOTsac8XwTWL4FylwIDAQAB
o4ICojCCAp4wDgYDVR0PAQH/BAQDAgWgMBkGA1UdEQQSMBCCDmFzYS5xeXRhbmcu
Y29tMB0GA1UdDgQWBBReB2owtFX2J1pa4ZMeHJcKGizlVzAfBgNVHSMEGDAWgBSX
lXTvzpGQ6yDA7tEHtRTcj6p/mDCBzgYDVR0fBIHGMIHDMIHAoIG9oIG6hoG3bGRh
cDovLy9DTj1xeXRhbmctV0lOMjAxOS1DQSxDTj1XSU4yMDE5LENOPUNEUCxDTj1Q
dWJsaWMlMjBLZXklMjBTZXJ2aWNlcyxDTj1TZXJ2aWNlcyxDTj1Db25maWd1cmF0
aW9uLERDPXF5dGFuZyxEQz1jb20/Y2VydGlmaWNhdGVSZXZvY2F0aW9uTGlzdD9i
YXNlP29iamVjdENsYXNzPWNSTERpc3RyaWJ1dGlvblBvaW50MIHCBggrBgEFBQcB
AQSBtTCBsjCBrwYIKwYBBQUHMAKGgaJsZGFwOi8vL0NOPXF5dGFuZy1XSU4yMDE5
LUNBLENOPUFJQSxDTj1QdWJsaWMlMjBLZXklMjBTZXJ2aWNlcyxDTj1TZXJ2aWNl
cyxDTj1Db25maWd1cmF0aW9uLERDPXF5dGFuZyxEQz1jb20/Y0FDZXJ0aWZpY2F0
ZT9iYXNlP29iamVjdENsYXNzPWNlcnRpZmljYXRpb25BdXRob3JpdHkwPQYJKwYB
BAGCNxUHBDAwLgYmKwYBBAGCNxUIgZX4d4OG0HCB4YUThL/hIoTp6Bw/ha2VV4Lb
ulMCAWQCAQUwJwYDVR0lBCAwHgYIKwYBBQUHAwIGCCsGAQUFBwMBBggrBgEFBQgC
AjAzBgkrBgEEAYI3FQoEJjAkMAoGCCsGAQUFBwMCMAoGCCsGAQUFBwMBMAoGCCsG
AQUFCAICMA0GCSqGSIb3DQEBCwUAA4IBAQC1BpR0hiXfoWYaz6i+CLXi+6HDi5sr
ig2YCpZ471aLR+obEfnPB/rYTwWtIy9mZz98NFGXgrlr08xSS8Hfcn/PnE6+qMnr
jaNZPG/H0w4fh5/pwVr6OGBi5k/OOPYrX45Qk6W5ZLbiFWHR17pBT1tN5tL3QLaJ
V/pJhVMiwFcVIR3RGD4jZuDYE8hf3bdxL1M7wK5FqcupeSWGbKzTVwLJvjcWM9rx
PpsU1KmlrO+NqbR6u8rGmypMKIaUvKxV4vdmUgFZZVtrPpzBiQNEvSiKoRxSOV5k
0jbs/rXfkxJD7T48hQf3vYB31Ji5JcoCp5RVGhHWyeuvWrbV/KVYbh45
-----END CERTIFICATE-----

quit
INFO: Certificate successfully imported

```

### 查看最终的证书
```shell
asa# show crypto ca certificates msca
Certificate
  Status: Available
  Certificate Serial Number: 110000000a0ff0f5864f6a7bf000000000000a
  Certificate Usage: General Purpose
  Public Key Type: RSA (2048 bits)
  Signature Algorithm: SHA256 with RSA Encryption
  Issuer Name:
    cn=qytang-WIN2019-CA
    dc=qytang
    dc=com
  Subject Name:
    cn=asa.qytang.com
    ou=qytangsec
    o=qytang
    l=Beijing
    st=Beijing
    c=CN
    hostname=asa.qytang.com
    ipaddress=202.100.3.10
  CRL Distribution Points:
    [1]  ldap:///CN=qytang-WIN2019-CA,CN=WIN2019,CN=CDP,CN=Public%20Key%20Services,CN=Services,CN=Configuration,DC=qytang,DC=com?certificateRevocationList?base?objectClass=cRLDistributionPoint
  Validity Date:
    start date: 16:26:07 GMT Oct 30 2023
    end   date: 16:26:07 GMT Oct 29 2025
  Associated Trustpoints: msca

CA Certificate
  Status: Available
  Certificate Serial Number: 3eec76fb95de8eaa4f8ba62964a87d98
  Certificate Usage: Signature
  Public Key Type: RSA (2048 bits)
  Signature Algorithm: SHA256 with RSA Encryption
  Issuer Name:
    cn=qytang-WIN2019-CA
    dc=qytang
    dc=com
  Subject Name:
    cn=qytang-WIN2019-CA
    dc=qytang
    dc=com
  Validity Date:
    start date: 15:49:05 GMT Oct 30 2023
    end   date: 15:59:04 GMT Oct 30 2028
  Associated Trustpoints: test msca

```

### ASA Tunnel Group配置
```shell
group-policy ikev1-policy internal
group-policy ikev1-policy attributes
 vpn-tunnel-protocol ikev1

tunnel-group qytangsec type ipsec-l2l
tunnel-group qytangsec general-attributes
 default-group-policy ikev1-policy
tunnel-group qytangsec ipsec-attributes
 chain
 ikev1 trust-point msca

crypto ca certificate map qytmap 10
 subject-name attr ou co qytangsec

tunnel-group-map qytmap 10 qytangsec

```

### ASA IPSec VPN配置
```shell
crypto ikev1 enable Outside
crypto ikev1 policy 10
 authentication rsa-sig
 encryption 3des
 hash md5
 group 2
 lifetime 86400

access-list vpn extended permit ip 10.1.3.0 255.255.255.0 10.1.2.0 255.255.255.0

crypto ipsec ikev1 transform-set cisco esp-3des esp-md5-hmac

crypto map cisco 10 match address vpn
crypto map cisco 10 set peer 202.100.1.253
crypto map cisco 10 set ikev1 transform-set cisco
crypto map cisco 10 set trustpoint msca chain
crypto map cisco interface Outside

```
