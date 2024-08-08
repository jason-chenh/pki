###问题: gitlab-runner无法注册到gitlab(企业内部证书)

### 把企业根证书"ca.pem" 拷贝到目录"/etc/pki/ca-trust/source/anchors/"
```shell
cp /pki2023/pki_4_linux_ca/linux_ca/cfssl_certs_and_keys/ca.pem /etc/pki/ca-trust/source/anchors/qytang.com.crt
update-ca-trust

```

### 注册gitlab-runner
```shell
[root@elasticsearch ~]# gitlab-runner register
Runtime platform                                    arch=amd64 os=linux pid=335000 revision=853330f9 version=16.5.0
Running in system-mode.

Enter the GitLab instance URL (for example, https://gitlab.com/):
https://gitlab.qytang.com/
Enter the registration token:
GR1348941_UaCPwjfpqwYEH6bEtx8
Enter a description for the runner:
[elasticsearch.qytang.com]: qyt_rocky
Enter tags for the runner (comma-separated):
qyt_rocky
Enter optional maintenance note for the runner:
qyt_rocky
WARNING: Support for registration tokens and runner parameters in the 'register' command has been deprecated in GitLab Runner 15.6 and will be replaced with support for authentication tokens. For more information, see https://docs.gitlab.com/ee/ci/runners/new_creation_workflow
Registering runner... succeeded                     runner=GR1348941_UaCPwjf
Enter an executor: docker-windows, shell, ssh, virtualbox, docker+machine, custom, docker, parallels, docker-autoscaler, instance, kubernetes:
docker
Enter the default Docker image (for example, ruby:2.7):
collinsctk/pki2023_test
Runner registered successfully. Feel free to start it, but if it's running already the config should be automatically reloaded!

Configuration (with the authentication token) was saved in "/etc/gitlab-runner/config.toml"

```

