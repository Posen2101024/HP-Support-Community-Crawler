
models=('Notebooks' 'Printers' 'Desktops' 'Tablets' 'Gaming' 'Software')

cd $(dirname "$0")

for model in ${models[*]}; do

	echo; echo ${model}

	python3 update.py ${model} --url

done

for times in $(seq 1 3); do

	for model in ${models[*]}; do

		echo; echo ${model}

		python3 update.py ${model} --html

	done

done