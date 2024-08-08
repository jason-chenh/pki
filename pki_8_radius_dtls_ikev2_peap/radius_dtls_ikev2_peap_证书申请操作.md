### --------- 申请Radius TLS证书(证书模板: QYT Web服务器) ----------
### Radius DTLS: 加载微软根证书
```shell
CSR3(config)#crypto pki authenticate DTLS

Enter the base 64 encoded CA certificate.
End with a blank line or the word "quit" on a line by itself

-----BEGIN CERTIFICATE-----
MIIDbTCCAlWgAwIBAgIQPux2+5XejqpPi6YpZKh9mDANBgkqhkiG9w0BAQsFADBJ
MRMwEQYKCZImiZPyLGQBGRYDY29tMRYwFAYKCZImiZPyLGQBGRYGcXl0YW5nMRow
GAYDVQQDExFxeXRhbmctV0lOMjAxOS1DQTAeFw0yMzEwMzAwNzQ5MDVaFw0yODEw
MzAwNzU5MDRaMEkxEzARBgoJkiaJk/IsZAEZFgNjb20xFjAUBgoJkiaJk/IsZAEZ
FgZxeXRhbmcxGjAYBgNVBAMTEXF5dGFuZy1XSU4yMDE5LUNBMIIBIjANBgkqhkiG
9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqZl6EUXQnjJi05Q8pSyotgdT8t+PkHS0rB7h
jDpG0jRzWmHK+JUB7tjgDDi4sZJmFrJZguqgRg8oDaxi0mLgfnbRuyiEmyQ3qT5o
OsS53NUwzzwMaZt3Xa3QbWz1esVYoXaBrxj4jzVJnLfj/ipqm2IDUp2c4t5/dJ6p
dm2wozLDvfkh0WVAIsou6idhD70xs0qFlJXpzr9+bMIgmku7CXY4t0znxbcGj7k4
Flo0QNK/ntBNJvf9d2apYwwBKVW67fXLwdspNX6QSFvXrD+RpIbrCwzDbwTRMi6l
8uJQvhaR2Iz3ofhc0T3Iz82VYnWkhTEpdgpEJs/Re126HlKdgQIDAQABo1EwTzAL
BgNVHQ8EBAMCAYYwDwYDVR0TAQH/BAUwAwEB/zAdBgNVHQ4EFgQUUFL70NIGv4uo
SdsmnSXzP5nYHIAwEAYJKwYBBAGCNxUBBAMCAQAwDQYJKoZIhvcNAQELBQADggEB
ADJkbCedFrbzODUSES3PPPC0lDuZSF7CfZtsVmmM/mJ932uvw5DvlFw5qxB3EMbk
jyY32YZs6Njxcr36QZUnyQHRjx2JlC6Kbi5k2SgihOcvB9HhDOP8AKLe442FBotA
Mraq3smNE8V9tnT9ouPYhkOz1C/vhxd22yphfDcYDSrutNivPkdP+G2+lgLlr8oh
50tUMLWsZ996pccGQrdo9uomLUROQ8d+a/vul3K31fEe9Prb1U5JLJjP51WqxGfH
UdfOG390ZJs0HGiKACznp6ccKLulntBv1UESToEyIPIUxQlMquSVZcNqi7OyCc+G
vop+0ldAf+lonSgSAdwqiQA=
-----END CERTIFICATE-----

Certificate has the following attributes:
       Fingerprint MD5: AE7B21B0 3019A3F3 363D140A E322B988
      Fingerprint SHA1: 19E61C59 1FA33FE3 7568155F D9ABE527 C8395A8B

% Do you accept this certificate? [yes/no]: yes
Trustpoint CA certificate accepted.
% Certificate successfully imported

```

### Radius DTLS: 产生证书申请
```shell
CSR3(config)#crypto pki enroll DTLS
% Start certificate enrollment ..

% The subject name in the certificate will include: cn=c8kv3.qytang.com,ou=qytangbj,o=qytang
% The subject name in the certificate will include: c8kv3.qytang.com
% Include the router serial number in the subject name? [yes/no]: no
% The IP address in the certificate is 202.100.3.1

Display Certificate Request to terminal? [yes/no]: yes
Certificate Request follows:

MIIC4DCCAcgCAQAwejEPMA0GA1UEChMGcXl0YW5nMREwDwYDVQQLEwhxeXRhbmdi
ajEZMBcGA1UEAxMQYzhrdjMucXl0YW5nLmNvbTE5MBgGCSqGSIb3DQEJCBMLMjAy
LjEwMC4zLjEwHQYJKoZIhvcNAQkCFhBjOGt2My5xeXRhbmcuY29tMIIBIjANBgkq
hkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyZPQmkw/bY9sWJl+ThAQqpA6W7mhm9SW
tprO4PkVIwKdXjl5x0x4/FrwmrihCpXDdo9rW+HLPj5sFXg3Ur9RsEaxWms9tFEz
ehFjSKtefvHbAryI0cFrpUNaQUkUf3ph8ZDPJNT/ENljT00IB37OCwAAxFxRx7Ix
WeC+WlFexjL510lW9BTguzV58eq+LX20k5uBO0bdbpLVYjWMri+zx7vAO+als/IR
zEUewm9vkV048ddrhtqyAxXGrs5hZzCdTE6tEYHOuLYBBhkmdNXb0hihmBdlwpZs
q6dlRDY8Z6qhGU8pHGmUvS3q0vUlrFKN3ONfSOmdcIvVFHd4Q1uUZQIDAQABoCEw
HwYJKoZIhvcNAQkOMRIwEDAOBgNVHQ8BAf8EBAMCBaAwDQYJKoZIhvcNAQEFBQAD
ggEBADbnqPzm9c0dGT5X7KvwvJJSwZU8ee5fEyiQ29G6GjHWvSgvivoWrTZKoHV1
V61Sh8qtQPq5zVWMZXVDF/35G0xlDW4HMN8pPdV83mSBL1//nRgWPgk0FP8FYKft
7YjV0R1VJCFgV6gwvvxHI/dE2doyOW7A6QpIWJp3xZ6p4ekR0SbiDdRwdwmJXPb7
XiuFA/Z6QazM3p4BSOA8shoEERS2jf3PbhBDd2X+SDNqdmwnofNP0ntI9sEEqIMH
vMqOemGf6U95HNLj8B8KF5MEWB7y/yTUoCaF4uLaKQ5Qz623pWAbAnf7BeLra1f5
zpZyTOGWqkDZQmfcaanrWc7h9dc=

---End - This line not part of the certificate request---

Redisplay enrollment request? [yes/no]: no

```

### Radius DTLS: 加载证书(证书模板: QYT Web服务器)
```shell
CSR3(config)#crypto pki import DTLS certificate
% The IP address in the certificate is 202.100.3.1


Enter the base 64 encoded certificate.
End with a blank line or the word "quit" on a line by itself

-----BEGIN CERTIFICATE-----
MIIFfjCCBGagAwIBAgITEQAAABbPVY3m0Lh4MgAAAAAAFjANBgkqhkiG9w0BAQsF
ADBJMRMwEQYKCZImiZPyLGQBGRYDY29tMRYwFAYKCZImiZPyLGQBGRYGcXl0YW5n
MRowGAYDVQQDExFxeXRhbmctV0lOMjAxOS1DQTAeFw0yMzExMDEwMjM1MThaFw0y
NTEwMzEwMjM1MThaMHwxGjAYBgkqhkiG9w0BCQgTCzIwMi4xMDAuMy4xMR8wHQYJ
KoZIhvcNAQkCExBjOGt2My5xeXRhbmcuY29tMQ8wDQYDVQQKEwZxeXRhbmcxETAP
BgNVBAsTCHF5dGFuZ2JqMRkwFwYDVQQDExBjOGt2My5xeXRhbmcuY29tMIIBIjAN
BgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyZPQmkw/bY9sWJl+ThAQqpA6W7mh
m9SWtprO4PkVIwKdXjl5x0x4/FrwmrihCpXDdo9rW+HLPj5sFXg3Ur9RsEaxWms9
tFEzehFjSKtefvHbAryI0cFrpUNaQUkUf3ph8ZDPJNT/ENljT00IB37OCwAAxFxR
x7IxWeC+WlFexjL510lW9BTguzV58eq+LX20k5uBO0bdbpLVYjWMri+zx7vAO+al
s/IRzEUewm9vkV048ddrhtqyAxXGrs5hZzCdTE6tEYHOuLYBBhkmdNXb0hihmBdl
wpZsq6dlRDY8Z6qhGU8pHGmUvS3q0vUlrFKN3ONfSOmdcIvVFHd4Q1uUZQIDAQAB
o4ICKjCCAiYwDgYDVR0PAQH/BAQDAgWgMB0GA1UdDgQWBBStwi5OesNFlspxctna
mq+cKn48MTAfBgNVHSMEGDAWgBRQUvvQ0ga/i6hJ2yadJfM/mdgcgDCBzgYDVR0f
BIHGMIHDMIHAoIG9oIG6hoG3bGRhcDovLy9DTj1xeXRhbmctV0lOMjAxOS1DQSxD
Tj1XSU4yMDE5LENOPUNEUCxDTj1QdWJsaWMlMjBLZXklMjBTZXJ2aWNlcyxDTj1T
ZXJ2aWNlcyxDTj1Db25maWd1cmF0aW9uLERDPXF5dGFuZyxEQz1jb20/Y2VydGlm
aWNhdGVSZXZvY2F0aW9uTGlzdD9iYXNlP29iamVjdENsYXNzPWNSTERpc3RyaWJ1
dGlvblBvaW50MIHCBggrBgEFBQcBAQSBtTCBsjCBrwYIKwYBBQUHMAKGgaJsZGFw
Oi8vL0NOPXF5dGFuZy1XSU4yMDE5LUNBLENOPUFJQSxDTj1QdWJsaWMlMjBLZXkl
MjBTZXJ2aWNlcyxDTj1TZXJ2aWNlcyxDTj1Db25maWd1cmF0aW9uLERDPXF5dGFu
ZyxEQz1jb20/Y0FDZXJ0aWZpY2F0ZT9iYXNlP29iamVjdENsYXNzPWNlcnRpZmlj
YXRpb25BdXRob3JpdHkwKQYJKwYBBAGCNxQCBBweGgBPAGYAZgBsAGkAbgBlAFIA
bwB1AHQAZQByMBMGA1UdJQQMMAoGCCsGAQUFBwMCMA0GCSqGSIb3DQEBCwUAA4IB
AQBfbMPeGGNIaME2Iymdl3eb6u68gGTYP2s/VBhObj2/vaoGfg8kNn6SriEXCBEe
HBz6eDMKcq3Mk707fFfKrWYdDKOt9LkiS92LiOJXvM/WC150QSgZyxT9qyvhUdMh
X+k5jC7dHxta0m0SkVc3PufdFb8RbYx68Ls5DxMXZhZzdjhIsMDfhCNO7vClwFPc
ANcmG3Dp39SkP+vIadG73wkg9/7OuDsuIUIVUk4IGM8p1BHzug5lGa7yI7JTyV/E
fJx/RZXCiQt8TIa8nVfFWY6UU1ZLiAWBom+qnNOKWqzAL72RpAKXHk8bZLHxKvuh
E73M/gOXg4BgJzhKjLVBmAeC
-----END CERTIFICATE-----

% Router Certificate successfully imported

```

### Radius DTLS: 查看证书
```shell
CSR3#show crypto pki certificates DTLS
Certificate
  Status: Available
  Certificate Serial Number (hex): 1100000016CF558DE6D0B87832000000000016
  Certificate Usage: General Purpose
  Issuer:
    cn=qytang-WIN2019-CA
    dc=qytang
    dc=com
  Subject:
    Name: c8kv3.qytang.com
    IP Address: 202.100.3.1
    cn=c8kv3.qytang.com
    ou=qytangbj
    o=qytang
    hostname=c8kv3.qytang.com
    ipaddress=202.100.3.1
  CRL Distribution Points:
    ldap:///CN=qytang-WIN2019-CA,CN=WIN2019,CN=CDP,CN=Public%20Key%20Services,CN=Services,CN=Configuration,DC=qytang,DC=com?certificateRevocationList?base?objectClass=cRLDistributionPoint
  Validity Date:
    start date: 10:35:18 GMT Nov 1 2023
    end   date: 10:35:18 GMT Oct 31 2025
  Associated Trustpoints: DTLS

CA Certificate
  Status: Available
  Certificate Serial Number (hex): 3EEC76FB95DE8EAA4F8BA62964A87D98
  Certificate Usage: Signature
  Issuer:
    cn=qytang-WIN2019-CA
    dc=qytang
    dc=com
  Subject:
    cn=qytang-WIN2019-CA
    dc=qytang
    dc=com
  Validity Date:
    start date: 15:49:05 GMT Oct 30 2023
    end   date: 15:59:04 GMT Oct 30 2028
  Associated Trustpoints: DTLS

```


### --------- 申请IKEv2证书(证书模板: QYT IPSec(脱机申请)) ----------
### IKEv2证书: 加载微软根证书
```shell
CSR3(config)#crypto pki import CA certificate

Enter the base 64 encoded certificate.
End with a blank line or the word "quit" on a line by itself

-----BEGIN CERTIFICATE-----
MIIFvzCCBKegAwIBAgITEQAAABc5VIgPFa15QQAAAAAAFzANBgkqhkiG9w0BAQsF
ADBJMRMwEQYKCZImiZPyLGQBGRYDY29tMRYwFAYKCZImiZPyLGQBGRYGcXl0YW5n
MRowGAYDVQQDExFxeXRhbmctV0lOMjAxOS1DQTAeFw0yMzExMDEwMjQyMDRaFw0y
NTEwMzEwMjQyMDRaMGAxHzAdBgkqhkiG9w0BCQITEGM4a3YzLnF5dGFuZy5jb20x
DzANBgNVBAoTBnF5dGFuZzERMA8GA1UECxMIcXl0YW5nYmoxGTAXBgNVBAMTEGM4
a3YzLnF5dGFuZy5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC8
h1eLJJOUH7rO3eeIwgdEwysSu8PBveFDZPtj6SJp8ysWvzdJ2+6oqwTwtvfTYi7S
6lvuJe8HlYJBR6237obqY/2dl4TwPTR3DRAOdiP3Mb9SYuiMQiYbq6iXaAD5b07/
ZKnTrolIDNBd6EzRQTw85c9WTVRLBcUhIMoEljuE0pkM/xujqdeEUvm1nJbXRwQp
w/rWgMuhMlIjff0wxV6ZeDB0u6X8/uI89LqpIrXYFoJmg6RA3UlteMJ9bc6mDpWX
9RUsN5j032T8Pn51k4BjK7wP454Tone5C/qoLOziC+RUFSTWT+WKd20Mqnyk1qCQ
nC/9mTsxeZiTYwDdGdRBAgMBAAGjggKHMIICgzAOBgNVHQ8BAf8EBAMCBaAwJwYD
VR0lBCAwHgYIKwYBBQUHAwIGCCsGAQUFBwMBBggrBgEFBQgCAjAdBgNVHQ4EFgQU
ohuCslRRpcIJRSipPl2CBH24yyQwHwYDVR0jBBgwFoAUUFL70NIGv4uoSdsmnSXz
P5nYHIAwgc4GA1UdHwSBxjCBwzCBwKCBvaCBuoaBt2xkYXA6Ly8vQ049cXl0YW5n
LVdJTjIwMTktQ0EsQ049V0lOMjAxOSxDTj1DRFAsQ049UHVibGljJTIwS2V5JTIw
U2VydmljZXMsQ049U2VydmljZXMsQ049Q29uZmlndXJhdGlvbixEQz1xeXRhbmcs
REM9Y29tP2NlcnRpZmljYXRlUmV2b2NhdGlvbkxpc3Q/YmFzZT9vYmplY3RDbGFz
cz1jUkxEaXN0cmlidXRpb25Qb2ludDCBwgYIKwYBBQUHAQEEgbUwgbIwga8GCCsG
AQUFBzAChoGibGRhcDovLy9DTj1xeXRhbmctV0lOMjAxOS1DQSxDTj1BSUEsQ049
UHVibGljJTIwS2V5JTIwU2VydmljZXMsQ049U2VydmljZXMsQ049Q29uZmlndXJh
dGlvbixEQz1xeXRhbmcsREM9Y29tP2NBQ2VydGlmaWNhdGU/YmFzZT9vYmplY3RD
bGFzcz1jZXJ0aWZpY2F0aW9uQXV0aG9yaXR5MD0GCSsGAQQBgjcVBwQwMC4GJisG
AQQBgjcVCIXe+AGGgbx4gZGbMoSdwGWHo59ZLYGztFGCreonAgFkAgEDMDMGCSsG
AQQBgjcVCgQmMCQwCgYIKwYBBQUHAwIwCgYIKwYBBQUHAwEwCgYIKwYBBQUIAgIw
DQYJKoZIhvcNAQELBQADggEBAAh6zL+m7fKdHky9eL6sDCxwng4uevGVCIMQ0Nrm
q3Y8u2cRpCeWGriEzVRC1HcHUP8Hgr9w5sYFOz/bgrjHgtMnDZ3h1E+JDGqdf+LP
6MCSZ0KP0MUx1EZGQLatuqVr8rfwWRa368pV4bpwXgeQoC7q9lMU7yo7a6xGOQRW
EyMk/kgIHfKl58r0JqisxmNIMSLtXkKv7FpP09KsIF+EoIG5zeFyEMfhKu49T0dZ
BORHF63ExlveYlkmXQxv6Ve9DgSvVLrRgk6eUSm01hkZro0MaYFiAuCHeHSy5koD
DRcesovRCaW0C8XtkKl4ttTHAam6wobB/s1FLOCeRBZlbwo=
-----END CERTIFICATE-----

% Router Certificate successfully imported
```


### IKEv2证书: 产生证书申请 
```shell
CSR3(config)#crypto pki enroll CA
% Start certificate enrollment ..

% The subject name in the certificate will include: cn=c8kv3.qytang.com, ou=qytangbj, o=qytang
% The subject name in the certificate will include: c8kv3.qytang.com
% Include the router serial number in the subject name? [yes/no]: no
% Include an IP address in the subject name? [no]: no
Display Certificate Request to terminal? [yes/no]: yes
Certificate Request follows:

MIIC2zCCAcMCAQAwYDEPMA0GA1UEChMGcXl0YW5nMREwDwYDVQQLEwhxeXRhbmdi
ajEZMBcGA1UEAxMQYzhrdjMucXl0YW5nLmNvbTEfMB0GCSqGSIb3DQEJAhYQYzhr
djMucXl0YW5nLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALyH
V4skk5Qfus7d54jCB0TDKxK7w8G94UNk+2PpImnzKxa/N0nb7qirBPC299NiLtLq
W+4l7weVgkFHrbfuhupj/Z2XhPA9NHcNEA52I/cxv1Ji6IxCJhurqJdoAPlvTv9k
qdOuiUgM0F3oTNFBPDzlz1ZNVEsFxSEgygSWO4TSmQz/G6Op14RS+bWcltdHBCnD
+taAy6EyUiN9/TDFXpl4MHS7pfz+4jz0uqkitdgWgmaDpEDdSW14wn1tzqYOlZf1
FSw3mPTfZPw+fnWTgGMrvA/jnhOid7kL+qgs7OIL5FQVJNZP5Yp3bQyqfKTWoJCc
L/2ZOzF5mJNjAN0Z1EECAwEAAaA2MDQGCSqGSIb3DQEJDjEnMCUwDgYDVR0PAQH/
BAQDAgWgMBMGA1UdJQQMMAoGCCsGAQUFBwMBMA0GCSqGSIb3DQEBBQUAA4IBAQB6
EGK+uVhaS7xtm7NTXMlWwRlz0z1+YSNMYICSTdeVsjBWv8NNawxQ+S3pGVaB/D1F
sy1n67eUMkIq6dVbNO8uyaK5FbShnqZrOgavhtQHV+FZBTvxqNj7mHDF6peKawO4
6dESjOrWopRF+FG97Rc7gmAM0Av0r8dDdtLBUKPt9Xyfaj53GV/s66t8MPAnzTRR
pBsGrjWCjD/k7BiBcHdi4242DQC3pJz4KmyIG/W3gMTHQ9GiTAJUCP1ekzyNXbFN
S3z+pL1TuRC9J7kdef/5TU3mqg8q6PKMhNiQM40rGOIpEjc0+LiaRVlsKoyDMk3O
uBbw0e47ZVv6YNrYjtX8

---End - This line not part of the certificate request---

Redisplay enrollment request? [yes/no]: no

```

### IKEv2证书: 加载证书(证书模板: QYT IPSec(脱机申请))
```shell
CSR3(config)#crypto pki import CA certificate

Enter the base 64 encoded certificate.
End with a blank line or the word "quit" on a line by itself

-----BEGIN CERTIFICATE-----
MIIFvzCCBKegAwIBAgITEQAAABc5VIgPFa15QQAAAAAAFzANBgkqhkiG9w0BAQsF
ADBJMRMwEQYKCZImiZPyLGQBGRYDY29tMRYwFAYKCZImiZPyLGQBGRYGcXl0YW5n
MRowGAYDVQQDExFxeXRhbmctV0lOMjAxOS1DQTAeFw0yMzExMDEwMjQyMDRaFw0y
NTEwMzEwMjQyMDRaMGAxHzAdBgkqhkiG9w0BCQITEGM4a3YzLnF5dGFuZy5jb20x
DzANBgNVBAoTBnF5dGFuZzERMA8GA1UECxMIcXl0YW5nYmoxGTAXBgNVBAMTEGM4
a3YzLnF5dGFuZy5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC8
h1eLJJOUH7rO3eeIwgdEwysSu8PBveFDZPtj6SJp8ysWvzdJ2+6oqwTwtvfTYi7S
6lvuJe8HlYJBR6237obqY/2dl4TwPTR3DRAOdiP3Mb9SYuiMQiYbq6iXaAD5b07/
ZKnTrolIDNBd6EzRQTw85c9WTVRLBcUhIMoEljuE0pkM/xujqdeEUvm1nJbXRwQp
w/rWgMuhMlIjff0wxV6ZeDB0u6X8/uI89LqpIrXYFoJmg6RA3UlteMJ9bc6mDpWX
9RUsN5j032T8Pn51k4BjK7wP454Tone5C/qoLOziC+RUFSTWT+WKd20Mqnyk1qCQ
nC/9mTsxeZiTYwDdGdRBAgMBAAGjggKHMIICgzAOBgNVHQ8BAf8EBAMCBaAwJwYD
VR0lBCAwHgYIKwYBBQUHAwIGCCsGAQUFBwMBBggrBgEFBQgCAjAdBgNVHQ4EFgQU
ohuCslRRpcIJRSipPl2CBH24yyQwHwYDVR0jBBgwFoAUUFL70NIGv4uoSdsmnSXz
P5nYHIAwgc4GA1UdHwSBxjCBwzCBwKCBvaCBuoaBt2xkYXA6Ly8vQ049cXl0YW5n
LVdJTjIwMTktQ0EsQ049V0lOMjAxOSxDTj1DRFAsQ049UHVibGljJTIwS2V5JTIw
U2VydmljZXMsQ049U2VydmljZXMsQ049Q29uZmlndXJhdGlvbixEQz1xeXRhbmcs
REM9Y29tP2NlcnRpZmljYXRlUmV2b2NhdGlvbkxpc3Q/YmFzZT9vYmplY3RDbGFz
cz1jUkxEaXN0cmlidXRpb25Qb2ludDCBwgYIKwYBBQUHAQEEgbUwgbIwga8GCCsG
AQUFBzAChoGibGRhcDovLy9DTj1xeXRhbmctV0lOMjAxOS1DQSxDTj1BSUEsQ049
UHVibGljJTIwS2V5JTIwU2VydmljZXMsQ049U2VydmljZXMsQ049Q29uZmlndXJh
dGlvbixEQz1xeXRhbmcsREM9Y29tP2NBQ2VydGlmaWNhdGU/YmFzZT9vYmplY3RD
bGFzcz1jZXJ0aWZpY2F0aW9uQXV0aG9yaXR5MD0GCSsGAQQBgjcVBwQwMC4GJisG
AQQBgjcVCIXe+AGGgbx4gZGbMoSdwGWHo59ZLYGztFGCreonAgFkAgEDMDMGCSsG
AQQBgjcVCgQmMCQwCgYIKwYBBQUHAwIwCgYIKwYBBQUHAwEwCgYIKwYBBQUIAgIw
DQYJKoZIhvcNAQELBQADggEBAAh6zL+m7fKdHky9eL6sDCxwng4uevGVCIMQ0Nrm
q3Y8u2cRpCeWGriEzVRC1HcHUP8Hgr9w5sYFOz/bgrjHgtMnDZ3h1E+JDGqdf+LP
6MCSZ0KP0MUx1EZGQLatuqVr8rfwWRa368pV4bpwXgeQoC7q9lMU7yo7a6xGOQRW
EyMk/kgIHfKl58r0JqisxmNIMSLtXkKv7FpP09KsIF+EoIG5zeFyEMfhKu49T0dZ
BORHF63ExlveYlkmXQxv6Ve9DgSvVLrRgk6eUSm01hkZro0MaYFiAuCHeHSy5koD
DRcesovRCaW0C8XtkKl4ttTHAam6wobB/s1FLOCeRBZlbwo=
-----END CERTIFICATE-----

% Router Certificate successfully imported

```

### IKEv2证书: 查看证书状态, 使用verbose查看证书用途(证书模板: QYT IPSec(脱机申请))
```shell
CSR3#show crypto pki certificates verbose CA
Certificate
  Status: Available
  Version: 3
  Certificate Serial Number (hex): 11000000173954880F15AD7941000000000017
  Certificate Usage: General Purpose
  Issuer:
    cn=qytang-WIN2019-CA
    dc=qytang
    dc=com
  Subject:
    Name: c8kv3.qytang.com
    cn=c8kv3.qytang.com
    ou=qytangbj
    o=qytang
    hostname=c8kv3.qytang.com
  CRL Distribution Points:
    ldap:///CN=qytang-WIN2019-CA,CN=WIN2019,CN=CDP,CN=Public%20Key%20Services,CN=Services,CN=Configuration,DC=qytang,DC=com?certificateRevocationList?base?objectClass=cRLDistributionPoint
  Validity Date:
    start date: 10:42:04 GMT Nov 1 2023
    end   date: 10:42:04 GMT Oct 31 2025
  Subject Key Info:
    Public Key Algorithm: rsaEncryption
    RSA Public Key: (2048 bit)
  Signature Algorithm: SHA256 with RSA Encryption
  Fingerprint MD5: D9ADC3A9 1AFF1495 62D479AA FFDDAB63
  Fingerprint SHA1: 757E0A63 B55BD739 DA75BF6E D229E1EC 1F23D283
  X509v3 extensions:
    X509v3 Key Usage: A0000000
      Digital Signature
      Key Encipherment
    X509v3 Subject Key ID: A21B82B2 5451A5C2 094528A9 3E5D8204 7DB8CB24
    X509v3 Authority Key ID: 5052FBD0 D206BF8B A849DB26 9D25F33F 99D81C80
    Authority Info Access:
        CA ISSUERS: ldap:///CN=qytang-WIN2019-CA,CN=AIA,CN=Public%20Key%20Services,CN=Services,CN=Configuration,DC=qytang,DC=com?cACertificate?base?objectClass=certificationAuthority
    Extended Key Usage:
        1.3.6.1.5.5.8.2.2
        Server Auth   ###-----严重关注-----
        Client Auth   ###-----严重关注-----
  Associated Trustpoints: CA
  Key Label: c8kv3.qytang.com

CA Certificate
  Status: Available
  Version: 3
  Certificate Serial Number (hex): 3EEC76FB95DE8EAA4F8BA62964A87D98
  Certificate Usage: Signature
  Issuer:
    cn=qytang-WIN2019-CA
    dc=qytang
    dc=com
  Subject:
    cn=qytang-WIN2019-CA
    dc=qytang
    dc=com
  Validity Date:
    start date: 15:49:05 GMT Oct 30 2023
    end   date: 15:59:04 GMT Oct 30 2028
  Subject Key Info:
    Public Key Algorithm: rsaEncryption
    RSA Public Key: (2048 bit)
  Signature Algorithm: SHA256 with RSA Encryption
  Fingerprint MD5: AE7B21B0 3019A3F3 363D140A E322B988
  Fingerprint SHA1: 19E61C59 1FA33FE3 7568155F D9ABE527 C8395A8B
  X509v3 extensions:
    X509v3 Key Usage: 86000000
      Digital Signature
      Key Cert Sign
      CRL Signature
    X509v3 Subject Key ID: 5052FBD0 D206BF8B A849DB26 9D25F33F 99D81C80
    X509v3 Basic Constraints:
        CA: TRUE
    Authority Info Access:
  Associated Trustpoints: CA DTLS

```