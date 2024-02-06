# Validador de CPF

- Este é um simples script em Python que valida números de CPF digitado pelo usuario.

## Funcionamento

- O programa solicita um CPF ao usuário, verificando se o usuário digitou corretamente ou enviou dados sequenciais. A partir disso, o código utiliza os primeiros nove digitos do CPF do usuário para gerar assim o primeiro dígito verificador. Em seguida, o programa calcula o segundo dígito verificador,com base nos primeiros 9 digitos e no primeiro dígito verificador

-Para validar um CPF fornecido pelo usuário, o script realiza os seguintes passos:

1. Calcula o primeiro dígito verificador com base nos primeiros nove dígitos do CPF fornecido.
2. Calcula o segundo dígito verificador com base nos primeiros nove dígitos do CPF fornecido e no primeiro dígito verificador calculado anteriormente.
3. Verifica se o CPF fornecido pelo usuário corresponde ao CPF calculado.
4. Se corresponder, o CPF é válido, se não, é inválido.

## Contribuição

- Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request se encontrar algum problema ou tiver uma sugestão de melhoria.

## Licença

- Este projeto é licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.

