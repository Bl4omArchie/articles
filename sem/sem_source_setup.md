# Snort Easy Manual

Welcome to ESM. This document will guide through the installation of Snort and its configuration.


## Installation

### Pre-requistes

First of all, you have to install the following packages in your system.
```
apt install cmake libdaq-dev flex g++ hwloclibhwloc-dev libnuma-dev libluajit-5.1-dev libssl-dev libpcap-dev libpcre3-dev pkg-config zlib1g-dev
```


### Libdaq

Then you have to install the DAQ library, an abstraction layer for communicating with a data source (such as network interface).

```sh
git clone https://github.com/snort3/libdaq.git

cd libdaq
./bootstrap
./configure --prefix=/usr/local/lib/daq_s3
make -j $(nproc//2)
make install
```

**Note**: 
- `make -j $(nproc//2)` use half your processus for 'make install'

- Here the `--prefix=/usr/local/lib/daq_s3` is optional, if you want to keep the default location, don't specify anything and simply do : `./configure`.

If you choose a non-standard location, you must tell your system where to find the new shared libraries. 

Add a new file dedicated to libdaq into the dynamic linker:
```sh
echo /etc/ld.so.conf.d/libdaq3.conf > /you/path/to/libdaq/lib
``` 

And then, update the linker cache:
```sh
ld config
```

### Snort

Now that libdaq is installed, you can install Snort.

#### Default location
```sh
git clone https://github.com/snort3/snort3.git

./configure_cmake.sh
cd build
make -j $(nproc)
make install
```

#### Custom location

If you installed libdaq in a non-standard location, specify the correct path with `--with-daq-includes` and `--with-daq-libraries`.

Same for snort, if you want a custom location, specify the path at `--prefix`.
```sh
./configure_cmake.sh --prefix=/path/to/snort/ /
                     --with-daq-includes=/usr/local/lib/daq_s3/include/  /
                     --with-daq-libraries=/usr/local/lib/daq_s3/lib/
```

Verify if snort is installed correctly:
```sh
snort -V
```

or for custom location:
```sh
/path/to/snort/bin/snort -V
```

## Rules management

Snort is based on signature detection, which means you have to set rules so Snort can determine if a package is malicious or not.

Here is an overview of the free / paid set of rules you can find online.

| Name | Features | Price | Updated ? | Link |
| :---: | :---: | :---: | :---: | :---: |
| Snort community | Rules | Free | partially | [link](https://www.snort.org/downloads/community/snort3-community-rules.tar.gz)
| Snort registered | Rules, policies | Free | partially | [link](https://www.snort.org/downloads/registered/Talos_LightSPD.tar.gz)
| Snort subscription | Rules, policies | 29.99$/month | Yes | [link](https://www.snort.org/products)
| Emerging Threats | Rules | Free | Yes | [link](https://rules.emergingthreats.net/open/snort-edge/)


First, you have to set the folders where to put the rules, blocklist and logs:
```sh
sudo mkdir /usr/local/etc/rules
sudo mkdir /usr/local/etc/so_rules/
sudo mkdir /usr/local/etc/lists/
sudo touch /usr/local/etc/rules/local.rules
sudo touch /usr/local/etc/lists/default.blocklist
sudo mkdir /var/log/snort
```

Once done, you either can copy paste your own rules and blocklist or download set of rules from the snort website.


## Configuration

With snort, every configuration files are .lua file. Those files are located here :
```sh
cd /usr/local/snort/etc/snort
ls
```
or
```sh
cd /path/to/snort/etc/snort
ls
```

Read the main config file:
```sh
cat snort.lua
```

And as an example, you can read the default config:
```sh
cat snort_default.lua
```

### Default variables

In the snort config file, you can defines variable. Those variable are useful for writting rules.


### Network range

The network range is the first thing you set snort Snort can correctly work.
You have to define two values. The first one is the home network and the second one, external network.

Home network represent every IP ranges snort must scan and external network, which IP ranges snort must skip. 

Most of the time, you only set your home network because 'any' is enought for external network as you don't want any of them to be scanned.


### Search engine

In order to detect malicious content, Snort is using a Pattern Matching engine using regular expression. The engine implemented in Snort lack efficiency and must be replaced by a commonly accepted one, Hyperscan.

Let's install Hyperscan and its dependencies from source.


- Colm (previously: Ragel)
```sh
git clone "https://github.com/adrian-thurston/colm-suite/"

./configure
cmake ..
make -j $(( $(nproc) / 2 ))
make install
ldconfig
```

- Boost

I am using version 1.90.
Verify the latest version and change the url if needed [boost latest release](https://www.boost.org/releases/latest/).
```sh
wget_install "https://github.com/boostorg/boost/archive/refs/tags/boost-1.90.0.tar.gz" "https://archives.boost.io/release/1.90.0/source/boost_1_90_0.tar.gz"

tar xf boost_1_90_0.tar.gz
ln -s $PWD/boost_1_90_0/boost hyperscan/include/boost
```

Note: `As Hyperscan uses the header-only parts of Boost, it is not necessary to compile the Boost libraries.` [source](https://intel.github.io/hyperscan/dev-reference/getting_started.html)

- Hyperscan :
```sh
git clone "https://github.com/intel/hyperscan"

mkdir build && cd build
cmake ..
make -j $(( $(nproc) / 2 ))
make install
ldconfig
```


# Sources

- [Official documentation from snort.org](https://docs.snort.org/start/installation)

- [Snort 3.1.18.0 on Ubuntu 18 & 20 Configuring a Full NIDS & SIEM by Noah Dietrich](https://snort-org-site.s3.amazonaws.com/production/document_files/files/000/012/147/original/Snort_3.1.8.0_on_Ubuntu_18_and_20.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAU7AK5ITMBDFJ4Z4P%2F20260410%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260410T100704Z&X-Amz-Expires=172800&X-Amz-SignedHeaders=host&X-Amz-Signature=f89b62647ed595eecaa84db854015525dcfb17c92711a7f037bcffbaefb86f03)
