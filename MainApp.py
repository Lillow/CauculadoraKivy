from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MainApp(App):
    def build(self):
        self.operators = ['+', '-', '*', '/']
        self.last_was_operator = None
        self.last_button = None
        '''Nas linhas acima, 
        criamos uma lista de operators e alguns valores úteis, 
        last_was_operator e last_button, que nós usaremos mais tarde.'''

        main_layout = BoxLayout(orientation = 'vertical')
        self.solution = TextInput(
            multiline = False, readonly = True, halign = 'right', font_size = 55
        ) 

        '''Nas linhas acima, criamos um layout main_layout de nível superior 
        e adicionamos um widget TextInput somente leitura a ele.'''

        main_layout.add_widget(self.solution)
        buttons = [['7', '8', '9', '/'],
                   ['4', '5', '6', '*'],
                   ['1', '2', '3', '-'],
                   ['.', '0', 'C', '+']]
        '''Nas linhas acima, nós criamos uma lista aninhada de listas 
        contendo a maioria dos nossos buttons para a calculadora.'''

        for row in buttons: # nós iniciamos um forloop sobre aqueles buttons.Para cada lista
            h_layout = BoxLayout() # criamos um BoxLayout com orientação horizontal
            for label in row: #  iniciamos outro loop sobre os itens da lista aninhada
                button = Button( 
                    text = label,
                    pos_hint = {'center_x': .5, 'center_y': .5},
                ) 
                ''' Nas linhas acima nós criamos os botões para a linha, 
                os vinculamos a um manipulador de eventos e 
                adicionamos os botões à horizontalBoxLayout'''

                button.bind(on_press = self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)  # você adiciona esse layout ao arquivo main_layout

        equals_button = Button(
            text = '=', pos_hint = {'center_x': .5, 'center_y': .5}
        )
        equals_button.bind(on_press = self.on_solution)
        main_layout.add_widget(equals_button)
        '''Nas linhas acima, você cria o botão igual (=),
        associa-o a um manipulador de eventos e adiciona-oa main_layout.'''

        return main_layout
        
        # A próxima etapa é criar o manipulador de eventos on_button_press(). Vamos lá!

    def on_button_press(self, instance): # recebe o argumento instance para que você possa acessar qual widget chamou a função.
        current = self.solution.text
        button_text = instance.text
    # Nas linhas acima, extraem e armazenam o valor do solution e do botão text.

        if button_text == 'C':
            '''verifica qual botão foi pressionado. Se o usuário pressionou C, 
            você limpará o arquivo solution. 
            Caso contrário,vá para a declaração else'''

            # Clear the solution widget
            self.solution.text = ''
        else:
            
            if current and (self.last_was_operator # verifica se a solução possui algum valor pré-existente.
                            and button_text in self.operators):
                '''verificam se o último botão pressionado foi um botão do operador. 
                Se foi, então solution não será atualizado. 
                Isso é para evitar que o usuário tenha dois operadores seguidos.
                Por exemplo, 1 */ não é uma declaração válida.'''

                # Don’t add two operators right after each other

                return
            elif current == '' and button_text in self.operators:
                '''verifica se o primeiro caractere é um operador. 
                Se for, solution não será atualizado, 
                poiso primeiro valor não pode ser um valor de operador.'''

                # First character cannot be an operator

                return

            else:
                new_text = current + button_text
                self.solution.text = new_text
                '''cai para a cláusula else. 
                Se nenhuma das condições anteriores for atendida, 
                atualize o solution.'''

        self.last_button = button_text # define last_button no rótulo do último botão pressionado.
        self.last_was_operator = self.last_button in self.operators # é definida last_was_operator como True ou False dependendo se era ou não um caractere de operador.

        # A última parte do código a ser digitada é o .on_solution(). Veja abaixo:

    def on_solution(self, instance):
        text = self.solution.text

        if text:
            solution = str(eval(self.solution.text))

            self.solution.text = solution

if __name__ == '__main__':
    MainApp().run()