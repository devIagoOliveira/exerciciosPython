def fechamentoTurma(notas):
    media = sum(notas.values()) / len(notas)

    print(f"A média da turma é {media}, alunos aprovados:")

    alunosAprovados = []

    for aluno, nota in notas.items():
        if nota > media:
            alunosAprovados.append(aluno)

    return alunosAprovados

"""
import ex03

notas = {
    "Iago": 8, "Bryan": 9.5, "Manu": 7.5, "Amanda": 7.5, "Igor": 6, "Vivi": 6.5
}

fim = ex03.fechamentoTurma(notas)

print(fim)
"""