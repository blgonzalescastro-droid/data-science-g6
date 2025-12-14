#ENCAPSULAMIENTO EN POO CON PYTHON
class Usuario:
    
    usuario_email = 'admin@gmail.com'
    usuario_password = '123'
    
    def __ini__(self):
        pass
    
    def login(self,email,password):
        if email == self.usuario_email and password == self.usuario_password:
            print('Login exitoso')
        else:
            print('Login fallido')
            
print("LOGIN DE USUARIO")
email = input('Ingrese su email: ')
password = input('Ingrese su password: ')

usuario = Usuario()
usuario.login(email, password)