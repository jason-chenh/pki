### C8Kv2上的静态转换
```shell
interface GigabitEthernet1
 ip address 202.100.2.1 255.255.255.0
 ip nat outside
!
interface GigabitEthernet2
 ip address 10.1.1.254 255.255.255.0
 ip nat inside
!
ip nat inside source static 10.1.1.1 202.100.2.11
```

### 需要提前配置DNS映射
| 域名               | 类型  | IP地址         |
|------------------|-----|--------------|
| nginix.dcloud.cisco.com | A记录 | 202.100.2.11 |
