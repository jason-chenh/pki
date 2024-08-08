### 吊销证书, 产生CRL
```shell
[root@elasticsearch cfssl_json]# pwd
/pki2023/pki_4_linux_ca/linux_ca/cfssl_json


[root@elasticsearch cfssl_json]# ls -an
~~~忽略其他~~~
-rw-r--r-- 1 0 0   47 Oct 30 07:35 revocation-list.txt

[root@elasticsearch cfssl_json]# cat revocation-list.txt
97933555654769875261133697086325916228451763952

cfssl gencrl revocation-list.txt \
../cfssl_certs_and_keys/ca.pem \
../cfssl_certs_and_keys/ca-key.pem | tee cloudcrl.crl
MIIC6jCB0zANBgkqhkiG9w0BAQsFADBSMQswCQYDVQQGEwJDTjEQMA4GA1UECBMHYmVpamluZzEQMA4GA1UEBxMHYmVpamluZzEPMA0GA1UEChMGcXl0YW5nMQ4wDAYDVQQDEwVxeXRjYRcNMjMxMDMwMTM0MzM5WhcNMjMxMTA2MTM0MzM5WjArMCkCFBEnfhWR/4V0+WNQaw25t8qJnwbwFxEyMzEwMzAwOTQzMzktMDQwMKAjMCEwHwYDVR0jBBgwFoAUXnr02NR4K8UUICmGS3X3MS+mhiIwDQYJKoZIhvcNAQELBQADggIBACSXq2vJ6GXDGNurerzreDS9X77rhOKsmUnkQhRgWxUC+2RKAf/mweD7RN70KFYWCsxIFlKu+YvTvHSDsxJ9IQK44aYhJu2UK4xfRweF3z9bX47ImfeUVl0NJ2mZLHp5FqjCybSATfyG3AiqzOdzXP/M3YoO9RvdU80sUV5vYEyeNnEY6MOxVdsCYMjaqJz4F4TZ8YfVNutOOLJIO6nifSV+TfH756nO/aCkySRwKOYVZuoITRLLBeONzgQUTwIcCLHsnx1yc4nz46tHbZLHN1MOY7W4Qgm3ayH2eX5PW8xH+KwasgTCo/OGwgg/vBg+KeYuZZHH+7JLGuP5L7hLFUAw3PTTK28g1VVZUsje2o2btFPcQMN6dPkq21Dgo4bm/QfHOXYyLRFlsLnctsWsh2fv4Ow0pndntHza21Ul2hxbICK3pRqG+ll4Nz/HkOnOqqwkJFQPYvjQDy054vooERO8YDkVF4itpZKOiF25Vj0OwMYM00sbUR7qSj9NJz9U1reT0/w4lPDljyuuA0Ttwq0E33FukmUhWQ84lvaTqLsLD88+yRMtZtRFXhkLC8jmnPH2vHNPiqEyrWGnE1zr24dYByr7Osc4zskUv6OttQ6NFDMJ4Olr3PIbs/nXllUSYDni6/v1rpXpuyO4cCgobxp99a0Qn3hkxGHx2/xfCr8Z

```

### 把产生的内容贴如到AD(域控)的"C:\inetpub\wwwroot\qytcrl.crl"

### 确认可以通过"http://win2019.qytang.com/qytcrl.crl"下载