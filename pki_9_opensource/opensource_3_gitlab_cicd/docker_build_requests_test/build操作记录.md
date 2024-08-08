### build操作记录
```shell
[root@elasticsearch docker_build_requests_test]# pwd
/pki2023/pki_9_opensource/opensource_3_gitlab_cicd/docker_build_requests_test

[root@elasticsearch docker_build_requests_test]# docker build -t collinsctk/pki2023_test .

[root@elasticsearch docker_build_requests_test]# docker login

[root@elasticsearch docker_build_requests_test]# docker push collinsctk/pki2023_test

```