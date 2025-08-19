import sys

def validar_cpf(cpf):
   if not cpf.isdigit():
      print("\nErro! Por favor, digite apenas números.\n")
      return False
  
   return True

def tamanho_cpf(cpf):
  if len(cpf) != 11:
      print("\nErro! O CPF deve ter exatamente 11 (onze) dígitos.\n", file=sys.stderr)
      return False
  
  return True

def sequencia(cpf):
   count = 0
   for i in range(11):
      if cpf[i] == cpf[0]:
         count += 1
   
   if count == 11:
      print("\nErro! Os dígitos do CPF não podem ser todos iguais.\n", file=sys.stderr)
      return False
   
   return True
      
def digito_dez(cpf):
   fat = 10
   soma = 0
   for i in range(9):
      soma += int(cpf[i]) * fat
      fat -= 1
   n10 = (soma * 10) % 11
   
   return '0' if n10 == 10 else str(n10)

def digito_onze(cpf2):
   fat = 11
   soma = 0
   for i in range(10):
      soma += int(cpf2[i]) * fat
      fat -= 1
   n11 = (soma * 10) % 11

   return '0' if n11 == 10 else str(n11)

while True:
  cpf = input("\nInforme o seu CPF (ou digite 'sair' para finalizar): ")

  if cpf.lower() == "sair":
     print("\nPrograma encerrado.")
     sys.exit(0)

  validar = validar_cpf(cpf)
  if validar == False:
     continue
  else:
     validar = tamanho_cpf(cpf)
     if validar == False:
        continue
     else:
        validar = sequencia(cpf)
        if validar == False:
           continue
        else:
           n10 = digito_dez(cpf)
           n11 = digito_onze(cpf)
           
           if n10 == cpf[9] and n11 == cpf[10]:
              print("\nCPF VÁLIDO! ✅")
              sys.exit(0)
           else:
              print("\nCPF INVÁLIDO! ❌")
              sys.exit(0)