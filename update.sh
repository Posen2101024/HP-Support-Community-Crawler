
if [ "$#" == "0" ]; then
	models=('Notebooks' 'Printers' 'Desktops' 'Tablets' 'Gaming' 'Software')
else
	models="$@"
fi

cd $(dirname "$0")

for model in ${models[*]}; do

	printf "\n${model}\n"

	python3 main.py ${model} --url

done

for times in $(seq 1 3); do

	printf "\n%s\n" "------------------------------"

	for model in ${models[*]}; do

		printf "\n${model}\n"

		python3 main.py ${model} --html

	done

done
