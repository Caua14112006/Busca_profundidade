def criar_grafo():

    return {}





def inserir_vertice(grafo, vertice):

    if vertice not in grafo:

        grafo[vertice] = []

        print("Vertice inserido com sucesso!")

    else:

        print("Vertice ja existe!")





def inserir_aresta(grafo, origem, destino, nao_direcionado=False):

    if origem not in grafo:

        inserir_vertice(grafo, origem)



    if destino not in grafo:

        inserir_vertice(grafo, destino)



    if destino not in grafo[origem]:

        grafo[origem].append(destino)



    if nao_direcionado and origem != destino:

        if origem not in grafo[destino]:

            grafo[destino].append(origem)



    print("Aresta inserida com sucesso!")





def vizinhos(grafo, vertice):

    if vertice in grafo:

        return grafo[vertice]

    return []





def listar_vizinhos(grafo, vertice):

    if vertice in grafo:

        print("Vizinhos de", vertice, ":", vizinhos(grafo, vertice))

    else:

        print("Vertice nao encontrado!")





def exibir_grafo(grafo):

    if not grafo:

        print("Grafo vazio!")

        return



    print("\nLista de Adjacencia:")

    for vertice in grafo:

        print(vertice, "->", grafo[vertice])





def remover_aresta(grafo, origem, destino, nao_direcionado=False):

    if origem not in grafo or destino not in grafo:

        print("Vertice nao encontrado!")

        return



    if destino not in grafo[origem]:

        print("Aresta nao encontrada!")

        return



    grafo[origem].remove(destino)



    if nao_direcionado and origem != destino:

        if origem in grafo[destino]:

            grafo[destino].remove(origem)



    print("Aresta removida com sucesso!")





def remover_vertice(grafo, vertice, nao_direcionado=True):

    if vertice not in grafo:

        print("Vertice nao encontrado!")

        return



    for outro in grafo:

        if vertice in grafo[outro]:

            grafo[outro].remove(vertice)



    del grafo[vertice]

    print("Vertice removido com sucesso!")





def existe_aresta(grafo, origem, destino):

    if origem in grafo:

        return destino in grafo[origem]

    return False





def grau_vertices(grafo, nao_direcionado=False):

    graus = {}



    for vertice in grafo:

        graus[vertice] = {

            "entrada": 0,

            "saida": len(grafo[vertice]),

            "total": 0

        }



    for origem in grafo:

        for destino in grafo[origem]:

            graus[destino]["entrada"] += 1



    for vertice in grafo:

        if nao_direcionado:

            # Cada laco conta duas vezes no grau.

            graus[vertice]["total"] = (

                len(grafo[vertice]) +

                (1 if vertice in grafo[vertice] else 0)

            )

        else:

            graus[vertice]["total"] = (

                graus[vertice]["entrada"] +

                graus[vertice]["saida"]

            )



    return graus


def busca_largura(grafo, origem):
    if origem not in grafo:
        print("O vertice informado nao existe")
        return []

    visitados = []
    fila = []

    fila.append(origem)

    while fila:
        vertice = fila.pop(0)

        if vertice not in visitados:
            visitados.append(vertice)

            lista_vizinhos = vizinhos(grafo, vertice)

            for v in lista_vizinhos:
                if v not in fila and v not in visitados:
                    fila.append(v)

    return visitados





def menor_caminho(grafo, origem, destino):
    if origem not in grafo or destino not in grafo:
        print("Vertice nao encontrado!")
        return []

    fila = [(origem, [origem])]
    visitados = []

    while fila:
        vertice, caminho = fila.pop(0)

        if vertice == destino:
            return caminho

        if vertice not in visitados:
            visitados.append(vertice)

            lista_vizinhos = vizinhos(grafo, vertice)

            for v in lista_vizinhos:
                na_fila = False

                for item in fila:
                    if item[0] == v:
                        na_fila = True

                if not na_fila and v not in visitados:
                    novo_caminho = caminho + [v]
                    fila.append((v, novo_caminho))

    return []




def busca_profundidade(grafo, origem):

    if origem not in grafo:
        print("O vertice informado nao existe!")
        return []

    visitados = []

    pilha = []

    pilha.append(origem)

    while pilha:

        vertice = pilha.pop()

        if vertice not in visitados:

            visitados.append(vertice)

            lista_vizinhos = vizinhos(grafo, vertice)

            for v in reversed(lista_vizinhos):

                if v not in visitados and v not in pilha:

                    pilha.append(v)

    return visitados




def percurso_valido(grafo, caminho):

    if not caminho:

        return False



    for vertice in caminho:

        if vertice not in grafo:

            return False



    for i in range(len(caminho) - 1):

        origem = caminho[i]

        destino = caminho[i + 1]



        if not existe_aresta(grafo, origem, destino):

            return False



    return True





def main():

    grafo = criar_grafo()



    print("===== TIPO DE GRAFO =====")

    print("1 - Direcionado")

    print("2 - Nao direcionado")



    while True:

        tipo = input("Escolha o tipo: ")



        if tipo == "1" or tipo == "2":

            break

        print("Opcao invalida!")



    nao_direcionado = tipo == "2"



    while True:

        print("\n========== MENU GRAFO ==========")

        print("1 - Exibir grafo")

        print("2 - Inserir vertice")

        print("3 - Inserir aresta")

        print("4 - Remover vertice")

        print("5 - Remover aresta")

        print("6 - Listar vizinhos")

        print("7 - Verificar aresta")

        print("8 - Calcular grau dos vertices")

        print("9 - Verificar percurso")

        print("10 - Busca em largura")

        print("11 - Encontrar menor caminho")

        print("12 - Busca em profundidade (DFS)")

        print("0 - Sair")

        print("================================")



        opcao = input("Escolha uma opcao: ")



        if opcao == "1":

            exibir_grafo(grafo)



        elif opcao == "2":

            vertice = input("Digite o vertice: ").strip()

            inserir_vertice(grafo, vertice)



        elif opcao == "3":

            origem = input("Origem: ").strip()

            destino = input("Destino: ").strip()



            inserir_aresta(

                grafo, origem, destino, nao_direcionado

            )



        elif opcao == "4":

            vertice = input("Vertice para remover: ").strip()

            remover_vertice(grafo, vertice, nao_direcionado)



        elif opcao == "5":

            origem = input("Origem: ").strip()

            destino = input("Destino: ").strip()



            remover_aresta(

                grafo, origem, destino, nao_direcionado

            )



        elif opcao == "6":

            vertice = input("Digite o vertice: ").strip()

            listar_vizinhos(grafo, vertice)



        elif opcao == "7":

            origem = input("Origem: ").strip()

            destino = input("Destino: ").strip()



            if existe_aresta(grafo, origem, destino):

                print("A aresta existe!")

            else:

                print("A aresta nao existe!")



        elif opcao == "8":

            graus = grau_vertices(grafo, nao_direcionado)



            for vertice in graus:

                print("\nVertice:", vertice)



                if nao_direcionado:

                    print("Grau:", graus[vertice]["total"])

                else:

                    print("Grau de entrada:",

                          graus[vertice]["entrada"])

                    print("Grau de saida:",

                          graus[vertice]["saida"])

                    print("Grau total:",

                          graus[vertice]["total"])



        elif opcao == "9":

            entrada = input(

                "Digite o percurso (ex: A,B,C): "

            )



            caminho = [

                v.strip() for v in entrada.split(",")

            ]



            if percurso_valido(grafo, caminho):

                print("Percurso valido!")

            else:

                print("Percurso invalido!")


        
        elif opcao == "10":
            origem = input("Digite o vertice inicial: ").strip()

            resultado = busca_largura(grafo, origem)

            if resultado:
                print("Ordem da busca em largura:", resultado)


        
        elif opcao == "11":
            origem = input("Digite o vertice inicial: ").strip()
            destino = input("Digite o vertice destino: ").strip()

            caminho = menor_caminho(grafo, origem, destino)

            if caminho:
                print("Menor caminho:", caminho)
                print("Quantidade de arestas:", len(caminho) - 1)
            else:
                print("Nao foi encontrado um caminho!")


        elif opcao == "12":

            origem = input(
                "Digite o vertice inicial: "
            ).strip()

            resultado = busca_profundidade(grafo, origem)

            if resultado:
                print("Ordem da busca em profundidade:", resultado)


        elif opcao == "0":

            print("Encerrando programa...")

            break



        else:

            print("Opcao invalida!")





if __name__ == "__main__":

    main()