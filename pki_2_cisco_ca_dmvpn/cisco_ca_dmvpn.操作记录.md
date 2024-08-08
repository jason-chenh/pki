### 需要提前配置DNS映射
| 域名               | 类型  | IP地址        |
|------------------|-----|-------------|
| c8kv1.qytang.com | A记录 | 202.100.1.1 |
| c8kv2.qytang.com | A记录 | 202.100.2.1 |
| c8kv3.qytang.com | A记录 | 202.100.3.1 |

#### DNS转发器设置为: 223.5.5.5

### 基础配置(所有路由器)

```shell
ip domain name qytang.com
!
ip name-server 202.100.1.100
ip name-server 198.18.133.1
!
ip http server
!
clock timezone GMT +8
!
ntp server ntp.aliyun.com
ntp server cn.ntp.org.cn
ntp server edu.ntp.org.cn
ntp server ntp.ntsc.ac.cn

```

### 一定要等待NTP同步完成后再进行下面的操作(所有路由器)

```shell
C8Kv1#show ntp status
Clock is synchronized, stratum 2, reference is 202.118.1.81
nominal freq is 250.0000 Hz, actual freq is 249.9980 Hz, precision is 2**10
ntp uptime is 162400 (1/100 of seconds), resolution is 4016
reference time is E8E05A76.0F1A9FE8 (10:35:34.059 GMT Mon Oct 23 2023)
clock offset is -0.4780 msec, root delay is 36.00 msec
root dispersion is 19.41 msec, peer dispersion is 3.68 msec
loopfilter state is 'CTRL' (Normal Controlled Loop), drift is 0.000007810 s/s
system poll interval is 256, last update was 555 sec ago.

```
### C8Kv1产生CA的RSA密钥对
```shell
crypto key generate rsa label CA-KEY modulus 2048

crypto pki trustpoint CA
 rsakeypair CA-KEY

 PKI的server 要使用你自己的key,先需要创建一个trustpoint 引用之前创建的key:CA-KEY
 Trustpoint的名字和pki server 的名字也要一致
```

### 三台路由器产生DMVPN的RSA密钥对
```shell
crypto key generate rsa label DMVPN modulus 2048

```

### C8Kv1配置PKI服务器

```shell
crypto pki server CA
 database level complete
 database archive pkcs12 password Cisc0123
 issuer-name cn=dcloud.cisco.com, ou=cisco
 lifetime certificate 730
 lifetime ca-certificate 3650
 no shutdown

```
### C8Kv1 激活CA服务器，产生root 证书
```shell
C8Kv1(config)#crypto pki server CA
C8Kv1(cs-server)# database level complete
C8Kv1(cs-server)# database archive pkcs12 password Cisc0123
C8Kv1(cs-server)# issuer-name cn=ca.qytang.com, ou=qytang
C8Kv1(cs-server)# lifetime certificate 730
C8Kv1(cs-server)# lifetime ca-certificate 3650
C8Kv1(cs-server)#no shutdown
%Some server settings cannot be changed after CA certificate generation.

% Certificate Server enabled.


C8Kv1#show crypto pki server
Certificate Server CA:
    Status: enabled
    State: enabled
    Server's configuration is locked  (enter "shut" to unlock it)
    Issuer name: cn=ca.qytang.com, ou=qytang
    CA cert fingerprint: 779DB914 822A6E71 33EF87A9 9684D5EB
    Granting mode is: manual
    Last certificate issued serial number (hex): 1
    CA certificate expiration timer: 16:23:23 GMT Oct 29 2033
    CRL NextUpdate timer: 22:23:26 GMT Nov 1 2023
    Current primary storage dir: nvram:
    Database Level: Complete - all issued certs written as <serialnum>.cer

```

### C8Kv1配置PKI Trustpoint（认证服务器，谁给你颁发证书）

```shell
crypto pki trustpoint DMVPN
 enrollment url http://198.18.133.212:80
 fqdn  csr.dcloud.cisco.com
 ip-address  198.18.133.212
 subject-name cn=csr.dcloud.cisco.com, ou=cisco
 revocation-check crl
 rsakeypair DMVPN

```

### C8Kv2配置PKI Trustpoint

```shell
crypto pki trustpoint DMVPN
 enrollment url http://202.100.1.1:80
 fqdn c8kv2.qytang.com
 ip-address 202.100.2.1
 subject-name cn=c8kv2.qytang.com, ou=qytang
 revocation-check crl
 rsakeypair DMVPN
 
```

### C8Kv3配置PKI Trustpoint

```shell
crypto pki trustpoint DMVPN
 enrollment url http://202.100.1.1:80
 fqdn c8kv3.qytang.com
 ip-address 202.100.3.1
 subject-name cn=c8kv3.qytang.com, ou=qytang
 revocation-check crl
 rsakeypair DMVPN
 
```

### 获取根证书, 验证根证书服务器(所有路由器)

```shell
C8Kv1(config)#crypto pki authenticate DMVPN
Certificate has the following attributes:
       Fingerprint MD5: 779DB914 822A6E71 33EF87A9 9684D5EB
      Fingerprint SHA1: F1046684 E63135A6 576DB614 4EE43F23 06EC5AB0

% Do you accept this certificate? [yes/no]: yes
Trustpoint CA certificate accepted.

```

### 申请个人证书(所有路由器)

```shell
C8Kv1(config)#crypto pki enroll DMVPN
%
% Start certificate enrollment ..
% Create a challenge password. You will need to verbally provide this
   password to the CA Administrator in order to revoke your certificate.
   For security reasons your password will not be saved in the configuration.
   Please make a note of it.

Password:
Nov  1 08:30:19.166: %PKI-6-CERT_ENROLL_MANUAL: Manual enrollment for trustpoint DMVPN
Re-enter password:

% The subject name in the certificate will include: cn=c8kv1.qytang.com, ou=qytang
% The subject name in the certificate will include: c8kv1.qytang.com
% Include the router serial number in the subject name? [yes/no]: no
% The IP address in the certificate is 202.100.1.1

Request certificate from CA? [yes/no]: yes
% Certificate request sent to Certificate Authority
% The 'show crypto pki certificate verbose DMVPN' commandwill show the fingerprint.

CSR1(config)#
Nov  1 08:30:28.044: %PKI-6-CSR_FINGERPRINT:
                      CSR Fingerprint MD5 : 994A7897CFEA32B740E7C81AB9202A80
                      CSR Fingerprint SHA1: 98BFE789AF867FFB040984A02D883AB2BF77E528
Nov  1 08:30:28.044: CRYPTO_PKI:  Certificate Request Fingerprint MD5: 994A7897 CFEA32B7 40E7C81A B9202A80
Nov  1 08:30:28.046: CRYPTO_PKI:  Certificate Request Fingerprint SHA1: 98BFE789 AF867FFB 040984A0 2D883AB2 BF77E528

```
### CA服务器查看请求的证书
```shell
CSR1#show crypto pki server CA requests
Enrollment Request Database:

Subordinate CA certificate requests:
ReqID  State      Fingerprint                      SubjectName
--------------------------------------------------------------

RA certificate requests:
ReqID  State      Fingerprint                      SubjectName
--------------------------------------------------------------

Router certificates requests:
ReqID  State      Fingerprint                      SubjectName
--------------------------------------------------------------
1      pending    994A7897CFEA32B740E7C81AB9202A80 ipaddress=202.100.1.1+hostname=c8kv1.qytang.com,cn=c8kv1.qytang.com,ou=qytang

```

### CA服务器颁发证书
```shell
C8Kv1#crypto pki server CA grant 1

C8Kv1#terminal monitor

C8Kv1#
Nov  1 08:32:28.698: %PKI-6-CERT_INSTALL: An ID certificate has been installed under
                      Trustpoint   : DMVPN
                      Issuer-name  : cn=ca.qytang.com,ou=qytang
                      Subject-name : ipaddress=202.100.1.1+hostname=c8kv1.qytang.com,cn=c8kv1.qytang.com,ou=qytang
                      Serial-number: 02
                      End-date     : 2025-10-31T16:32:07Z

```


### 查看证书(所有路由器)
    
```shell
C8Kv1#show crypto pki certificates DMVPN
Certificate
  Status: Available
  Certificate Serial Number (hex): 02
  Certificate Usage: General Purpose
  Issuer:
    cn=ca.qytang.com
    ou=qytang
  Subject:
    Name: c8kv1.qytang.com
    IP Address: 202.100.1.1
    ipaddress=202.100.1.1+hostname=c8kv1.qytang.com
    cn=c8kv1.qytang.com
    ou=qytang
  Validity Date:
    start date: 10:42:15 GMT Oct 30 2023
    end   date: 10:42:15 GMT Oct 29 2025
  Associated Trustpoints: DMVPN

CA Certificate
  Status: Available
  Certificate Serial Number (hex): 01
  Certificate Usage: Signature
  Issuer:
    cn=ca.qytang.com
    ou=qytang
  Subject:
    cn=ca.qytang.com
    ou=qytang
  Validity Date:
    start date: 10:38:12 GMT Oct 30 2023
    end   date: 10:38:12 GMT Oct 27 2033
  Associated Trustpoints: DMVPN CA
```

### 配置IKE(所有路由器)

```shell
crypto pki certificate map ikev1-cert-map 10
 subject-name co ou = qytang
!
crypto isakmp policy 10
 encryption aes 
 hash sha256
 group 14
crypto isakmp profile ikev1-profile
   ca trust-point DMVPN
   match certificate ikev1-cert-map
!
crypto ipsec transform-set trans esp-aes 256 esp-sha256-hmac
 mode tunnel
!
crypto ipsec profile ipsec-profile
 set transform-set trans
 set isakmp-profile ikev1-profile

```

### 配置C8Kv1的DMVPN

```shell
interface Tunnel0
 ip address 172.16.1.1 255.255.255.0
 no ip redirects
 ip mtu 1400
 no ip split-horizon eigrp 100
 ip nhrp authentication cisco
 ip nhrp network-id 10
 ip nhrp redirect
 tunnel source GigabitEthernet1
 tunnel mode gre multipoint
 tunnel key 123456
 tunnel protection ipsec profile ipsec-profile
 
```

### 配置C8Kv2的DMVPN(出现过DNS缓存问题, 可以考虑"clear host all *")

```shell
interface Tunnel0
 ip address 172.16.1.2 255.255.255.0
 no ip redirects
 ip mtu 1400
 ip nhrp authentication cisco
 ip nhrp network-id 10
 ip nhrp nhs dynamic nbma c8kv1.qytang.com multicast
 ip nhrp redirect
 tunnel source GigabitEthernet1
 tunnel mode gre multipoint
 tunnel key 123456
 tunnel protection ipsec profile ipsec-profile
 
```

### 配置C8Kv3的DMVPN(出现过DNS缓存问题, 可以考虑"clear host all *")

```shell
interface Tunnel0
 ip address 172.16.1.3 255.255.255.0
 no ip redirects
 ip mtu 1400
 ip nhrp authentication cisco
 ip nhrp network-id 10
 ip nhrp nhs dynamic nbma c8kv1.qytang.com multicast
 ip nhrp redirect
 tunnel source GigabitEthernet1
 tunnel mode gre multipoint
 tunnel key 123456
 tunnel protection ipsec profile ipsec-profile
 
```

### 配置C8Kv1的EIGRP

```shell
interface Loopback0
 ip address 1.1.1.1 255.255.255.0
!
router eigrp 100
 network 1.1.1.0 0.0.0.255
 network 172.16.1.0 0.0.0.255

```

### 配置C8Kv2的EIGRP

```shell
router eigrp 100
 network 10.1.1.0 0.0.0.255
 network 172.16.1.0 0.0.0.255
 
```

### 配置C8Kv3的EIGRP

```shell
interface Loopback0
 ip address 3.3.3.3 255.255.255.0
!
router eigrp 100
 network 3.3.3.0 0.0.0.255
 network 172.16.1.0 0.0.0.255

```

### CA服务器(C8Kv1)吊销C8Kv3的证书(0x4)

```shell
C8Kv1#crypto pki server CA revoke 0x4
% Certificate 04 succesfully revoked.

```

### 但是C8Kv3 shutdown/no shutdown 隧道口依然能够正常建立IPSec

### 查看C8Kv1的吊销列表
```shell
C8Kv1#show crypto pki crls
CRL Issuer Name:
    cn=ca.qytang.com,ou=qytang
    LastUpdate: 10:38:13 GMT Oct 30 2023
    NextUpdate: 16:38:13 GMT Oct 30 2023

    CRL downloaded at: 10:49:43 GMT Oct 30 2023

    Retrieved from CRL Distribution Point:
      ** CDP Not Published - Retrieved via SCEP

 CRL DER is 370 bytes
 CRL is stored in parsed CRL cache


Parsed CRL cache current size is 370 bytes
Parsed CRL cache maximum size is 65536 bytes

```

### C8Kv1重新获取CRL列表

```shell
C8Kv1(config)#crypto pki crl request DMVPN

C8Kv1#show crypto pki crls
CRL Issuer Name:
    cn=ca.qytang.com,ou=qytang
    LastUpdate: 10:54:09 GMT Oct 30 2023
    NextUpdate: 16:54:09 GMT Oct 30 2023

    CRL downloaded at: 10:56:54 GMT Oct 30 2023

    Retrieved from CRL Distribution Point:
      ** CDP Not Published - Retrieved via SCEP

 CRL DER is 392 bytes
 CRL is stored in parsed CRL cache


Parsed CRL cache current size is 392 bytes
Parsed CRL cache maximum size is 65536 bytes

```

### 现在C8Kv3 shutdown/no shutdown 隧道口就无法正常建立了
```shell
C8Kv3#
Oct 30 02:58:01.948: %SYS-5-CONFIG_I: Configured from console by admin on vty0 (202.100.1.101)
Oct 30 02:58:05.963: %DMVPN-5-NHRP_NHS_DOWN: Tunnel0: Next Hop Server : (Tunnel: UNKNOWN NBMA: 38.127.0.128 ) for (Tunnel: 172.16.1.3 NBMA: 202.100.3.1) is DOWN, Reason: NHRP Registration Failure(NHRP: no error)
Oct 30 02:58:11.725: %DMVPN-5-NHRP_NHS_DOWN: Tunnel0: Next Hop Server : (Tunnel: UNKNOWN NBMA: 38.127.0.128 ) for (Tunnel: 172.16.1.3 NBMA: 202.100.3.1) is DOWN, Reason: NHRP Registration Failure(NHRP: no error)

```

### CA服务器(C8Kv1)切换到手动颁发证书
```shell
C8Kv1(config)#crypto pki server CA
C8Kv1(cs-server)#shutdown
Certificate server 'shut' event has been queued for processing.

C8Kv1(cs-server)#grant auto
%PKI-6-CS_GRANT_AUTO: All enrollment requests will be automatically granted.

C8Kv1(cs-server)#no shutdown
Certificate server 'no shut' event has been queued for processing.

C8Kv1#show crypto pki server CA
Certificate Server CA:
    Status: enabled
    State: enabled
    Server's configuration is locked  (enter "shut" to unlock it)
    Issuer name: cn=ca.qytang.com, ou=qytang
    CA cert fingerprint: 779DB914 822A6E71 33EF87A9 9684D5EB
    Granting mode is: auto
    Last certificate issued serial number (hex): 4
    CA certificate expiration timer: 16:23:23 GMT Oct 29 2033
    CRL NextUpdate timer: 22:53:06 GMT Nov 1 2023
    Current primary storage dir: nvram:
    Database Level: Complete - all issued certs written as <serialnum>.cer

```

### C8Kv3重新申请证书

```shell
C8Kv3(config)#crypto pki enroll DMVPN
Trustpoint DMVPN has already enrolled and has a router cert issued to it.
If you successfully re-enroll this trustpoint,the existing certificate will be replaced.

Do you want to continue with re-enrollment? [yes/no]: yes
%
% Start certificate enrollment ..
% Create a challenge password. You will need to verbally provide this
   password to the CA Administrator in order to revoke your certificate.
   For security reasons your password will not be saved in the configuration.
   Please make a note of it.

Password: [回车]
Re-enter password: [回车]

% The subject name in the certificate will include: cn=c8kv3.qytang.com, ou=qytang
% The subject name in the certificate will include: c8kv3.qytang.com
% Include the router serial number in the subject name? [yes/no]: no
% The IP address in the certificate is 202.100.3.1

Request certificate from CA? [yes/no]: yes
% Certificate request sent to Certificate Authority
% The 'show crypto pki certificate verbose DMVPN' commandwill show the fingerprint.

```

### 现在C8Kv3 shutdown/no shutdown 隧道口就可以正常建立了
