### 基本配置, 时间非常重要
```shell
hostname asa
domain-name qytang.com
clock timezone GMT +8

dns domain-lookup outside
dns name-server 202.100.1.100

ntp server 202.100.1.1 source Outside prefer

http server enable 6443
http 0.0.0.0 0.0.0.0 Outside

```

### 产生RSA密钥对, 配置Trustpoint
```shell
crypto key generate rsa label SSLVPN modulus 2048

crypto ca trustpoint CA
 enrollment terminal
 fqdn asa.qytang.com
 subject-name cn=asa.qytang.com,ou=qytang,o=qytbj
 ip-address 202.100.3.10
 keypair SSLVPN
 validation-usage ssl-client
 
```

### 配置最终给客户授权的Group Policy
```shell
group-policy ssl-user-policy internal
group-policy ssl-user-policy attributes
	banner value welcome to qytang!

```

### 配置LDAP, 映射LDAP属性memberOf到Group Policy
### memberOf "CN=sslgroup,OU=sslvpn,DC=qytang,DC=com"
### Group Policy "ssl-user-policy"
```shell
ldap attribute-map qyt-ldap-map
  map-name  memberOf Group-Policy
  map-value memberOf CN=sslgroup,OU=sslvpn,DC=qytang,DC=com ssl-user-policy

aaa-server MSAD protocol ldap
aaa-server MSAD (Outside) host 202.100.1.100
	ldap-base-dn dc=qytang, dc=com
	ldap-login-dn cn=administrator, cn=users, dc=qytang, dc=com
	ldap-login-password Cisc0123
	ldap-naming-attribute sAMAccountName
	ldap-scope subtree
	server-type microsoft
	ldap-attribute-map qyt-ldap-map

```

### 配置Tunnel Group, 激活证书认证, 从证书CN中提取用户名, 再使用提取到的用户名到LDAP授权
```shell
tunnel-group sslvpn type remote-access
tunnel-group sslvpn general-attributes
 authorization-server-group MSAD
 username-from-certificate CN
 authorization-required
tunnel-group sslvpn webvpn-attributes
 authentication certificate
 
```

### 这个策略的主要任务: 通过证书属性找到Tunnel-Group, 默认就是用OU的名字来查找Tunnel Group
```shell
crypto ca certificate map qytang-cert-map 10
 subject-name attr ou co sslvpn
crypto ca certificate map qytang-cert-map 20

tunnel-group-map enable rules

```

### 激活SSLVPN, 证书匹配策略到Tunnel Group
```shell
webvpn
 enable Outside
 certificate-group-map qytang-cert-map 10 sslvpn
 certificate-group-map qytang-cert-map 20 DefaultWEBVPNGroup

```

### 在Outside接口激活SSLVPN的证书
```shell
ssl trust-point CA Outside

```

### 拨号成功后查看 vpn-sessiondb状态
### 关注点1: Group Policy : ssl-user-policy
### 关注点2: Tunnel Group : sslvpn
```shell
asa# show vpn-sessiondb webvpn

Session Type: WebVPN

Username     : ssluser                Index        : 2
Public IP    : 202.100.1.102
Protocol     : Clientless
License      : AnyConnect Premium
Encryption   : Clientless: (1)AES-GCM-256
Hashing      : Clientless: (1)SHA384
Bytes Tx     : 290386                 Bytes Rx     : 46494
Group Policy : ssl-user-policy        Tunnel Group : sslvpn
Login Time   : 10:03:11 GMT Wed Nov 1 2023
Duration     : 0h:00m:15s
Inactivity   : 0h:00m:00s
VLAN Mapping : N/A                    VLAN         : none
Audt Sess ID : 0a0103fe000020006541b1df
Security Grp : none

```