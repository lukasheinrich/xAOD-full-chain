FROM lukasheinrich/slc6_cern_server_x86_64_2015-02-10
RUN yum groupinstall -y "Development Tools"
RUN yum install -y git make gcc-c++ gcc binutils libX11-devel libXpm-devel libXft-devel libXext-devel
RUN yum install -y gcc-gfortran openssl-devel pcre-devel mesa-libGL-devel glew-devel ftgl-devel mysql-devel fftw-devel cfitsio-devel graphviz-devel avahi-compat-libdns_sd-devel libldap-dev python-devel libxml2-devel gsl-static
RUN yum install -y procmail openssl098e.x86_64 compat-libf2c-34.x86_64 libtool-ltdl libtool-ltdl-devel
RUN mkdir /code
WORKDIR /code
COPY jo_maker /code/jo_maker
COPY resources /code/resources
COPY tests /code/tests
