#class y object

#   una clase es un mecanismo de "paquetizar" datos y funciones en una unica identidad -> puede tener variables propias de la clase que son comunes a todos los elementos de la clase
#   una clase se puede sustanciar creando un objeto instanciado del tipo definidio por la clase
#   los objetos instanciados (objetos creados) tienen atributos que pueden ser datos (variables) y métodos (funciones)
#   el primer argumento en caso de objetos vas a ser (self, ...) que hace referencia al propio objeto
#   un método especial es el "constructor" y otro es el "destructor"
#   los atributos de datos (variables) de la clase son comunes a todos los objetos de la clase
#   automaticamente se añade como primer argumento de las funciones de un objeto instanciado la referencia al objeti instanciado
# por convenio el primer argumento es llamado "self"

#   EJEMPLO

    class RobotSixDegrees:
        """class represent and manage six degree of freedom robots"""

        num_robots = 0

        def __init__(self, name):
            RobotSixDegrees.num_robots += 1
            self.filename = name
            #Robot axis default position in radians
            self.axis_1 = self.axis_2 = self.axis_3 = self.axis_4 = \
            self.axis_5 = self.axis_6 = 0.0
        def __del__(self):
            RobotSixDegrees.num_robots -= 1
        def move_tcp(self, x, y, z, rot):
            self.tcp_x = x
            self. tcp_y = y
            self.tcp_z = z
            self.tcp_rot = rot

irb = RobotSixDegrees("irb")
print("File name: ", irb.filename)
ur3 = RobotSixDegrees("UR3")
print("File name: ", ur3.filename)
print("Number of robots después de creador ur3: ", RobotSixDegrees.num_robots)
del(ur3) #despues de haber borrado el robot UR3, la variable ahora vale 1
print("Number of robots borrado ur3: ", RobotSixDegrees.num_robots)
print("IRB axis positions: ", irb.axis_1, irb.axis_2, irb.axis_3, irb.axis_4, irb.axis_5, irb.axis_6)
irb.move_tcp(100, 200, 300, 90)
print("TCP position: ", irb.tcp_x, irb.tcp_y, irb.tcp_z, irb.tcp_rot)
del(irb)
print("Number of robots borrado irb: ", RobotSixDegrees.num_robots)
