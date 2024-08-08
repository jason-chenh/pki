### C8Kv1配置PKI Trustpoint

```shell
no crypto pki trustpoint DMVPN

 
```

### C8Kv2配置PKI Trustpoint

```shell
no crypto pki trustpoint DMVPN

crypto pki trustpoint DMVPN
 enrollment url http://ad-2016.dcloud.cisco.com/certsrv/mscep/mscep.dll
 fqdn csr.dcloud.cisco.com
 ip-address  198.18.133.212
 subject-name cn=csr.dcloud.cisco.com, ou=cisco
 revocation-check none
 rsakeypair DMVPN
 

 
```

### C8Kv3配置PKI Trustpoint

```shell
no crypto pki trustpoint DMVPN

crypto pki trustpoint DMVPN
 enrollment url http://win2019.qytang.com/certsrv/mscep/mscep.dll
 fqdn c8kv3.qytang.com
 ip-address 202.100.3.1
 subject-name cn=c8kv3.qytang.com, ou=qytang
 revocation-check none
 rsakeypair DMVPN
 
```
