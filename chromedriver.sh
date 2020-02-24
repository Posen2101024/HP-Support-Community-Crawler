
if [ "$#" == "0" ]; then
	version=80.0.3987.106
else
	version=${1}
fi

mkdir -p crawler/chromedriver/Linux &&\
wget https://chromedriver.storage.googleapis.com/${version}/chromedriver_linux64.zip &&\
unzip chromedriver_linux64.zip &&\
rm chromedriver_linux64.zip &&\
mv chromedriver crawler/chromedriver/Linux

mkdir -p crawler/chromedriver/Mac &&\
wget https://chromedriver.storage.googleapis.com/${version}/chromedriver_mac64.zip &&\
unzip chromedriver_mac64.zip &&\
rm chromedriver_mac64.zip &&\
mv chromedriver crawler/chromedriver/Mac

mkdir -p crawler/chromedriver/Windows &&\
wget https://chromedriver.storage.googleapis.com/${version}/chromedriver_win32.zip &&\
unzip chromedriver_win32.zip &&\
rm chromedriver_win32.zip &&\
mv chromedriver.exe crawler/chromedriver/Windows
