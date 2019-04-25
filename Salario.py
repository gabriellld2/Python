NUMBER = int(input())    #Número do Funcionário
HORAS = int(input())     # Horas Trabalhadas
SALARYH = round(float(input()), 2)  # Salário por hora trabalhada
SALARY = (HORAS * SALARYH)  #Cálculo do Salário
##PRINTS##
print("NUMBER =", NUMBER) #print do numero do funcionário
print("SALARY = U$ {:.2f}".format(SALARY)) ##Print do salário
