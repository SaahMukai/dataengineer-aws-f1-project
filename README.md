# dataengineer-aws-f1-project

#### "Como uma equipe de Fórmula 1 pode usar dados históricos para analisar rivais e melhorar suas decisões estratégicas em corridas futuras?"

Neste projeto, assumo o papel de um analista de desempenho de uma equipe de F1. Usando dados históricos da categoria para:

- Identificar padrões de vitória entre pilotos e escuderias;

- Avaliar desempenhos por pista, temporada e condições climáticas;

- Entender perda de posições (ex.: pit stops, voltas lentas, falhas mecânicas);

- Preparar benchmarks e simulações para novos pilotos com base em históricos;

- Implementar boas práticas de governança com o AWS DataZone, facilitando o consumo e a catalogação de dados para o time técnico.

# F1 Data Engineer Project

### 1. Objetivo do Projeto

Criar um pipeline de dados da Fórmula 1 que permita ingerir, processar e analisar informações de corridas, equipes e pilotos, utilizando AWS e boas práticas de engenharia de dados.
Caso de negócio fictício: a F1 deseja gerar insights estratégicos sobre desempenho de pilotos, construtores e treinos, para melhorar decisões de equipe e engajamento de fãs.

### 2. Arquitetura da Solução

Diagrama resumido da arquitetura:

  Raw Data (CSV/Kaggle)
        │
        ▼
  S3 Raw Bucket
        │
        ▼
  AWS Glue (ETL)
        │
        ▼
  S3 Trusted Bucket + Glue Catalog
        │
        ▼
  AWS Athena (queries)
        │
        ▼
  Lake Formation + DataZone (governança)
        │
        ▼
  QuickSight (visualizações e dashboards)


--> Componentes principais:

- S3 Buckets: armazenamento de dados raw e trusted.

- AWS Glue: transformação de dados, limpeza e catálogo.

- AWS Athena: consultas SQL serverless sobre dados confiáveis.

- Lake Formation / DataZone: controle de acesso, governança e catalogação de dados.

- QuickSight: dashboards interativos e análise de KPIs.

--> Justificativa dos componentes:
Cada componente foi escolhido para garantir escalabilidade, governança e análise rápida de dados sem necessidade de infraestrutura gerenciada.


### 3. Escopo Planejado

Ingestão de datasets de corridas, pilotos, construtores, treinos e resultados.

Transformação e limpeza de dados com Glue (ex.: remoção de duplicatas, tratamento de nulos).

Organização dos dados em buckets raw e trusted.

Catalogação de dados no Glue para consultas via Athena.

Criação de dashboards no QuickSight respondendo perguntas de negócio.

Aplicação de boas práticas de governança com Lake Formation e DataZone.


### 4. Escopo Realizado

Todos os datasets do Kaggle foram carregados no S3 raw e transformados para trusted.

Criados crawlers Glue para cada tabela (ex.: crawler_circuits, crawler_races, etc.).

Dados catalogados no Glue Catalog e consultas testadas via Athena.

Dashboards no QuickSight com KPIs relevantes (ex.: melhor piloto por corrida, desempenho de construtores, comparativo de tempos de treinos).

Governança aplicada via tags, Lake Formation e DataZone para controle de acesso e rastreabilidade.

Limpeza básica de dados: linhas inválidas ou com valores “N” ignoradas nos dashboards.


### 5. Boas Práticas e Pontos de Atenção

Naming conventions: crawlers, buckets e tabelas seguem padrão claro (f1_<tipo>_dev).

Tags e governança: todas as tabelas e buckets principais possuem tags para DataZone e Lake Formation.

Tratamento de dados nulos e inválidos: Athena consultas ignoram registros com valores “N” ou nulos.

Separação de ambientes: buckets com sufixos _dev para diferenciar de produção.

Documentação contínua: README atualizado com arquitetura e escopo.


### 6. Perguntas de Negócio e Dashboards (QuickSight) *dividir em 4 categorias (separadas) cada uma com 3 perguntas*


- Qual piloto teve o melhor tempo médio por corrida em cada temporada? --> best_lap_per_driver_per_year

- Qual construtor apresentou melhor desempenho acumulado em treinos e corridas?

- Como o desempenho do piloto varia entre treinos e corridas?

- Qual corrida teve maior número de mudanças de posições durante a temporada?

- Análise de tempos de qualificação e correlação com resultados finais.
