class Example(MDApp):
    # ... (código existente)

    def build(self):
        # ... (código existente)
        return Builder.load_string(KV)

    def mover_para_historico(self, tarefa_id, tarefa_nome, tarefa_descricao):
        try:
            db.child("historico").push({
                'nome': tarefa_nome,
                'descricao': tarefa_descricao,
                'tarefa_pai': tarefa_id
            })
            self.delete_task(tarefa_id)  # Remove a tarefa da lista de tarefas
            self.listar_tarefas()  # Atualiza a lista de tarefas exibida
        except Exception as e:
            print(f"Erro ao mover tarefa para o histórico: {str(e)}")

    def listar_tarefas(self):
        tarefas_list = self.root.ids.tarefas_list
        tarefas_list.clear_widgets()

        tarefas = db.child("tarefas").get()
        if tarefas.each():
            for tarefa in tarefas.each():
                tarefa_nome = tarefa.val()['nome']
                tarefa_descricao = tarefa.val()['descricao']
                tarefa_id = tarefa.key()

                tarefa_label = TarefaListItem(
                    text=f"{tarefa_nome}",
                    secondary_text=f"{tarefa_descricao}",
                    tarefa_id=tarefa_id
                )

                tarefa_label.add_checkbox()  # Adiciona o checkbox
                tarefa_label.checkbox.bind(active=lambda checkbox, active, tarefa_id=tarefa_id, tarefa_nome=tarefa_nome, tarefa_descricao=tarefa_descricao: self.checkbox_handler(checkbox, active, tarefa_id, tarefa_nome, tarefa_descricao))

                tarefas_list.add_widget(tarefa_label)

    def checkbox_handler(self, checkbox, active, tarefa_id, tarefa_nome, tarefa_descricao):
        if active:
            self.mover_para_historico(tarefa_id, tarefa_nome, tarefa_descricao)
