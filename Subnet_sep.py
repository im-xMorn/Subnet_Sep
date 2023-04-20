# 本脚本实现子网划分
import ipaddress
# new_prefix 为 子网掩码位数
list_sub = ipaddress.IPv4Network('192.168.1.0/24').subnets(new_prefix=27)
for i in list_sub:
    print(i)
    print('网络地址:',i[0],'广播地址:',i[31])
    # 32-24 = 8 个子网 网络位向主机位借3位 24+3=27 算出主机位 8-3=5 2^5=32-1(网络地址)
