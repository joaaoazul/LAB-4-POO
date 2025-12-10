from abc import ABC, abstractmethod

class VeiculoEletrico(ABC):
    def __init__(self, carga_inicial: float):
        self.__carga_atual = max(0.0, min(100.0, carga_inicial))

    @property
    def carga(self):
        return self.__carga_atual

    def _alterar_carga(self, valor: float):
        nova_carga = self.__carga_atual + valor
        self.__carga_atual = max(0.0, min(100.0, nova_carga))

    @abstractmethod
    def deslocar(self, distancia: float) -> float:
        pass

    @abstractmethod
    def recarregar(self, carga: float) -> float:
        pass

    def mostrar_carga(self):
        print(f"Carga atual do veículo: {self.__carga_atual:.2f}%")

class TrotineteEletrica(VeiculoEletrico):
    def deslocar(self, distancia: float) -> float:
        consumo = distancia * 1.0

        if self.carga >= consumo:
            self._alterar_carga(-consumo)
            return consumo
        else:
            print(f"[Trotinete] Erro: Carga insuficiente para {distancia}km")
            return 0.0

    def recarregar(self, minutos: float) -> None:
        ganho = minutos * 0.5
        self._alterar_carga(ganho)


class BicicletaEletrica(VeiculoEletrico):
    def deslocar(self, distancia: float) -> float:
        consumo = distancia * 0.5

        if self.carga >= consumo:
            self._alterar_carga(-consumo)
            return consumo
        else:
            print(f"[Bicicleta] Erro: Carga insuficiente para {distancia}km")
            return 0.0

    def recarregar(self, minutos: float) -> None:
        ganho = minutos * 3.0
        self._alterar_carga(ganho)

class CarroEletrico(VeiculoEletrico):
    def deslocar(self, distancia: float) -> float:
        consumo = distancia * 2.0

        if self.carga >= consumo:
            self._alterar_carga(-consumo)
            return consumo
        else:
            print(f"[Carro] Erro: Carga insuficiente para {distancia}km")
            return 0.0

    def recarregar(self, minutos: float) -> None:
        ganho = minutos * 10.0
        self._alterar_carga(ganho)

class SistemaMobilidade:
    def __init__(self):
        self.frota = []

    def realizar_deslocamento(self, distancia):
        pass

    def adicionar_veiculo(self, veiculo):
        self.frota.append(veiculo)
        print(f"Veículo adicionado: {type(veiculo).__name__}")

    def listar_cargas(self):
        print("=== ESTADO ATUAL DA FROTA ===")
        for veiculo in self.frota:
            nome_tipo = type(veiculo).__name__
            print(f"[{nome_tipo}]", end="")
            veiculo.mostrar_carga()

    def recarregar_todos(self, minutos):
        print(f"A CARREGAR A FROTA POR {minutos} MINUTOS")

        for veiculo in self.frota:
            veiculo.recarregar(minutos)
            print(f" -> {type(veiculo).__name__}: ", end="")
            veiculo.mostrar_carga()


if __name__ == "__main__":
    print(">>> SISTEMA DE GESTÃO DE FROTA <<<")

    sistema = SistemaMobilidade()

    v1 = TrotineteEletrica(50)
    v2 = BicicletaEletrica(95)
    v3 = CarroEletrico(10)

    sistema.adicionar_veiculo(v1)
    sistema.adicionar_veiculo(v2)
    sistema.adicionar_veiculo(v3)

    sistema.listar_cargas()

    sistema.realizar_deslocamento(15.0)

    sistema.recarregar_todos(10.0)

    print("\n>>> FIM <<<")

print("a91152 - João Azul")