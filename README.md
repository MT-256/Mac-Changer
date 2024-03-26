# Mac_Changer

Tool designed to modify the MAC address in python

# What is a MAC address?

A MAC (Media Access Control) address is a unique identifier assigned to a specific network interface on a device, such as a computer, smartphone, printer, or any other device that connects to a network. This address is globally unique and is used to uniquely identify each device on a local network. The MAC address consists of 12 hexadecimal characters (0-9 and A-F), which are divided into six pairs separated by colons or hyphens, such as: 00:1A:2B:3C:4D:5E or 00-1A-2B-3C-4D-5E.

Each manufacturer of network devices is assigned a range of MAC addresses managed by the Institute of Electrical and Electronics Engineers (IEEE). The first three pairs of characters in a MAC address represent the manufacturer's unique identifier, while the last three pairs represent a unique identifier assigned by the manufacturer to the specific network interface of the device

# Usage 

To use the script, we must know two things: 1) Our network interface (eth0, enp0s3, enp0s17, ens33, etc), we know this by doing "ip a, ifconfig or ipconfig" and 2) The Mac that we want to change, is It will be the first 3 digits (xx:xx:xx:ff:ff:ff)

To see available mac addresses we use:

```
macchanger -l | grep "Samsung"
```

![Mac 1](https://github.com/MT-256/Mac-Changer/assets/127991386/28907e80-44f4-416a-802d-89d241131e56)

If we need to know our mac, we can do it with the following command:

```
macchanger -s enp0s3
```

We know that the mac was changed successfully if we are assigned another IP different from the one we previously had

```
python3 Mac_Changer.py -i enp0s3 -m 00:02:78:11:11:11
```

![image](https://github.com/MT-256/Mac-Changer/assets/127991386/9ef10b69-8558-4b02-b57c-2c7cb6a2eab4)


