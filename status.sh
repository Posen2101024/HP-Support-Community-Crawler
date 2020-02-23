
cd $(dirname "$0")

touch .status

while :; do

	clear

	echo "$(date)"

	cat .status; 

	sleep 1

done
