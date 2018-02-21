## Requirements  
- Ubuntu Server 16.04
- boost 1.65.1  
- cmake 3.9.6  
- ForexConnectAPI 1.4.1  

### Update system
    sudo apt-get update
    sudo apt-get -y upgrade
    sudo reboot

### Install apt-get packages
    sudo apt-get -y install git
    sudo apt-get -y install python3-pip
    sudo apt-get -y install build-essential
    sudo apt-get -y install python3-dev
    sudo apt-get -y install build-essential libboost-log-dev libboost-date-time-dev libboost-python-dev
    sudo apt-get -y install libtool m4 automake autogen
    sudo apt-get -y install checkinstall

### Install pip packages
    pip3 install numpy
    pip3 install pymysql
    pip3 install cprint
    pip3 install pytz
    pip3 install ipython3


### Install libuv
[http://www.linuxfromscratch.org/blfs/view/cvs/general/libuv.html](http://www.linuxfromscratch.org/blfs/view/cvs/general/libuv.html)

    wget https://github.com/libuv/libuv/archive/v1.19.1/libuv-1.19.1.tar.gz
    tar -xvzf libuv-1.19.1.tar.gz
    cd libuv-1.19.1/
    sh autogen.sh  &&
    ./configure --prefix=/usr --disable-static &&
    make
    sudo checkinstall


### Install libarchive
    wget http://www.libarchive.org/downloads/libarchive-3.3.2.tar.gz
    tar -xvzf libarchive-3.3.2.tar.gz
    cd libarchive-3.3.2/
    ./configure --prefix=/usr \
    --disable-static &&
    make
    sudo checkinstall
    

### Install curl-7.58.0
    wget https://curl.haxx.se/download/curl-7.58.0.tar.xz
    tar -xf curl-7.58.0.tar.xz
    cd curl-7.58.0/
    ./configure --prefix=/usr   \
    --disable-static\
    --enable-threaded-resolver  &&
    make
    sudo checkinstall


### Install cmake 3.9.6
[http://www.linuxfromscratch.org/blfs/view/cvs/general/cmake.html](http://www.linuxfromscratch.org/blfs/view/cvs/general/cmake.html)

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


### Install which-2.21
[http://www.linuxfromscratch.org/blfs/view/cvs/general/which.html](http://www.linuxfromscratch.org/blfs/view/cvs/general/which.html)

    wget ftp://ftp.gnu.org/gnu/which/which-2.21.tar.gz
    tar -xvzf which-2.21.tar.gz
    cd which-2.21/
    ./configure --prefix=/usr &&
    make
    sudo check install


### Boost Install
[http://www.boost.org/users/history/version_1_65_1.html](http://www.boost.org/users/history/version_1_65_1.html)
[http://www.linuxfromscratch.org/blfs/view/cvs/general/boost.html](http://www.linuxfromscratch.org/blfs/view/cvs/general/boost.html)

    wget https://dl.bintray.com/boostorg/release/1.65.1/source/boost_1_65_1.tar.gz
    tar -xvzf boost_1_65_1.tar.gz
    cd boost_1_65_1
    ./bootstrap.sh --with-python=python3.5  --prefix=/usr
    echo "using python : 3.5 : /usr/bin/python3.5 : /usr/include/python3.5 : /usr/lib ;" >> project-config.jam
    ./b2 stage threading=multi link=shared -j 2
    sudo ./b2 install threading=multi link=shared -j 2

### Required for compiling python3-forexconnect
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

### Install python3-forexconnect  
    wget http://fxcodebase.com/bin/forexconnect/1.4.1/ForexConnectAPI-1.4.1-Linux-x86_64.tar.gz  
    tar xvf ForexConnectAPI-1.4.1-Linux-x86_64.tar.gz  
    mv ForexConnectAPI-1.4.1-Linux-x86_64 ForexConnectAPI  
    git clone -b python3-forexconnect https://github.com/JamesKBowler/python-forexconnect.git  

    cd python-forexconnect && mkdir build && cd build  
    cmake .. -DDEFAULT_FOREX_URL="http://www.fxcorporate.com/Hosts.jsp"  
    sudo make install  

