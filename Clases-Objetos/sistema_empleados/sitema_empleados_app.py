from empresa import Empresa
from empleado import Empleado

print('*** Sistema de Empleados ***')

# Crear una instancia de una empresa
empresa1 = Empresa('Futurmatica')

# Contratar empleados
empresa1.contratar_empleado('Juan', 'Desarrollo')
empresa1.contratar_empleado('Karla', 'Recursos Humanos')
empresa1.contratar_empleado('Pedro', 'Desarrollo')
empresa1.contratar_empleado('Martha', 'Finanzas')

# Obtener el total de objetos de tipo Empleado
print(f'Total de empleados: {Empleado.obtener_total_empleados()}')

# Obtener el número de empleados en el departamento de desarrollo
print(f'Empleados en el departamento de Desarrollo: {empresa1.obtener_numero_empleados_departamento("Desarrollo")}')

# Obtener el total de empleados de empresa1
empresa1.obtener_total_empleados()