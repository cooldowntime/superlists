配置新网站
==============
## 需要的包
* nginx
* Python 3.7
* virtualenv + pip
* Git
## Nginx虚拟主机
* 参考nginx.template.conf

## Systemd服务
* 参考gunicorn-upstart.template.conf

## 文件夹结构
/home/uername
    sites
        SITENAME
            database
	    source
	    static
	    virtualenv

