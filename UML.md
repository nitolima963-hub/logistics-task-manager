### Diagrama de Classes UML (Estrutura de Dados)

```mermaid
classDiagram
    class Tarefa {
        +int id
        +string titulo
        +string status  // A Fazer, Em Progresso, Concluído
        +string prioridade // Alta, Média, Baixa (Gestão de Mudanças)
    }
### Diagrama de Casos de Uso UML (Requisitos)

```mermaid
%% Diagrama de Casos de Uso (UML)
graph TD
    subgraph Sistema de Gerenciamento de Tarefas
        UC1[Gerenciar Tarefas (CRUD)]
        UC2[Priorizar Tarefa]
        UC3[Visualizar Fluxo (Kanban)]
    end

    Actor(Usuário)
    Actor --> UC1
    Actor --> UC2
    Actor --> UC3
