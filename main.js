const fs = require('fs');

function escreverDadosEmCSV(formulario, nomeArquivo) {
	const dadosCSV = Object.values(formulario).join(',') + '\n';

	fs.appendFile(nomeArquivo, dadosCSV, (err) => {
		if (err) {
			console.error('Erro ao escrever os dados no arquivo CSV:', err);
		} else {
			console.log('Dados escritos com sucesso no arquivo CSV!');
		}
	});
}

function getInputValues(form) {
	const inputs = form.querySelectorAll('input');
	const values = {};

	inputs.forEach((input) => {
		values[input.name] = input.value;
	});

	return values;
}


function handleClick(event)
      {
        alert("Funfou")
      }

escreverDadosEmCSV(formulario, nomeArquivo);