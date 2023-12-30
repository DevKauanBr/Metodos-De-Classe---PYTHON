#Nas classes, existe dois tipo de escopo, escopo de INSTÂNCIA e escopo de CLASSE. Se por acaso um metodo for criado no escopo do classe ele não...
#pode interagir com atributos ou outras coisas referente ao escopo da INSTÂNCIA.
#VEJAMOS O EXEMPLO A SEGUIR:

class controleRemoto:
    variaveldaclasse = 'sbt'        #<------ Variaveis como essa são do escopo da classe e se for acessar através de metodos, tem que ser
                                    # METODOS DE CLASSE
    def __init__(self):
        self.canal = 'sbt'                             #<------ Atributo criado, esses fazem parte do escopo da INSTÂNCIA

    def passar_canal1(self, canalParaPassar):                                    
        print(f'O canal foi passado para {canalParaPassar}')        #<------  criado no escopo de INSTÂNCIA

    @classmethod
    def passar_canal2(cls):
        print(f'O canal foi passado para {cls.variaveldaclasse}')       #<------  criado no escopo de CLASSE
'                                         ⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆ - Aqui podemos ver que estamos usando a variavel global lá de cima que somente...'
'pode ser acessada se o metodo for global.'

    

controleRemoto.passar_canal2()             #<------ Aqui podemos ver que atráves do metodo de CLASSE podemos chamar sem precisar
                                               #criamos uma instância. A saida será : "O canal foi passado para sbt"

#Um detalhe que podemos ver é que o comando a cima, ele não usa os atributos lá em cima, até porque não tem como pois os atributos são do escopo 
#da instância e não da classe.

print()        #<------ Print para separar a saída

#Agora em baixo vamos tentar fazer a mesma coisa com o metodo que não é da classe e vamos enfrentar erros.

controleRemoto.passar_canal1('sbt')
#E como podemos esperar... essa foi a saída:


'''O canal foi passado para sbt
Traceback (most recent call last):
  File "c:\Windows\PythonPast00222\Teoria\Classes\Metodos de Classes.py", line 26, in <module>     
    controleRemoto.passar_canal1('sbt')
TypeError: controleRemoto.passar_canal1() missing 1 required positional argument: 'canalParaPassar'''

#Podemos ver que somente a linha de cima deu certo e a de baixo não deu pois ele está tentando chamar o metodo "passar_canal1('sbt')" que é
#pertecente ao escopo de INSTÂNCIA no escopo global.


'Métodos de Instância:'
# - São métodos associados a uma instância específica da classe.
# - Têm acesso aos atributos da instância (self.atributo).
# - São chamados em uma instância da classe.

'Métodos de Classe:'
# - São métodos associados à classe, não a uma instância específica.
# - São decorados com @classmethod.
# - Têm acesso apenas aos atributos da classe (cls.atributo).
# - São chamados na classe, não em uma instância.
