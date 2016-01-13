#!/bin/bash
ip link set up dev enp0s25
ip addr add 10.10.10.1/24 dev enp0s25
sysctl net.ipv4.ip_forward=1
iptables -t nat -A POSTROUTING -o wlp3s0 -j MASQUERADE
iptables -A FORWARD -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i enp0s25 -o wlp3s0 -j ACCEPT
