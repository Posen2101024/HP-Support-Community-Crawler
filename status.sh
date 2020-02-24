
cd $(dirname "$0")

touch .status

while :; do

	clear

	printf "$(date)\n"

	cat .status; 

	sleep 1

done
