
if [ "$#" == "0" ]; then
	models=('Notebooks' 'Printers' 'Desktops' 'Tablets' 'Gaming' 'Software')
else
	models="$@"
fi

cd $(dirname "$0")

for model in ${models[*]}; do

	echo ${model}

	python3 main.py ${model} --url

	echo

done

for times in $(seq 1 3); do

	echo "------------------------------\n"

	for model in ${models[*]}; do

		echo ${model}

		python3 main.py ${model} --html

		echo

	done

done