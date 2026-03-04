#!/usr/bin/env python3
"""Jogo de depopular: elimine personagens até restar o campeão do caos."""

from __future__ import annotations

import random


PERSONAGENS = [
    {"nome": "Palhaço Quântico", "valor": 8, "descricao": "Faz piada em 3 dimensões."},
    {"nome": "Pato CEO", "valor": 7, "descricao": "Fatura milhões, mas só grasna."},
    {"nome": "Ninja do Café", "valor": 9, "descricao": "Some e aparece com espresso."},
    {"nome": "Conde Inútil", "valor": 2, "descricao": "Elegante, mas não ajuda em nada."},
    {"nome": "Estagiário Invisível", "valor": 3, "descricao": "Ninguém sabe o que faz."},
    {"nome": "Bardo do Bug", "valor": 6, "descricao": "Canta e resolve metade dos erros."},
]


def mostrar_personagens(elenco: list[dict[str, object]]) -> None:
    print("\n=== Personagens no jogo ===")
    for idx, p in enumerate(elenco, start=1):
        print(f"{idx}. {p['nome']} (popularidade {p['valor']}) — {p['descricao']}")


def turno_jogador(elenco: list[dict[str, object]]) -> None:
    while True:
        escolha = input("\nEscolha um número para depopular (eliminar): ").strip()
        if not escolha.isdigit():
            print("Digite um número válido.")
            continue

        indice = int(escolha) - 1
        if 0 <= indice < len(elenco):
            removido = elenco.pop(indice)
            print(f"💥 {removido['nome']} foi depopularizado!")
            return

        print("Número fora da lista.")


def evento_caotico(elenco: list[dict[str, object]]) -> None:
    if len(elenco) < 2:
        return

    if random.random() < 0.45:
        escolhido = random.choice(elenco)
        bonus = random.randint(1, 3)
        escolhido["valor"] = int(escolhido["valor"]) + bonus
        print(
            f"✨ Evento caótico: {escolhido['nome']} viralizou e ganhou +{bonus} de popularidade!"
        )


def anunciar_vencedor(elenco: list[dict[str, object]]) -> None:
    vencedor = elenco[0]
    print("\n🏆 Campeão do depopular:")
    print(f"{vencedor['nome']} com popularidade {vencedor['valor']}!")
    print("Descrição:", vencedor["descricao"])


def main() -> None:
    print("🎮 Bem-vindo ao Jogo de Depopular!")
    elenco = [p.copy() for p in PERSONAGENS]
    random.shuffle(elenco)

    while len(elenco) > 1:
        mostrar_personagens(elenco)
        turno_jogador(elenco)
        evento_caotico(elenco)

    anunciar_vencedor(elenco)


if __name__ == "__main__":
    main()
