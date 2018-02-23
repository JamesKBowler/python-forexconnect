python3-forexconnect
===================

[![alt text](https://travis-ci.org/neka-nat/python-forexconnect.svg?branch=master)](https://travis-ci.org/neka-nat/python-forexconnect)

About
------
This library is a Python binding of Forexconnect API
using boost.python.

Build
-----

#### Tested Working Specifications   
- Ubuntu Server 16.04
- Python 3.5.2
- boost 1.65.1  
- cmake 3.9.6  
- ForexConnectAPI 1.4.1 

#### Update system
    sudo apt-get update
    sudo apt-get -y upgrade
    sudo reboot

#### Install apt-get packages
    sudo apt-get -y install git
    sudo apt-get -y install python3-pip
    sudo apt-get -y install build-essential
    sudo apt-get -y install python3-dev
    sudo apt-get -y install build-essential libboost-log-dev libboost-date-time-dev libboost-python-dev
    sudo apt-get -y install libtool m4 automake autogen
    sudo apt-get -y install checkinstall

#### Install pip packages
    pip3 install ipython3

#### [<>](http://www.linuxfromscratch.org/blfs/view/cvs/general/libuv.html)  Install libuv 

    wget https://github.com/libuv/libuv/archive/v1.19.1/libuv-1.19.1.tar.gz
    tar -xvzf libuv-1.19.1.tar.gz
    cd libuv-1.19.1/
    sh autogen.sh  &&
    ./configure --prefix=/usr --disable-static &&
    make
    sudo checkinstall

#### [<>](http://linuxfromscratch.org/blfs/view/svn/general/libarchive.html)  Install libarchive  

    wget http://www.libarchive.org/downloads/libarchive-3.3.2.tar.gz
    tar -xvzf libarchive-3.3.2.tar.gz
    cd libarchive-3.3.2/
    ./configure --prefix=/usr \
    --disable-static &&
    make
    sudo checkinstall

#### [<>](http://linuxfromscratch.org/blfs/view/svn/basicnet/curl.html) Install curl-7.58.0  

    wget https://curl.haxx.se/download/curl-7.58.0.tar.xz
    tar -xf curl-7.58.0.tar.xz
    cd curl-7.58.0/
    ./configure --prefix=/usr   \
    --disable-static\
    --enable-threaded-resolver  &&
    make
    sudo checkinstall

#### [<>](http://www.linuxfromscratch.org/blfs/view/cvs/general/cmake.html) Install cmake 3.9.6  

    wget https://cmake.org/files/v3.9/cmake-3.9.6.tar.gz
    tar -xvzf cmake-3.9.6.tar.gz
    cd cmake-3.9.6/
    sed -i '/"lib64"/s/64//' Modules/GNUInstallDirs.cmake &&
    
    ./bootstrap --prefix=/usr\
    --system-libs\
    --mandir=/share/man  \
    --no-system-jsoncpp  \
    --no-system-librhash \
    --docdir=/share/doc/cmake-3.10.2 &&
    make
    sudo checkinstall

#### [<>](http://www.linuxfromscratch.org/blfs/view/cvs/general/which.html)  Install which-2.21  

    wget ftp://ftp.gnu.org/gnu/which/which-2.21.tar.gz
    tar -xvzf which-2.21.tar.gz
    cd which-2.21/
    ./configure --prefix=/usr &&
    make
    sudo check install

#### [<>](http://www.linuxfromscratch.org/blfs/view/cvs/general/boost.html)  Boost Install  

    wget https://dl.bintray.com/boostorg/release/1.65.1/source/boost_1_65_1.tar.gz
    tar -xvzf boost_1_65_1.tar.gz
    cd boost_1_65_1
    ./bootstrap.sh --with-python=python3.5  --prefix=/usr
    echo "using python : 3.5 : /usr/bin/python3.5 : /usr/include/python3.5 : /usr/lib ;" >> project-config.jam
    ./b2 stage threading=multi link=shared -j 2
    sudo ./b2 install threading=multi link=shared -j 2
    [www.boost.org](http://www.boost.org/users/history/version_1_65_1.html)

#### Required for compiling python3-forexconnect
    export BOOST_ROOT="/usr"
    export BOOST_INCLUDEDIR="/usr/include/"
    export BOOST_LIBRARYDIR="/usr/lib/"
    export INCLUDE="/usr/include/boost/:$INCLUDE"
    export LIBRARY_PATH="/usr/local/:$LIBRARY_PATH"
    export FOREXCONNECT_ROOT="$(pwd)/ForexConnectAPI"
    export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$(pwd)/ForexConnectAPI/lib"
    echo "export BOOST_ROOT=/usr" >> .profile
    echo "export BOOST_INCLUDEDIR=/usr/include/" >> .profile
    echo "export BOOST_LIBRARYDIR=/usr/lib/" >> .profile
    echo "export INCLUDE=/usr/include/boost/:$INCLUDE" >> .profile
    echo "export LIBRARY_PATH=/usr/local/:$LIBRARY_PATH" >> .profile
    echo "export FOREXCONNECT_ROOT=$(pwd)/ForexConnectAPI" >> .profile
    echo "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$(pwd)/ForexConnectAPI/lib" >> .profile
    sudo ldconfig

**Note if you are using a python virtual env, it is necessary to change this line in the CMake file**  

**from this..**  
>     COMMAND python3 -c "import site; print(site.getsitepackages()[0])"

**to this..**    
>     COMMAND python3 -c "import site, os; print(os.path.dirname(site.__file__) + '/site-packages')"

#### Install python3-forexconnect  
    wget http://fxcodebase.com/bin/forexconnect/1.4.1/ForexConnectAPI-1.4.1-Linux-x86_64.tar.gz  
    tar xvf ForexConnectAPI-1.4.1-Linux-x86_64.tar.gz  
    mv ForexConnectAPI-1.4.1-Linux-x86_64 ForexConnectAPI  
    git clone https://github.com/neka-nat/python-forexconnect.git
    cd python-forexconnect && mkdir build && cd build  
    cmake .. -DDEFAULT_FOREX_URL="http://www.fxcorporate.com/Hosts.jsp"  
    sudo make install  


Usage
------

This tutorial is simple trading using python-forexconnect.
First, give FXCM account username, password and type ("Real" or "Demo") to login.
Next, send query to open position and get the position list which you have.
Finally, close the opened position and logout.

    >> import forexconnect
    >> cl = forexconnect.ForexConnectClient("usrname", "pass", "Real")
    >> cl.open_position("EUR/JPY", forexconnect.BUY, 1)
    >> ti = cl.get_trades()
    >> cl.close_position(ti[0].trade_id)
    >> cl.logout()
