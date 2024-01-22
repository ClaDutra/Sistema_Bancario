# Sistema Bancario

Este projeto implementa um sistema bancário simples em Python, oferecendo funcionalidades básicas como depósito, saque, consulta de extrato e sair do sistema. O código é estruturado em um loop principal que exibe um menu de opções para o usuário.

**Funcionalidades:**

1. **Depositar (Opção 1):**
   - O usuário pode depositar um valor positivo na conta.
   - Se o valor for válido, ele é adicionado ao saldo, e a transação é registrada no extrato.
   - Caso contrário, uma mensagem de erro é exibida.

2. **Sacar (Opção 2):**
   - O usuário pode sacar um valor da conta, desde que respeite as seguintes condições:
      - Tenha saldo suficiente.
      - Não exceda o limite de saque definido.
      - Não ultrapasse o número máximo de saques permitidos.
   - Se as condições forem atendidas, o valor é deduzido do saldo, e a transação é registrada no extrato. Caso contrário, mensagens de erro específicas são exibidas.

3. **Extrato (Opção 3):**
   - O usuário pode visualizar um extrato contendo todas as transações realizadas, incluindo depósitos e saques.
   - O saldo atual da conta também é exibido.

4. **Sair (Opção 4):**
   - Permite ao usuário encerrar o programa.

**Observações:**
- O código inclui verificações de validação para garantir que as operações sejam realizadas corretamente.
- Limites são estabelecidos para garantir que as transações estejam dentro de parâmetros aceitáveis.
- O programa continua em execução até que o usuário escolha a opção de sair (4).

**Uso:**
- O usuário interage com o sistema através do console, inserindo o número correspondente à operação desejada no menu.
