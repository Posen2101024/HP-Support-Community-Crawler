
if [ "$#" == "0" ]; then
	version=83.0.4103.39
else
	version=${1}
fi

cd $(dirname "$0")

mkdir -p ../crawler/chromedriver/Linux &&\
wget https://chromedriver.storage.googleapis.com/${version}/chromedriver_linux64.zip &&\
unzip -o chromedriver_linux64.zip &&\
rm chromedriver_linux64.zip &&\
mv chromedriver ../crawler/chromedriver/Linux

mkdir -p ../crawler/chromedriver/Mac &&\
wget https://chromedriver.storage.googleapis.com/${version}/chromedriver_mac64.zip &&\
unzip -o chromedriver_mac64.zip &&\
rm chromedriver_mac64.zip &&\
mv chromedriver ../crawler/chromedriver/Mac
