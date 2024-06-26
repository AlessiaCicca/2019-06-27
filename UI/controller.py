import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_analisi(self, e):
        reato = self._view.dd_reato.value
        if reato is None:
            self._view.create_alert("Selezionare un reato")
            return
        mese = self._view.dd_mese.value
        if mese is None:
            self._view.create_alert("Selezionare un mese")
            return

        grafo = self._model.creaGrafo(reato, int(mese))
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumNodes()} nodi."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumEdges()} archi."))
        lista=self._model.analisi()
        self._view.txt_result.controls.append(ft.Text(f"Il peso medio deglia archi del grafo è {self._model.pesoMedio}"))
        for (nodo1,nodo2,peso) in lista:
            self._view.txt_result.controls.append(ft.Text(f"{nodo1} e {nodo2} con peso={peso}"))
        self._view.update_page()


    def fillDD(self):
                reati = self._model.getReati
                for reato in reati:
                    self._view.dd_reato.options.append(ft.dropdown.Option(
                        text=reato))
                mese = self._model.getMesi
                for m in mese:
                    self._view.dd_mese.options.append(ft.dropdown.Option(
                        text=m))
