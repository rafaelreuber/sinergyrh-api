FROM debian:buster-slim

RUN apt update -y && \
    apt install -y wget git dirmngr gnupg apt-transport-https ca-certificates build-essential && \
    wget https://packages.microsoft.com/config/debian/10/packages-microsoft-prod.deb -O packages-microsoft-prod.deb && \
    dpkg -i packages-microsoft-prod.deb &&  apt update -y && \
    apt-get install -y apt-transport-https dotnet-sdk-5.0 aspnetcore-runtime-5.0 dotnet-runtime-5.0 clang libglib2.0-dev python-dev python3-pip

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \
    echo "deb https://download.mono-project.com/repo/debian stable-buster main" | tee /etc/apt/sources.list.d/mono-official-stable.list && \
    apt update -y && \
    apt install mono-devel nuget -y

RUN apt install clang libglib2.0-dev python-dev -y

# Yes, you must install pythonnet 2x times. It's a bug ;)
RUN pip3 install pythonnet; pip3 install pythonnet
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /app
COPY CryptSinergyClient.dll .
COPY main.py /app

EXPOSE 5000:5000
CMD gunicorn -b 0.0.0.0:5000 --timeout=300 --workers=6 main:app