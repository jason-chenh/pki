### 基本网络与aaa线下保护
```shell
ip domain name qytang.com
!
ip name-server 202.100.1.100
!
ip http server
!
clock timezone GMT +8
!
ntp server ntp.aliyun.com
ntp server cn.ntp.org.cn
ntp server edu.ntp.org.cn
ntp server ntp.ntsc.ac.cn

aaa new-model

aaa authentication login noacs none
aaa authentication login vty local
aaa authorization exec vty local

line con 0
 login authentication noacs

line vty 0 15
 authorization exec vty
 login authentication vty

```

### DTLS Trust point(类型: 路由器(脱机申请))
```shell
crypto pki trustpoint DTLS
 enrollment terminal
 fqdn csr.dcloud.cisco.com
 ip-address 198.18.133.212
 subject-name cn=csr.dcloud.cisco.com,ou=cisco,o=dcloud
 subject-alt-name csr.dcloud.cisco.com
 revocation-check none
 rsakeypair DTLS 2048

```

### 配置DTLS的Radius
```shell
aaa group server radius dcloud-ise-group
 server name ise
aaa server radius dynamic-author
 client 198.18.133.27 dtls client-tp DTLS server-tp DTLS
radius server ise
 address fqdn ise.securitydemo.net
 dtls port 2083
 dtls trustpoint client DTLS
 dtls trustpoint server DTLS
 dtls match-server-identity hostname ise.securitydemo.net


```

### 配置IKEv2的Trust point(类型: QYT IPSec(脱机申请), 在原来模板之上增加 server auth)
```shell
crypto pki trustpoint CA_IPSec
enrollment terminal
 fqdn csr.dcloud.cisco.com
 ip-address 198.18.133.212
 subject-name cn=csr.dcloud.cisco.com,ou=cisco,o=dcloud
 subject-alt-name csr.dcloud.cisco.com
 revocation-check none
 rsakeypair csr.dcloud.cisco.com 2048
 eku request server-auth
 
```

### 双向证认证IPSec配置
```shell
ip local pool qytpool 123.1.1.100 123.1.1.200

aaa authorization network qytang-local-group-author-list local

crypto ikev2 authorization policy qytang-ikev2-author
 pool qytpool
 
crypto pki certificate map qytang-cert-map 10
 subject-name co cn = win10.qytang.com

crypto ikev2 proposal qytang-ikev2-proposal
 encryption aes-cbc-256
 integrity sha1
 group 2
!
crypto ikev2 policy qytang-ikev2-policy
 proposal qytang-ikev2-proposal
!
crypto ikev2 profile qytang-ikev2-profile
 match certificate qytang-cert-map
 identity local fqdn c8kv3.qytang.com
 authentication remote rsa-sig
 authentication local rsa-sig
 pki trustpoint CA
 aaa authorization group cert list qytang-local-group-author-list qytang-ikev2-author
 virtual-template 1
!
crypto ipsec transform-set qytang-ipsec-trans esp-3des esp-sha-hmac
 mode tunnel
!
crypto ipsec profile qytang-ipsec-profile
 set transform-set qytang-ipsec-trans
 set ikev2-profile qytang-ikev2-profile
!
interface Virtual-Template1 type tunnel
 ip unnumbered GigabitEthernet1
 tunnel mode ipsec ipv4
 tunnel protection ipsec profile qytang-ipsec-profile
!
interface Loopback0
 ip address 3.3.3.3 255.255.255.0

```
### 测试
```shell
WIN10 需要申请计算机证书

cn = win10.qytang.com

```

---

### EAP认证IPSec配置
```shell
ip local pool qytpool 123.1.1.100 123.1.1.200
!
crypto ikev2 proposal qytang-ikev2-proposal
 encryption aes-cbc-256
 integrity sha1
 group 2
!
crypto ikev2 policy qytang-ikev2-policy
 proposal qytang-ikev2-proposal
!
aaa authentication login qytang-eap-list group qytang-ise-group
aaa authorization network qytang-eap-list group qytang-ise-group
!
crypto ikev2 name-mangler qytang-name-mangler
 eap suffix delimiter @
!
crypto ikev2 profile qytang-ikev2-eap-profile
 match identity remote address 0.0.0.0
 authentication local rsa-sig
 authentication remote eap query-identity
 pki trustpoint CA
 aaa authentication eap qytang-eap-list
 aaa authorization group eap list qytang-eap-list name-mangler qytang-name-mangler
 virtual-template 2
!
crypto ipsec transform-set qytang-ipsec-eap-transform-set esp-aes 256 esp-sha-hmac
 mode tunnel
!
crypto ipsec profile qytang-ipsec-eap-profile
 set transform-set qytang-ipsec-eap-transform-set
 set ikev2-profile qytang-ikev2-eap-profile
!
interface Virtual-Template2 type tunnel
 ip unnumbered GigabitEthernet1
 tunnel mode ipsec ipv4
 tunnel protection ipsec profile qytang-ipsec-eap-profile

```

### 用户
```shell
用户名: win10user@win10group     密码: Cisc0123
用户名: win10group               密码: cisco         注意: 需要关闭密码复杂度要求
----------------------------------------------------------------------------

Authorization Profiles: win10group
cisco-av-pair = ipsec:addr-pool=qytpool
cisco-av-pair = ipsec:dns-servers=10.1.1.101

----------------------------------------------------------------------------
Authorized Policy:

InternalUser.Name         EQUALS    win10group
Results/Profiles                    win10group
```

### AAA测试
```shell
C8Kv3#test aaa group qytang-ise-group win10user@win10group Cisc0123 new
User successfully authenticated

USER ATTRIBUTES

username             0   "win10user@win10group"

C8Kv3#test aaa group qytang-ise-group win10group cisco new
User successfully authenticated

USER ATTRIBUTES

username             0   "win10group"
addr-pool            0   "qytpool"
dns-servers          0   "10.1.1.101"

```