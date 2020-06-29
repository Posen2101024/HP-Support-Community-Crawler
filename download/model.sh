
cd $(dirname "${0}")/..

download() {

	# id = ${1}

	gdown "https://drive.google.com/uc?export=download&id=${1}" -O model.zip

	unzip -o model.zip && rm model.zip
}

download "1-e0MIuw2q1qSsLvL9Y0LAAMM1SdF6gvg"
