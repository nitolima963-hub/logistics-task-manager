# 🚀 TechFlow Solutions - Sistema de Gerenciamento de Tarefas Ágil

Este projeto foi desenvolvido para uma **startup de logística**, com o objetivo de facilitar o acompanhamento de tarefas, priorizar atividades críticas e monitorar o desempenho da equipe em tempo real.

---

## 🎯 Objetivo
Fornecer uma ferramenta de **gerenciamento de tarefas baseada em metodologias ágeis**, permitindo que a equipe visualize o progresso e mantenha a produtividade.

---

## 🧱 Escopo do Projeto
- CRUD completo para tarefas (Criar, Ler, Atualizar e Excluir)
- Acompanhamento por status (A Fazer, Em Progresso, Concluído)
- Priorização de tarefas críticas
- Painel Kanban no GitHub Projects
- Testes automatizados com GitHub Actions

---

## ⚙️ Tecnologias
- Python + Flask  
- Banco de dados SQLite  
- GitHub Actions (para testes automatizados)

---

## ▶️ Como Executar
```bash
git clone https://github.com/nitolima963-hub/logistics-task-manager
cd logistics-task-manager
python app.py

## 🔄 Gestão de Mudanças (Alteração de Escopo)

**Motivação:**
O cliente (startup de logística) solicitou a adição de um campo de prioridade (`Alta`, `Média`, `Baixa`) para otimizar o acompanhamento das tarefas críticas, demonstrando a adaptabilidade do projeto ágil.

**Mudança Implementada:**
Adição do campo `priority` (com valor padrão 'Média') ao modelo de tarefa, e atualização da documentação para refletir a nova funcionalidade.
