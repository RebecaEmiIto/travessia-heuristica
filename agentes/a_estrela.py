from agentes.abstrato import AgenteAbstrato


class A_Estrela(AgenteAbstrato):
    def ___init__(self):
        super().__init__()
        pass

    
        
"""
1° - veja o Avaliacao

2° - faça o método de probabilidade somando os resultados da avaliacao

3° - faça um random.random()

4° - com o resultado do random.random() subtraia com cada resultado da divisão do fitness ate um deles dar negativo
ex:random.random()
   0.7251890729417858
   0.7251890729417858 - 0.2625
   0.4626890729417858
   0.4626890729417858 - 0.225
   0.2376890729417858
   0.2376890729417858 - 0.25
   -0.01231092705821421

5° - (para esse exercício faça mais 3x a mesma coisa que fez no 4°)

"""