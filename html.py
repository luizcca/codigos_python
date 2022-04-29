arquivo = open('ola.html', 'w', encoding='utf-8')
arquivo.write('''<!DOCTYPE html>
<html lang="pt-BR"
<head>
<meta charset="utf-8">
<title> Teste Python com html</title>
</head>
<body>
<i>
<b>
<h1 style="text-indent:30px;">
Introdução
• Ambiente multiusuário
– vários usuários utilizam o mesmo sistema ao mesmo tempo
– múltiplos programas (transações) compartilham a mesma CPU
Laboratório de Bases de Dados – Processamento de Transações
Profa. Dra. Cristina Dutra de Aguiar Ciferri

compartilham a mesma CPU
• Forma de execução dos programas
– intercalada (interleaved)
– alguns comandos de um programa são executados e o programa é
suspenso; alguns comandos de outro
programa são executados, o programa é suspenso, e assim por diante ...
</h1>
</b>
</i>
</body>
</html>''')
arquivo.close()
