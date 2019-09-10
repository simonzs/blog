### 1.通过ssh访问内部的其他端口的解决方案:

例如要访问: 通过22 访问 1111

ssh -D localhost:1080 ubuntu@***.com

https://chrome.google.com/webstore/detail/proxy-switchyomega/padekgcemlokbadohgkifijomclgjgif

proxy 配置 socket5 127.0.0.1:1080

启动配置， 访问远程主机的etho， 如: http://170.1.2.3:1111

完成

### 进入虚拟环境
source venv/bin/activate

https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/

### docker 

docker build -t app:v0.0.3 .

docker run -e HOST_IP=192.168.0.1 -e DATABASE_IP=10.11.1.1 app:v0.0.3
docker run -p 8080:80 -e HOST_IP=10.201.0.1 -e DATABASE_IP=10.201.0.1 app:v0.0.3

docker tag app:v0.0.3 registry.github.com:5000/app:v0.0.3

docker push  registry.github.com:1111/app:v0.0.3
