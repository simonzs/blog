### 1.通过ssh访问内部的其他端口的解决方案:

例如要访问: 通过22 访问 1111

ssh -D localhost:1080 ubuntu@***.com

https://chrome.google.com/webstore/detail/proxy-switchyomega/padekgcemlokbadohgkifijomclgjgif

proxy 配置 socket5 127.0.0.1:1080

启动配置， 访问远程主机的etho， 如: http://170.1.2.3:1111

完成

### 进入虚拟环境
source venv/bin/activate
